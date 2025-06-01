# 🎭 Emotion to Expression AI

Turn your **emotions** into **poetic expressions** with this intelligent AI app. Powered by NLP and deep learning, this project allows users to input text or speech and receive emotionally-tuned poetic responses with matching visual themes.

![App Screenshot](assets/night_sky.jpg)

## 🌐 Live Demos

- 🔗 [Streamlit Demo](https://emotionai-dzjpecbetxzpyybquwlbqq.streamlit.app/)
- 🔗 [Lovable App Mirror](https://expressive-ai-poetry-verse.lovable.app/)

---

## 💡 Features

- 🎤 **Voice-to-Emotion**: Speak your heart — the app transcribes and analyzes.
- 📝 **Text-to-Emotion**: Type in any sentence to detect emotional tone.
- 🖋️ **Poetic Generator**: Converts emotions into creative, metaphorical verses.
- 🖼️ **Visual Art**: Auto-generates artistic imagery based on detected emotion.

---

## 🤖 Tech Stack

| Layer       | Tools/Tech Used |
|-------------|-----------------|
| UI          | Streamlit       |
| NLP Model   | 🤗 Transformers (DistilRoBERTa) |
| Speech      | SpeechRecognition (Google API) |
| Styling     | Unsplash API (image query), CSS via Streamlit |
| Logic       | Python, Custom Templates |

---

## 🚀 Getting Started

### 🔧 Installation

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
