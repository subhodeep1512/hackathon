import os
import boto3
import moviepy.editor as mp
import whisper
from transformers import pipeline

# ------------------ CONFIG ------------------
video_file = "./uploads/suffering_part.mp4"
audio_file = "./uploads/audio/extracted_audio.wav"
bucket_name = "aititans515287845833bucket"

sentiment_s3_folder = "sentiment-analysis"
summarization_s3_folder = "Summarization"

local_base_dir = "./models"
sentiment_local_dir = os.path.join(local_base_dir, "sentiment-analysis")
summarization_local_dir = os.path.join(local_base_dir, "Summarization")

# Create necessary folders
os.makedirs(os.path.dirname(audio_file), exist_ok=True)
os.makedirs(sentiment_local_dir, exist_ok=True)
os.makedirs(summarization_local_dir, exist_ok=True)

# ------------------ STEP 1: Download S3 folders ------------------
def download_s3_folder(bucket_name, s3_folder, local_dir):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        if not obj.key.endswith("/"):
            local_file_path = os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            print(f"Downloading {obj.key} to {local_file_path}")
            bucket.download_file(obj.key, local_file_path)

download_s3_folder(bucket_name, sentiment_s3_folder, sentiment_local_dir)
download_s3_folder(bucket_name, summarization_s3_folder, summarization_local_dir)

# ------------------ STEP 2: Video to Audio ------------------
print("\nExtracting audio from video...")
video = mp.VideoFileClip(video_file)
audio = video.audio
audio.write_audiofile(audio_file)

# ------------------ STEP 3: Whisper Transcription ------------------
print("\nTranscribing audio using OpenAI Whisper...")
whisper_model = whisper.load_model("base")
result = whisper_model.transcribe(audio_file)
text = result.get("text", "").strip()
print("Whisper Transcription:\n", text)

# ------------------ STEP 4: Summarization ------------------
def summarize_text(text_to_summarize):
    print("\nSummarizing text...")
    summarizer = pipeline("summarization", model=summarization_local_dir)
    summary = summarizer(text_to_summarize, max_length=150, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text']
    print("Summary:\n", summary_text)
    return summary_text

# ------------------ STEP 5: Emotion Analysis ------------------
def analyze_state_and_suggest(text_to_analyze):
    print("\nAnalyzing emotional state...")
    classifier = pipeline("sentiment-analysis", model=sentiment_local_dir)
    results = classifier(text_to_analyze)
    main_emotion = results[0]['label']
    confidence = results[0]['score']

    print(f"Detected Emotion: {main_emotion} (Confidence: {confidence:.2f})")

    if main_emotion in ['sadness', 'anger', 'fear', 'disgust'] and confidence > 0.7:
        return "Strong negative emotions detected. Consider consulting a doctor or mental health expert."
    elif main_emotion == 'neutral' or (main_emotion == 'joy' and confidence < 0.6):
        return "Neutral or mild positive state. Mindfulness or yoga may help maintain well-being."
    elif main_emotion == 'joy' and confidence >= 0.6:
        return "Positive emotional state! Keep up the good work and maintain healthy habits."
    elif main_emotion == 'surprise':
        return "Surprise detected. Yoga may help manage excitement or stress."
    else:
        return "Emotional state is ambiguous. Consider general well-being activities."

# ------------------ STEP 6: Run Pipeline ------------------
if __name__ == "__main__":
    print("-" * 60)

    if not text:
        print("No transcription found. Exiting.")
    else:
        print("\n--- Summarizing ---")
        summarized_text = summarize_text(text)

        print("\n--- Emotion Analysis ---")
        suggestion = analyze_state_and_suggest(text)

        print("\n--- Recommendation ---")
        print(suggestion)