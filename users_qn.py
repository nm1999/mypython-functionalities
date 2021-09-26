import random 
import webbrowser
print("\n\n")
greeting = ['Anyone here !!!!!','Talk to mi' ,'Hello' , 'Hey' ,'Anybody talk to me !!!']
user_answers = ['Your welcome ' ,'Am gad that you here ' ,'Thank you for coming ']
words_for_sick =['Just relax  , am going to help you','Now that you here that is going to be sorted','Am going to help about that' ,'I am going to help you']
apologies = ['Sorry we cannot get your issue' ,'please try to elaborate more your problem' ,'Summarise your statements please']

greeting_out = random.choice(greeting)
user_name = input(greeting_out + " , Am MATIA . What is your name ?\n")

user_answer_out = random.choice(user_answers)

main = input(user_answer_out + " , How can i help you ? \n")

                   # if the user enters anything related to sickness

if 'sick' in main or 'doctor' in main or 'not feeling well' in main:

    words_for_sick_out = random.choice(words_for_sick)
    print(words_for_sick_out + " , " + str(user_name) + "\n")

    print("I want to help you detect your sickness ,\n ENTER ONE OR MORE OF THE SIGNS AND SYMPTOMS OPTIONS ASKED \n")


        # if the user enters anything related to buyibg something
elif 'food' in main or 'market' in main or 'shopping' in main or 'buy' in main:
    print("Am going to connect you to the potential sellers.")
    country = input("Enter your country name\n")

    if 'Uganda' in country or 'Kenya' in country or 'Tanzania' in country or 'Rwanda' in country:
        try:
            webbrowser.open("www.jumia.com")
        except:
            webbrowser.open("www.yammieshoppers.com")
    else:
        webbrowser.open("www.amazon.com")
elif 'where' in main or 'lost' in main or 'map' in main:
    webbrowser.open("www.googlemaps.com")
else:
    display_apology = random.choice(apologies)

    

