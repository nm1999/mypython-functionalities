import speech_recognition as sr
import pyttsx3

# initiating a speaking female robot
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)

# initiating a listening robot
rec = sr.Recognizer()


                    # Starting a robot conversation
with sr.Microphone() as source:
    audio = rec.listen(source)
    text = rec.recognize_google(audio)
    Hello = "{}".format(text)

    if 'hello' in Hello or 'hi' in hello or 'good morning':
        engine.say("Hello")
        engine.runAndWait() 
    
    with sr.Microphone() as source:
        audio1 = rec.listen(source)
        text1 = rec.recognize_google(audio1)
        ask = "{}".format(text1)

        if 'how are you ' in ask or 'how do you do' in ask:
            engine1 = say("Am fine , thank you")
            engine1.runAndWait()





