import streamlit as st

from utils import detect_emotion, generate_expression

st.set_page_config(page_title="🎭 Emotion to Expression AI", layout="centered")
st.title("🎙️ Emotion to Expression AI")
st.subheader("Turn Your Voice into Artful Expression")

# TEXT INPUT OPTION
user_text = st.text_input("✍️ Type your sentence here:")

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
