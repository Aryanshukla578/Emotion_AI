import streamlit as st
import os
import speech_recognition as sr
from utils import detect_emotion, generate_expression
<<<<<<< HEAD

=======
from PIL import Image
from utils import detect_emotion, generate_expression
>>>>>>> 2440052 ("modified: app.py")
st.set_page_config(page_title="🎭 Emotion to Expression AI", layout="centered")
st.title("🎙️ Emotion to Expression AI")
st.subheader("Turn Your Voice or Text into Artful Expression")

<<<<<<< HEAD
# TEXT INPUT OPTION
user_text = st.text_input("✍️ Type your sentence here:")
=======
user_text = st.text_input("Type your sentence here:")

if st.button("Analyze Emotion"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("🎭 Detecting Emotion..."):
            emotion, score = detect_emotion(user_text)
            poetic = generate_expression(emotion)

            st.success(f"🔍 Detected Emotion: `{emotion}` ({round(score*100, 2)}%)")
            st.markdown("### ✨ Poetic Expression:")
            st.write(poetic)
            st.image(
                f"https://source.unsplash.com/600x400/?{emotion},abstract",
                caption="AI Imagined Art",
                use_container_width=True
            )

def record_audio(filename="temp_audio.wav"):
    recognizer = sr.Recognizer()
    try:
        mic = sr.Microphone()
    except OSError:
        st.error("No microphone found. Please connect a microphone and try again.")
        return None
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        st.info("🎤 Speak now...")
        try:
            audio = recognizer.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            st.warning("⏰ Listening timed out. Please try again.")
            return None
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
    return filename
>>>>>>> 2440052 ("modified: app.py")

if st.button("🔍 Analyze Text Emotion"):
    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Detecting Emotion..."):
            emotion, score = detect_emotion(user_text)
            poetic = generate_expression(emotion)

            st.success(f"🎭 Detected Emotion: `{emotion}` ({round(score*100, 2)}%)")
            st.markdown("### ✨ Poetic Expression:")
            st.write(poetic)
            st.image(
                f"https://source.unsplash.com/600x400/?{emotion},abstract",
                caption="AI Imagined Art",
                use_container_width=True
            )

st.markdown("---")

# AUDIO INPUT OPTION (via upload)
st.subheader("🎵 Or Upload an Audio File (WAV/MP3)")
uploaded_audio = st.file_uploader("Upload your voice file", type=["wav", "mp3"])

def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Speech Recognition API error: {e}"
    except Exception as e:
        return f"Error: {e}"

if uploaded_audio is not None:
    # Save uploaded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_audio.read())

    with st.spinner("🧠 Transcribing Audio..."):
        user_text = speech_to_text("temp_audio.wav")
        st.markdown(f"🗣️ Transcribed: `{user_text}`")

        if "Could not understand" in user_text or "Error" in user_text:
            st.warning("😕 Sorry, couldn't understand your voice. Try another file.")
        else:
            with st.spinner("🎭 Detecting Emotion..."):
                emotion, score = detect_emotion(user_text)
                poetic = generate_expression(emotion)

                st.success(f"🎭 Detected Emotion: `{emotion}` ({round(score*100, 2)}%)")
                st.markdown("### ✨ Poetic Expression:")
                st.write(poetic)
                st.image(
                    f"https://source.unsplash.com/600x400/?{emotion},abstract",
                    caption="AI Imagined Art",
                    use_container_width=True
                )

    # Clean up
    os.remove("temp_audio.wav")
