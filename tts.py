import pyttsx3


engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name)

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)
engine.say("Edit: The funny part is I made a post similar to this about Yone over 2 years ago pretty much going over the exact same thing, funny how time flies and still NOTHING has changed.")
engine.runAndWait()