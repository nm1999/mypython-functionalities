import pyttsx3

engine = pyttsx3.init()
# engine.setProperty('rate',1)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# 0 - male voice  
# 1 - female voice
engine.say("mwasuuuze mutya")

engine.runAndWait()