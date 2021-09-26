import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print("speak")
    voice = rec.listen(source)
    try:
        text = rec.recognize_google(voice)
        print("{}".format(text))
    except:
        print("failed to recognise your voice")