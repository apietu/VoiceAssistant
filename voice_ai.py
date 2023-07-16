import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import json
listener =sr.Recognizer()
engine = pyttsx3.init()


def greeting_message():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir !")

    else:
        engine.say("Good Evening Sir !")
    engine.say('I am your virtual assistant')
    engine.say('How can I assist you')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def accept_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if '' in command:
                command = command.replace('', '')
                print(command)

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None

    except sr.RequestError as e:
        print(f"Sorry, there was a problem with the speech recognition service: {e}")
        return None

    return command


def ask_more():
    engine.say('Is there anything else you need help with?')
    engine.runAndWait()
    command = accept_command()
    command = command.lower()
    if 'yes' in command:
        return True
    else:
        engine.say('Okay. Goodbye.')
        engine.runAndWait()
        return False

def process_command(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt('playing ' + song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + time)
        print('The time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'how are you' in command:
        talk('I am doing great')
        print('I am doing great')

    else:
        talk('I did not get that. Can you repeat what you said.')


def run_ai():
    greeting_message()
    while True:
        command = accept_command()
        if command:
            process_command(command)
            if not ask_more():
                break
        else:
            talk('Sorry, I could not understand what you said. Can you repeat that?')
run_ai()