import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0

# 1 - Listen : Hindi or English

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=10)

    try:
        print("Recoginsing...")
        query = r.recognize_google(audio, language='en-us''en-in''hi')
        print(f"You said: {query}")

    except:
        return

    query = str(query).lower()
    return query

# 2 - Translation

def Translation(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    # print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = Translation(query)
    return data