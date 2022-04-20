// Constants
const audio_element = document.querySelector("audio#audio")
const tts_string_element = document.querySelector("textarea#string")
const tts_lang_element = document.querySelector("select#lang")
const audio_url = "out/audio.wav"
const download_element = document.querySelector("a#download")

// Functions
function set_audio_data_js() {
    let date = new Date()

    audio_element.src = `${audio_url}?cb=${date}`
    download_element.download = `audio-${Number(date)}.wav`
    download_element.parentElement.hidden = false

    audio_element.load()
    audio_element.play()
}

// Config
document.querySelector("button#submit").onclick=async () => {
    await eel.update_audio_data_py(
        tts_string_element.value,
        tts_lang_element.value
    )()
}


// Exposures
eel.expose(set_audio_data_js)