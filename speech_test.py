import speech_recognition as sr
import pyttsx3 as tts

r = sr.Recognizer()
engine = tts.init()

# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

def loop_echo() -> None:
    """ TTS echo mic input until 'goodbye' """
    while True:
        with sr.Microphone() as source:
            print("listening:")
            # audio = r.listen(source, snowboy_configuration=("snowboy", ["Aika.pmdl"]))
            audio = r.listen(source)  # hotword thing comes later
            try:
                text = r.recognize_google(audio)
                engine.say(text)
                if text.lower() == "goodbye": break
                engine.runAndWait()
                print("you said: " + text)
            except:
                print("Try again.")
    engine.say("take care")
    engine.runAndWait()

loop_echo()
# with sr.AudioFile("test.wav") as source:
#     audio = r.record(source)
#     # try:
#     text = r.recognize_google(audio)
#     # except:
#     #     print("sorry")
#     print(text)
