import base64
from io import BytesIO
from gtts import gTTS
from gtts.lang import tts_langs


def get_tts_suported_languages():
    try:
        return tts_langs()
    except Exception:
        return {}


def is_tts_supported(language_code):
    supportoed = tts_langs()
    return language_code in supportoed


def synthesize_speech(text, language_code):
    if not text:
        return None
    
    supported_languages = tts_langs()

    if language_code not in supported_languages:
        return None
    
    try:
        audio_buffer = BytesIO()

        tts = gTTS(text=text, lang=language_code)
        tts.write_to_fp(audio_buffer)
        
        audio_buffer.seek(0)

        audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")
        return audio_base64
    except Exception:
        return None

