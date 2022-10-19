import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import webbrowser
import pyautogui as pg
from datetime import datetime

now = datetime.now()
todo = []

listener = sr.Recognizer()
tess = pyttsx3.init()
voices = tess.getProperty('voices')
tess.setProperty('voices' , voices[1].id)
tess.setProperty('rate' , 200)
tess.setProperty('volume' , 1000)

def Activated():   
    tess.say("Hey Qwerty! , Tess is activated")
    tess.say("How can i help you?")
    tess.runAndWait()
    try:
        with sr.Microphone() as source:
            while True:   

                print('listening...')
                voice = listener.listen(source , phrase_time_limit=3)
                command = listener.recognize_google(voice)
                print(command)

                if 'time' in command: 
                    current_time = now.strftime("%H:%M")
                    print("Current Time =", current_time)
                    tess.say("The current time is "+ current_time)
                    tess.runAndWait()   
                if 'climate' in command:
                    import requests, json
                    # base URL
                    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                    # City Name CITY = "Hyderabad"
                    # API key API_KEY = "Your API Key"
                    # upadting the URL
                    CITY = "Trichy"
                    API_KEY = "2fd37a81cc8ec4b8d5ae96a8f7c6b4af" 
                    URL = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
                    # HTTP request
                    response = requests.get(URL)
                    # checking the status code of the request
                    if response.status_code == 200:
                        # getting data in the json format
                        data = response.json()
                        # getting the main dict block
                        main = data['main']
                        # getting temperature
                        temperature = main['temp']
                        # getting the humidity
                        humidity = main['humidity']
                        # getting the pressure
                        pressure = main['pressure']
                        # weather report
                        report = data['weather']
                        print(f"{CITY:-^30}")
                        print(f"Temperature: {temperature - 273}")
                        tess.say("Temparature at Trichy is: "+str(temperature - 273)+" Degree Celsius")
                        tess.runAndWait()
                        print(f"Humidity: {humidity}")
                        print(f"Pressure: {pressure}")
                        print(f"Weather Report: {report[0]['description']}")
                        tess.say("Weather Report of trichy is: "+str(report[0]['description']))
                        tess.runAndWait()
                    else:
                    # showing the error message
                        print("Error in the HTTP request")
                        tess.say("There is an error please try again")
                        tess.runAndWait()
                if "play" in command:
                    print("Which Song do you want me to play? ")
                    tess.say("Which Song do you want me to play? ")
                    tess.runAndWait()
                    voice = listener.listen(source , phrase_time_limit=3)
                    command1 = listener.recognize_google(voice)
                    print(command1)
                    # data = command.replace('play' , '')
                    tess.say("Playing "+command1)
                    tess.runAndWait()
                    pywhatkit.playonyt(command1)


                if "message" in command:
                    hours = now.strftime("%H")
                    minutes = now.strftime("%M")
                    print("To whom you want to send message to?")
                    tess.say("To whom you want to send message to? ")
                    tess.runAndWait()
                    print("listening...")
                    contact = listener.listen(source , phrase_time_limit=3)
                    command1 = listener.recognize_google(contact)
                    print(command1)
                    print("What message you want to send?")
                    tess.say("What message you want to send?")
                    tess.runAndWait()
                    print("listening...")
                    msg = listener.listen(source , phrase_time_limit=3)
                    command2 = listener.recognize_google(msg)
                    print(command2)
                    tess.say("Sending message to "+command1+" immediately")
                    tess.runAndWait()
                    if (command1 == "Manish"):
                        pywhatkit.sendwhatmsg_instantly("+919476085181", command2)
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")

                        pg.press("enter")
                        time.sleep(5)
                        pg.hotkey("alt","f4")
                        pg.press("enter")

                    elif(command1 == "Harish"):
                        pywhatkit.sendwhatmsg_instantly("+918900927929", command2)
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")
                        pg.press("tab")

                        pg.press("enter")
                        time.sleep(5)
                        pg.hotkey("alt","f4")
                        pg.press("enter")

                if "search" in command:
                    print("What you want to search for in google?")
                    tess.say("What you want to search for in google?")
                    tess.runAndWait()
                    print("listening...")
                    voice = listener.listen(source , phrase_time_limit=3)
                    data = listener.recognize_google(voice)
                    print(data)
                    webbrowser.open_new("https://www.google.com/search?q="+data)
                
                
            


    except:
        pass

Activated()
