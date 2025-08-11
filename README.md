# 🧠 Together – AI-Powered Mental Health Companion

🧠 Together is an AI-powered mental health companion that transcribes and summarizes patient's videos, detects emotions, and recommends actions. It helps patients track emotional well-being, spot patterns, and share insights with therapists for more personalized support.

---

## 🚀 Features

- **🎙 Video-to-Text Transcription**  
  - Generates accurate transcripts from videos uploaded by patients.  
  - Uses **[OpenAI Whisper](https://github.com/openai/whisper)** for high-accuracy speech recognition across accents and noise levels.  
  - Audio preprocessing with `ffmpeg` and `moviepy` for clarity.  

- **📝 Summarization & Emotion Detection**  
  - Summarization with **[sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6)** – a distilled BART model optimized for abstractive summarization.  
  - Emotion classification with **[j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)** – detects anger, joy, sadness, fear, surprise, disgust, and neutral emotions.  
  - Identifies emotional triggers and suggests mental wellness actions.

- **📊 Emotional Progress Tracking**  
  - Displays progress in interactive dashboards.  
  - Allows checking and managing schedules in the in-app calendar for therapy sessions and wellness activities.

- **☁ Cloud-Ready Deployment**  
  - **Streamlit** interface for easy video recording/upload.  
  - Backend powered by **AWS SageMaker** for scalable inference.  
  - Models stored in **AWS S3** for efficient deployment.

---

## 🛠 Tech Stack

| Component           | Technology |
|--------------------|------------|
| Speech-to-Text     | [OpenAI Whisper](https://github.com/openai/whisper) |
| Summarization      | [DistilBART CNN-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) |
| Emotion Detection  | [Emotion English DistilRoBERTa Base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) |
| Frontend           | Streamlit |
| Backend            | AWS SageMaker |
| Storage            | AWS S3 |
| Audio Processing   | ffmpeg, moviepy |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/together-ai.git
cd together-ai

# Install dependencies
pip install -r requirements.txt

# Install Git LFS for model downloads
git lfs install

# Download summarization model into summarization_model/ folder
git clone https://huggingface.co/sshleifer/distilbart-cnn-12-6 summarization_model

# Download emotion detection model into emotion_model/ folder
git clone https://huggingface.co/j-hartmann/emotion-english-distilroberta-base emotion_model

# Run the Streamlit app
streamlit run app.py
```

---

## 📌 Usage

1. **Record or Upload** your video diary via the Together interface.  
2. The app:
   - Transcribes speech to text using Whisper.
   - Summarizes the conversation using DistilBART.
   - Detects emotional state using DistilRoBERTa.
   - Suggests relevant mental wellness actions.  
3. **View Your Dashboard** to monitor emotional trends and improvements.  
4. **Share Insights** with a therapist for guided support.

---

## 📅 Roadmap

- [ ] Integrate **LangChain/CrewAI** for proactive therapy recommendations.  
- [ ] Add guided meditation and CBT activity suggestions.  
- [ ] Secure in-app chat for therapist-patient communication.  
- [ ] Predictive analytics for early intervention.

---

## 👥 Team – AWS Hackathon “AI Titans”

- **Mentor:** Virendra Bhatia  
- **Team Members:** Subhodeep Mondal, Rakesh Krishnamurthy, Bhupendra Kumar, Binod Kumar Biswal, Abhirup Majumder, Priya Mondal

---

## 📜 License
MIT License – you’re free to use, modify, and distribute with attribution.
