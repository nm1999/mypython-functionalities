from nltk.chat.util import Chat , reflections
import webbrowser

pairs = [
         ['hello|hi|good mng|hey',['hey','good mng too u','hello','hi']],
         ['how are you ?',['Am ok','Am very happy','Am alright','Am so good']],
         ['yes|yap|fine|ok|okay|that is good',['Alright','Okay','Seriously','Really']],
         ['My name is (.*)',['Hello %1  , how can i help you']],
         ['Am (.*)', ['Do you often feel %1']],
         ['what is the weather in (.*)',['In %1 , its raining','In %1 , its cloudy','In %1 , its sunny','In %1 , its windy']],
         ['who programmed you ?|who made you?',['matia mathias','JCM technologies','Nyanzi Matia']],
         ['i want (.*)',['%1 !!!!!!!!']],
         ['i like food|where can i get food',['Which online shop/website do you know ?']],
         ['jumia|yammie|amazon',['That`s right','Your right','let mi connect you there']],
         ['where is (.*) located',['%1 is in the far east','%1 , is located in the North of Kampala','%1 is in the south west of lake victoria','%1 is in the north west of Shara desert','%1 is in the south west of the city']],
         ['help|i need help|i need assistance',['what is the problem?','How can i help you?','Which type of help?','What has gone wrong?']],
         ['(.*)',['tell mi more','Try writing a phase','Be sepecific in your response','elaborate more','check your spelling']],
         ['goodbye|exit|quit',['Thank you for talking to mi','Have a nice time','Goodbye , hope we meet again','I wish you well','Goodbye Stay Safe']]
        ]        
chat = Chat(pairs,reflections)
chat.converse()
