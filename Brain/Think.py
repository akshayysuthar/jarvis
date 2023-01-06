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

def ThinkJarvis(question,chat_log = None):
    FileLog = open('Database\\QnA_log.txt','r')
    FileLog = open('Data\\memory.txt','r')
    chat_log_template = FileLog.read()
    FileLog.close()
    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question : {question}\nAnswer :'
    response = completion.create(
        engine="text-davinci-002", 
        prompt=prompt,  
        temperature=0,
        max_tokens=150,
        top_p=0.5, 
        frequency_penalty=0.5, 
        presence_penalty=0)
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'\nDate : {tt} \nQuestion : {question} \nAnswer : {answer}'
    FileLog = open('Database\\QnA_log.txt','w')
    FileLog.write(chat_log_template_update)
    return answer

if __name__ == "__main__": #main program
    
    while True:
        Data = input("Enter : ")

        if "What is" in Data or "Where is" in Data or "question" in Data or "answer" in Data:
            print(ThinkJarvis(Data))

