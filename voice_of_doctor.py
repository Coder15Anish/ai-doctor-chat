#Step1a: Setup Text to Speech–TTS–model with gTTS
from gtts import gTTS
import streamlit as st
import io
import base64


def speak(doctor_response):
    if doctor_response:
        # Generate speech
        tts = gTTS(doctor_response,lang="en",slow=False)
        
        # Save to in-memory file
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        # Encode audio to base64
        b64_audio = base64.b64encode(mp3_fp.read()).decode()

        # Create HTML audio tag with autoplay
        audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        """

        # Inject HTML
        st.markdown(audio_html, unsafe_allow_html=True)

    return
