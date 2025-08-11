# hackathon
🧠 Together is an AI-powered mental health companion that transcribes and summarizes patient's videos, detects emotions, and recommends actions. It helps patients track emotional well-being, spot patterns, and share insights with therapists for more personalized support.
🚀 Features
🎙 Video-to-Text Transcription

Converts video diaries into accurate, time-stamped transcripts.

Uses OpenAI Whisper for high-accuracy speech recognition.

Audio preprocessing via ffmpeg and moviepy ensures clarity.

📝 Summarization & Emotion Detection

Summarization with sshleifer/distilbart-cnn-12-6 – optimized for abstractive text summarization.

Emotion classification with j-hartmann/emotion-english-distilroberta-base – detects anger, joy, sadness, fear, surprise, disgust, and neutral emotions.

Identifies symptoms, emotional triggers, and provides recommendations.

📊 Emotional Progress Tracking

Monitors emotional changes over time.

Visual dashboards to track trends and improvements.

Suggests wellness actions (e.g., yoga, counseling, relaxation exercises).

☁ Cloud-Ready Deployment

Streamlit interface for easy video recording/upload.

Backend powered by AWS SageMaker for scalable inference.

Model files stored in AWS S3 for efficient deployment.

🛠 Tech Stack
Component	Technology
Speech-to-Text	OpenAI Whisper
Summarization	DistilBART CNN-12-6
Emotion Detection	Emotion English DistilRoBERTa Base
Frontend	Streamlit
Backend	AWS SageMaker
Storage	AWS S3
Audio Processing	ffmpeg, moviepy

📦 Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/your-username/together-ai.git
cd together-ai

# Install dependencies
pip install -r requirements.txt

# Download summarization model
git lfs install
git clone https://huggingface.co/sshleifer/distilbart-cnn-12-6 summarization_model

# Download emotion detection model
git clone https://huggingface.co/j-hartmann/emotion-english-distilroberta-base emotion_model

# Run the app
streamlit run app.py
📌 Usage
Record or Upload your daily video diary in the Together interface.

The app:

Extracts audio & transcribes it using Whisper.

Summarizes key points.

Detects your emotional state.

Suggests wellness actions.

View Your Dashboard to monitor your mental health journey.

Optionally share insights with a mental health professional.

📅 Roadmap
 Add LangChain/CrewAI for advanced health recommendations.

 Integrate guided meditation and CBT activities.

 Enable secure in-app therapist-patient chat.

 Add predictive analytics for emotional health forecasting.

👥 Team – AWS Hackathon “AI Titans”
Mentor: Virendra Bhatia

Team Members: Subhodeep Mondal, Rakesh Krishnamurthy, Bhupendra Kumar, Binod Kumar Biswal, Abhirup Majumder, Priya Mandal

📜 License
MIT License – you’re free to use, modify, and distribute with attribution.
