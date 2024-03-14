import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

print('Loading Walmart Siri lol')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except sr.UnknownValueError:
            speak("I didn't hear you, please say that again")
            return "none"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "none"
        return statement.lower()


speak("Loading Walmart Siri")
wishMe()

if __name__ == '__main__':
    while True:
        speak("What can I do for you?")
        statement = takeCommand()
        if statement == "none":
            continue

        if "goodbye" in statement or "ok bye" in statement or "turn off" in statement:
            speak('see you later!')
            break

        elif 'open' in statement:
            a = statement.split()
            b = a.index('open')
            website = ' '.join(a[b+1:])
            webbrowser.open_new_tab(website)
            time.sleep(5)
