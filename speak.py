from gtts import gTTS
import os

myText = "Mulago hospital pharmacy department has identified Astra Zeneca and covax from India Johnson and Johnson from UK, Moderna and Faiser from USA.The Director Mawa James recently received the call from the Ministry of Health over the COVID 19 vaccine and the ministry has ear marked 5,000,000 USD for the purchase of the vaccines. Action Non-Government organization in the health sector imported Astra medicine from India into Uganda to be distributed in the central region. On the 15th February 2021 th president launched the Astra vaccination in kinawataka. "

language = 'en'

output = gTTS(text=myText, lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")