import streamlit as st
import speech_recognition as sr
import os
from utils import detect_emotion, generate_expression
from PIL import Image
import time

st.set_page_config(page_title="🎭 Emotion to Expression AI", layout="centered")

st.title("🎙️ Emotion to Expression AI")
st.subheader("Turn Your Voice into Artful Expression")

# Step 1: Record user audio and save it
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

# Step 2: Convert speech to text
def speech_to_text(audio_file="temp_audio.wav"):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"Speech Recognition API error: {e}"
    except Exception as e:
        return f"Error: {e}"

# Main interface
if st.button("🎤 Start Voice Input"):
    with st.spinner("Recording..."):
        fname = record_audio()
    if fname is None:
        st.stop()

    with st.spinner("Converting Speech to Text..."):
        user_text = speech_to_text(fname)
        st.markdown(f"🗣️ Your Input: `{user_text}`")

        if "Could not understand" in user_text or "Error" in user_text:
            st.warning("😕 Sorry, couldn't understand your voice. Try again.")
        else:
            with st.spinner("🎭 Detecting Emotion..."):
                emotion, score = detect_emotion(user_text)
                poetic = generate_expression(emotion)

                st.success(f"🔍 Detected Emotion: `{emotion}` ({round(score*100, 2)}%)")

                st.markdown("### ✨ Poetic Expression:")
                st.write(poetic)

                st.image(f"https://source.unsplash.com/600x400/?{emotion},abstract", caption="AI Imagined Art", use_column_width=True)

    # Cleanup
    try:
        if fname:
            os.remove(fname)
    except Exception:
        pass

if __name__ == "__main__":
    import os
    os.system('python -m streamlit run app.py')
