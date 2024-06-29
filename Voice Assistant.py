import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):

    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():

    with sr.Microphone() as source:

        print("Listening...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:

            print("Recognizing...")
            speak("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"Did you say: {query}")
            speak(f"Did you say: {query}")

        except sr.UnknownValueError:

            print("Sorry, Can you please repeat? I could'nt understand that.")
            speak("Sorry, Can you please repeat? I could not understand that.")

            return None
        
        except sr.RequestError:
            
            print("Sorry, I am currently down at the moment!.")
            speak("Sorry, I am currently down at the moment!.")
            
            return None
        
    return query.lower()

def handle_query(query):

    if 'hello' in query or 'hi' in query or 'hey' in query:
        speak("Hello! How can I help you?")
        speak("What are your plans for today?")

    elif 'how are you' in query or "how r you" in query or "how r" in query:
        speak("I am good, thankyou for asking!! How are you?")

    elif 'I am good' in query or 'I am fine' in query:
        speak("Glad to hear that!")
        speak("What are your plans for today?")

    elif 'time' in query:
        now = datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
        speak("What are your plans for today?")

    elif 'search' or 'look' or 'look for' or 'find' in query:
        query = query.replace("search", "").replace("look", "").replace("look for","").replace("find","")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Here are results for {query.strip()}, i hope that will help you out")

    else:
        speak("I'm sorry, I didn't understand that. Can you please elaborate?")

if __name__ == "__main__":

    print("Hello! I am Ammar Voice Assistant. How can I help you?")
    speak("Hello! I am Ammar Voice Assistant. How can I help you?")

    while True:

        query = listen()
        
        if query:
            handle_query(query)

            if "stop" in query or "end" in query or "finish" in query:
                speak("Goodbye! Have a nice day!!")
                
                break
