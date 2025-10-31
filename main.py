import speech_recognition as sr  #its recognize the speech
import webbrowser      #its open the web browser
import pyttsx3         #its convert text to speech
import musicLibrary   #importing our music library

recognizer = sr.Recognizer()  #initializing the recognizer
engine = pyttsx3.init()       #initializing the text to speech engine       

def speak(text):
    engine.say(text)
    engine.runAndWait() 
 
def search_web(query):
    """Open web browser with search query for real-time information"""
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return f"I've opened a web search for {query}"    
    
def processCommand(command):
    print(f"Processing command: {command}")
    
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")   
    elif "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")  
    elif "open linkedin" in command.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link=musicLibrary.music[song] 
        webbrowser.open(link)
        speak(f"Playing {song}")   
        # Web search for real-time information
    elif "search" in command or "search for" in command or "khoj" in command:
        query = command.replace("search", "").replace("search for", "").replace("khoj", "").strip()
        if query:
            speak(f"Searching for {query}")
            search_web(query)
        else:
            speak("What would you like me to search for?")   
       # Exit commands
    elif any(word in command for word in ["exit", "quit", "goodbye", "bye", "band karo", "बंद करो", "stop", "निघून जा"]):
        speak("Goodbye! It was nice talking to you. Have a great day!")
        return False         
    else:
        # Let OpenAi Handle request  
        pass  

if __name__ == "__main__":
    speak("Hello Onkar, how can I assist you today?")
    while True:
        # Listen for wake word "Jarvis"
        # obtain audio from the microphone
        r=sr.Recognizer()
       
            
        print( "Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)  #It will listen for 2 seconds
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis"):
                speak("Yaa")
            word = word
            print(f"User said: {word}\n")
            
            
            # Listen for specific commands
            with sr.Microphone() as source:
                print("Jarvis Activate...")
                audio = r.listen(source)  
                command= r.recognize_google(audio)
                processCommand(command)#Function that process our command
                
        except Exception as e:
            print("Could not request results; {0}".format(e))        