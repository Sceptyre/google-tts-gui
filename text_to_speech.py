from google.cloud import texttospeech_v1beta1 as texttospeech
import os

APIKEYFILEPATH = os.path.abspath(".apiKey")

def text_to_speech(text, langCode="EN-US"):
    if not langCode:
        LANGCODE = "en-US"
    else:
        LANGCODE = langCode


    # Set environment variable to path of api key file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = APIKEYFILEPATH

    # Instantiates tts client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(
        ssml=text
    )

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code=LANGCODE,
        name=f"{LANGCODE}-WaveNet-F"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MULAW,
        sample_rate_hertz=8000
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response.audio_content