FileOpenAi = open('Data\\ApiKeys\\openai.txt','r')
apikey = FileOpenAi.read()
FileOpenAi.close()

import openai
import datetime
import time
from dotenv import load_dotenv

openai.api_key = apikey

hour = int(datetime.datetime.now().hour)
tt = time.strftime(f"%d/%m/%Y | %I:%M %p")

load_dotenv()
completion = openai.Completion()

chat_log_template = ''' 
Date : 16/11/2022 | 10:14 PM
You  :  Hello, who are you?  Jarvis : I am doing great. How can I help you today?
'''

def replyJarvis(question, chat_log=None):
    FileLog = open('Database\\chat_log.txt','r')
    FileLog = open('Data\\memory.txt','r')
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}You : {question}\nJarvis :'
    response = completion.create(
        engine="text-davinci-002", 
        prompt=prompt, 
        stop=['\nYou'], 
        temperature=0.5,
        top_p=1, 
        best_of=1,
        max_tokens=60,
        frequency_penalty=0.5, 
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'\nDate : {tt} \nYou : {question} \nJarvis : {answer}'
    FileLog = open('Database\\chat_log.txt','w')
    FileLog.write(chat_log_template_update)
    return answer


if __name__ == "__main__": #main program
    
    while True:
        k = input(" : ")
        print(ReplyByAI(k))