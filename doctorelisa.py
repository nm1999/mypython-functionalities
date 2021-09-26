import random
print(" YOUR WLECOME TO DOCTOR ELISA PROGRAM ,\n WE HELP U DETECT SICKNESS \n We request that English is used for all responses.")
print("========================================================================")
qn = input("Hello....!!!\n ")
responses = ['hey' , 'hello' ,'Good morning' ,'Hi' ,'Whats up']
select = random.choice(responses)


if responses in qn:
   print("THE DETAILS YOU GIVE , WILL NOT BE SHARED BY ANYONE OR ORGANISATION\n NO THIRD PARTY IS INVOLVED")
   name = input("I am Dr.ELISA , What is your name ?\n ")

   location = input("Which district do you come from? ")

   dob = input("In which year were you born e.g 2020 ?\n")

   signs = input("\nDo you have:  diahorrea , cough , vomit , running nose , joint pain ? If yes write it \n  ")

   symptom = input("\n Do you have : stomachache ,headache , constipation , heart burn ? \n")

   temp = input("\nIs your temperature : low , high , normal?\n ")

   sense = input("\n Is your sense of smell and taste : bad fair good")

   appetite = input("\n Is your  appetite : low , high , normal ? \n ")

   #Age 
   age = 2021 - int(dob) 

#    sickness conditions 
   if 'headache' in symptom and 'vomit' in signs and 'high' in temp and 'joint pain' in signs :
       print(name +"  , you have Malaria")

       precautions = input("Do you need medicine recommendation ? ")

       if 'yes' in precautions:

           if age >18 :
               print("\n\n"+name + " your " + str(age) + "years above 18 , take :\n 1x2 Panadol extra \n 3X2 Quatum \n Take alot of fluids \n\n ")
               print("If condition persist , Visit"+ location +"health centre IV for blood check up")
               prevent = input("Do you need ways of preventing Malaria ?\n")

               if 'yes' in prevent : 
                   print("PREVENTION")
                   print("============================================================")                    
                   print("\n\n Sleep under mosquito net \n Drain away stagnant water \n\n Thank you for talking to mi "+name+" \n\nHAVE A GOOD DAY")
               else:
                    print("\n Thank you !! Have a good day")

           else:
               print("\n\nYour "+str(age) +" below 18 years ,\n i recommend you to go at "+ location + "health centre IV  for more medical attention" )
               
       else:
            print("\n\nThank you for talking to Dr. Matia")

   elif 'headache' in symptom and 'stomachache' in symptom and 'diahorrea' in signs and 'low' in appetite:
        print(name +" , You have Typhoid")

        # copied
        typhoidpre = input("Do you need medicine recommendation ? ")

        if 'yes' in typhoidpre:

           if age >18 :
               print("\n\n"+name + " your " + str(age) + "years above 18 , take :\n 3x2 Panadol extra \n 3X1 Amoxyl \n 1x2 Seputrine\n   ")
               print("If condition persist , Visit "+ location +" health centre IV for blood check up")
               prevent_typ = input("Do you need ways of preventing Tyhoid ?\n")

               if 'yes' in prevent_typ : 
                   print("PREVENTION")
                   print("============================================================")                    
                   print("\n\n Ensure that you use dry utensil \n Take boiled water or milk\n  \n\n Thank you for talking to mi "+name+" \n\nHAVE A GOOD DAY")
               else:
                    print("\n Thank you !! Have a good day")

           else:
               print("\n\nYour "+str(age) +" below 18 years ,\n i recommend you to go at "+ location + "health centre IV  for more medical attention" )
               
        else:
            print("\n\nThank you for talking to Dr. Matia")
        # end copied


   elif 'stomachache'in symptom and 'high' in temp and 'constipation' in symptom and 'heart burn' in symptom:
        print(name + "  you have Ulcers")

        # copy
        precautions = input("Do you need medicine recommendation ? ")

        if 'yes' in precautions:

           if age >18 :
               print("\n\n"+name + " your " + str(age) + "years above 18 , take :\n 3x1 amoxyl \n 1x4 magnesium \n 1x1 lasoprazo\n\n ")
               print("If condition persist , Visit "+ location +" health centre IV for blood check up")
               prevent = input("Do you need ways of preventing Ulcers?\n")

               if 'yes' in prevent : 
                   print("PREVENTION")
                   print("============================================================")                  
                   print("\n\n Eat food in time \n Avoid eating oily things  \n\n Thank you for talking to mi "+name+" \n\nHAVE A GOOD DAY")
               else:
                    print("\n Thank you !! Have a good day")

           else:
               print("\n\nYour "+str(age) +" below 18 years ,\n i recommend you to go at "+ location + "health centre IV  for more medical attention" )
               
        else:
            print("\n\nThank you for talking to Dr. Matia")
        #end of copy

   elif 'joint pain' in signs and ( 'bad' in sense or 'fair' in sense ) and ('runnig nose' in signs or 'cough' in signs):
        print(name+" , you have covid 20")
        # copy
        precautions = input("Do you need medicine recommendation ? ")

        if 'yes' in precautions:

           if age >18 :
               print("\n\n"+name + " your " + str(age) + "years above 18 , take :\n 1x3 Vitamin C \n 1x2 Panadol  \n\n ")
               print("If condition persist , Visit "+ location +" health centre IV for blood check up")
               prevent = input("Do you need ways of preventing Covid 20 ?\n")

               if 'yes' in prevent :                   
                   print("\n\n Use sanitaize regularly \n Avoid touching your mouth , nose , eyes \n Put on a mask always \n Keep atleast 2metre distance from anyone \n\n Thank you for talking to mi "+name+" \n\nHAVE A GOOD DAY")
               else:
                    print("\n Thank you !! Have a good day")

           else:
               print("\n\nYour "+str(age) +" below 18 years ,\n i recommend you to go at "+ location + "health centre IV  for more medical attention" )
               
        else:
            print("\n\nThank you for talking to Dr. Matia")
        # copied

   else:
        print("YOU HAVE NO SERIOUS DIEASES")

    
else:
           decide = input("Do you want to exit ? \n")
           if 'yes' in decide:
               print("Goodbye please !!!!!")
           else:
              print("Run this program again in the terminal . Thank you")

          