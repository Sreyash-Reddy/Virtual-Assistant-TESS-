import speech_recognition as sr
import pyttsx3
import p2

listener = sr.Recognizer()
tess = pyttsx3.init()
voices = tess.getProperty('voices')
tess.setProperty('voices' , voices[0].id)
tess.setProperty('rate' , 150)
tess.setProperty('volume' , 1000)

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source , phrase_time_limit=5)
        command = listener.recognize_google(voice)
        print(command)
        if ('activate' or 'Activate') in command:
            tess.say("Activating tess")
            tess.runAndWait()
            print("Activating Tess")
            p2.Activated()

except:
    pass

