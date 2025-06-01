# 🎭 Emotion to Expression AI

Turn raw human emotion into poetic expression — with a single voice or text input.  
This Streamlit app detects **emotions from your voice or written words**, then responds with a **beautiful AI-generated poetic interpretation** and **abstract image**.

![App Screenshot](assests/night_sky.jpg)


## 🌐 Live Demos

- 📝 [Text-based Emotion App](https://emotionai-dzjpecbetxzpyybquwlbqq.streamlit.app/)
- 🔊 [Voice-based Poetic Expression](https://expressive-ai-poetry-verse.lovable.app/)

---

## 🧠 Features

- 🎙️ **Voice Input** (via microphone)
- 📝 **Text Input** (manual typing)
- 🧠 Emotion detection using NLP
- 🧾 Generates **poetic expression** from emotion
- 🖼️ Abstract background image based on emotion (via Unsplash API)

---

## 📦 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **Libraries**:
  - `speechrecognition`
  - `transformers`
  - `torch`
  - `streamlit`
  - `requests`
  - `pyaudio` (for voice)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Aryanshukla578/Emotion_AI.git
cd Emotion_AI

pip install -r requirements.txt
streamlit run app.py
Emotion_AI/
├── app.py               # Main Streamlit app
├── utils.py             # Emotion detection + poetry generator
├── requirements.txt     # Dependency list
├── assets/
│   └── night_sky.jpg    # Screenshot used in README
└── README.md
🧠 Emotion Classes Detected
Joy

Sadness

Anger

Fear

Love

Neutral

📝 Example Output
Input: I'm feeling lost today.
→ Detected Emotion: Sadness
→ Poetic Line: "Rain on forgotten pages."

📜 License
This project is licensed under the MIT License — feel free to modify or build upon it.

🙌 Credits
Created by Aryan Shukla

Emotion model: j-hartmann/emotion-english-distilroberta-base

Visuals: Unsplash API

“From feelings to verses, let AI be your silent poet.”

---

✅ **Next Steps:**
- Place your `night_sky.jpg` image inside a folder named `assets/` at the root of your repo.
- Push the updated `README.md`.

Let me know if you'd like a badge layout (Build, Python version, etc.) or a deploy button for Streamlit Cloud.
