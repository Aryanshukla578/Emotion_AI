# 🎭 Emotion to Expression AI

Transform voice or text into powerful **poetic expressions** and AI-generated visual art — all driven by the **emotion** hidden in your words.

🟢 Live App:  
- 🔗 [Streamlit (Original)](https://emotionai-dzjpecbetxzpyybquwlbqq.streamlit.app/)  
- 💖 [Lovable App](https://expressive-ai-poetry-verse.lovable.app/)

---

## 🧠 What It Does

**Emotion to Expression AI** is an interactive web app that:

🎙️ Converts your **speech or typed text** into text  
🔍 Detects the **underlying emotion** using a powerful NLP model  
✨ Generates a **poetic expression** representing your feeling  
🖼️ Shows a relevant **AI-generated abstract image** based on the emotion  

---

## 🌟 Features

| Feature | Description |
|--------|-------------|
| 🗣️ Speech & Text Input | Speak or type your thoughts |
| 🧠 Emotion Detection | Uses HuggingFace's `distilroberta` model for emotion classification |
| ✨ Poetic Generator | Custom poetic lines for each emotion |
| 🎨 Visual Expression | Unsplash image fetched based on detected emotion |
| 📱 Fully Responsive | Works on desktop and mobile (Streamlit UI) |

---

## 📸 Screenshots

![Emotion Detection](https://i.imgur.com/y3CXyoU.png)
*Example: Speech converted to text, emotion detected as "joy", poetry & art generated.*

---

## 🛠️ How It Works

1. **Speech or Text Input**
   - If you speak: Uses `speech_recognition` + `PyAudio` to transcribe
   - If you type: Directly uses that text

2. **Emotion Analysis**
   - Uses 🤗 `transformers` with `j-hartmann/emotion-english-distilroberta-base` model

3. **Expression Generation**
   - Based on detected emotion, returns a poetic sentence

4. **Visual Rendering**
   - Queries Unsplash for an image like `https://source.unsplash.com/?joy,abstract`

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – UI & interaction
- [Transformers](https://huggingface.co/transformers/) – Emotion model
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Voice input
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) – Microphone access (PC only)
- [Unsplash API](https://unsplash.com/developers) – Emotion-based image generation

---

## 🔧 Local Setup (Optional)

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
