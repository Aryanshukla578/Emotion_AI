# 🎭 Emotion to Expression AI

Transform your **voice or text** into expressive poetry and AI-generated art — powered by emotional intelligence.

🟢 Live App:  
- 🔗 [Streamlit (Original)](https://emotionai-dzjpecbetxzpyybquwlbqq.streamlit.app/)  
- 💖 [Lovable App](https://expressive-ai-poetry-verse.lovable.app/)

---

## 🧠 What It Does

**Emotion to Expression AI** is an interactive experience that:

🎙️ Accepts **voice or typed input**  
🔍 Detects the **emotion** behind your words  
✨ Generates a **poetic expression** for that emotion  
🖼️ Displays a **visual** that represents your feeling  

---

## 🌌 Screenshot

![Emotion AI Screenshot](assets/night-sky.jpg)


*A poetic night: stars echoing your mood.*

---

## 🌟 Features

| Feature              | Description |
|----------------------|-------------|
| 🗣️ Speech & Text Input | Speak or type to express your feelings |
| 🧠 Emotion Detection | Uses `distilroberta` transformer model |
| ✨ Poetic Generator  | Beautiful metaphors for your emotions |
| 🎨 AI Visual Art     | Emotion-linked abstract images |
| 📱 Mobile & Desktop | Fully responsive UI via Streamlit |

---

## 📦 Tech Stack

- `Streamlit` — Frontend
- `Transformers` (Hugging Face) — Emotion classification
- `SpeechRecognition` + `PyAudio` — Voice input
- `Unsplash` — Image backgrounds

---

## 🚀 Run Locally

```bash
git clone https://github.com/your-username/emotion-to-expression-ai.git
cd emotion-to-expression-ai
pip install -r requirements.txt
streamlit run app.py
💡 If you're on Windows, ensure PyAudio is installed correctly using .whl files if needed.
emotion-to-expression-ai/
│
├── app.py                # Main Streamlit app
├── utils.py              # Emotion detection & poetic generation
├── requirements.txt      # Dependencies
└── README.md             # You're here :)
❤️ Credits
Emotion model: j-hartmann/emotion-english-distilroberta-base

Images: Unsplash

Voice: Python's speech_recognition library

🚀 Future Features (Ideas)
🎭 Emotion intensity graphs

🎨 AI image generation (using Stable Diffusion)

🗃️ Emotion journaling dashboard

🎧 Background music matching the detected mood

📜 License
MIT License — use, remix, and improve freely. Just give credit 😊

Made with 💚 by Aryan Shukla

Let me know if you want:
- A version with badges and GitHub deploy instructions
- A fancy animated GIF demo
- A Notion-style whitepaper page
