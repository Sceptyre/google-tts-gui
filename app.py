import eel
from text_to_speech import text_to_speech

@eel.expose
def update_audio_data_py(string, lang_code="EN-US"):
    audio_data = text_to_speech(string, lang_code)
    with open('www/out/audio.wav', 'wb') as f:
        f.write(audio_data)
    eel.set_audio_data_js()()


eel.init('www')
eel.start('index.html', size=(320, 480))
