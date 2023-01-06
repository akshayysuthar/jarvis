import sys
from Body.Listen import Listen, MicExecution
from Body.Speak import Speak
from Brain.Think import ThinkJarvis
from Brain.Reply import replyJarvis
# from Main import MainTasksExecution

def MainExecution():
    Speak("Hello Sir !")
    while True:
        # Data = input(" Enter : ")
        Data = MicExecution()
        Data = str(Data).replace(".", "")


        # ValueReturn = MainTasksExecution(Data)
        
        # if ValueReturn==True:
        #     pass

        if len(Data)<2:
            pass 

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Speak(ThinkJarvis(Data)) 

        elif "exit" in Data:
            sys.exit()

        else:
            Reply = replyJarvis(Data)
            Speak(Reply)



MainExecution()
