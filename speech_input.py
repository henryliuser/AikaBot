import speech_recognition as sr
import pyttsx3 as tts
import voice_commands

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

def hotword_hack(text):
    close = ['aika', 'debug', 'ikea', 'iker', 'ico', 'ayto']
    for w in close:
        idx = text.find(w)
        if idx != -1: return idx
    return -1

def take_voice_command(ctx, source):
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()
        print(text)
    except:
        print("unknown")
        return
    # with open("temp_speech.wav", "wb") as file:  # don't need yet
    #     file.write(audio.get_wav_data())
    # print(ctx.message.author, text)
    aika = hotword_hack(text)
    if aika == -1: return
    else: text = text[len('aika '):]

    for c in voice_commands.commands.keys():
        loc = text.find(c)
        if loc == -1: continue
        left_arg = text[:loc].strip()
        right_arg = text[loc + len(c):].strip()
        return voice_commands.commands[c](left_arg, right_arg)

if __name__ == '__main__':
    # loop_echo()
    with sr.Microphone() as source:
        while True:
            print(take_voice_command(5, source))


# with sr.AudioFile("test.wav") as source:
#     audio = r.record(source)
#     # try:
#     text = r.recognize_google(audio)
#     # except:
#     #     print("sorry")
#     print(text)
