from gtts import gTTS

text = "Hello, this is a test of the text-to-speech function."

tts = gTTS(text)
tts.save("speech.mp3")

