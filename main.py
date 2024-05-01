import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
import time

# Initialize the speech engine
engine = p.init()

# Adjust speech settings
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for voice input
def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjusted duration
        speak("How can I assist you?")
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        speak("I encountered an error while processing your request.")
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to perform actions based on user input
def process_input(input_text):
    if "thank you" in input_text:
        speak("You're welcome! Goodbye!")
        exit()  # Exit gracefully
    elif "how are you" in input_text:
        speak("I'm doing well, thank you for asking!")
    elif "information" in input_text:
        speak("Sure, what topic are you interested in?")
        topic = listen()
        if topic:
            speak("Let me find information about " + topic)
            info = infow()
            info.get_info(topic)
    elif "tell me a joke" in input_text:
        speak("Why don't scientists trust atoms? Because they make up everything!")
    elif "exit" in input_text or "quit" in input_text:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm not sure how to respond to that.")

# Main function to run the voice assistant
def main():
    speak("Hello! I'm your voice assistant.")
    last_activity_time = time.time()  # Initialize last activity time
    while True:
        input_text = listen()
        if input_text:
            process_input(input_text)
            last_activity_time = time.time()  # Update last activity time
        else:
            # Check if there has been no activity for 10 seconds
            if time.time() - last_activity_time > 10:
                speak("I'm going to sleep now. Goodbye!")
                break

if __name__ == "__main__":
    main()
