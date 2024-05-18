import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')

def parle(text):
    engine.say(text)
    engine.runAndWait()

def ecoute():
    try:
        with sr.Microphone() as source:
            print('parle...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice , language='fr-FR')
            #command = command.lower()
            #if 'assistant' in command:
                #command = command.replace('assistant', '')
                #print(command)
    except:
        pass
    return command

def assistant():
    command = ecoute()
    print(command)  #mettre ses commandes ici
    if 'heure' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        parle('Il est ' + time)
    elif 'recherche' in command:
        recherche = command.replace('recherche', '')
        pywhatkit.search(recherche)

    elif 'bonjour' in command:
        parle('Bonjour, comment ça va ?')
    elif 'ca va et toi ?' in command:
        parle('Je vais bien, merci de demander.')
        
    else:
        parle('Je ne comprends pas, répète s\'il te plaît.')


while True:
    assistant()