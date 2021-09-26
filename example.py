

import speech_recognition as sp
rec = sp.Recognizer()
my_micro = sp.Microphone(device_index=1)

with my_micro as source:
    print("Say something.....")
    audio = rec.listen(source)

    to_text = rec.recognize_google(audio)

print(to_text)
