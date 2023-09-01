import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk, Image

class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.engine = pyttsx3.init()
        self.listener = sr.Recognizer()

        self.root.configure(bg="#fff")

        self.centre = ImageTk.PhotoImage(file="Images/Mic.png")
        centre_label = Label(self.root, image=self.centre)
        centre_label.place(x=220, y=50, height=400, width=100)

        start_button = Button(self.root, text='Start', font=('Poppins', 14), command=self.run_command)
        start_button.place(x=150, y=520)

        close_button = Button(self.root, text='Close', font=('Poppins', 14), command=self.close_window)
        close_button.place(x=350, y=520)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def start(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            wish = "Good Morning!"
        elif 12 <= hour < 18:
            wish = "Good Afternoon!"
        else:
            wish = "Good Evening!"
        self.speak("Hello Sir, " + wish + " I am your Voice Assistant. Tell me how may I help you.")

    def take_command(self):
        try:
            with sr.Microphone() as data_taker:
                print('Say something')
                voice = self.listener.listen(data_taker)
                instruction = self.listener.recognize_google(voice)
                instruction = instruction.lower()
                return instruction
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass

    def run_command(self):
        self.start()

        instruction = self.take_command()
        if instruction is not None:
            print(instruction)

            if 'who are you' in instruction:
                self.speak('I am your Personal Voice Assistant')

            elif 'what can you do for me' in instruction:
                self.speak('I can play songs, tell time, and help you go with Wikipedia')

            elif 'current time' in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                self.speak('Current time is ' + time)

            elif 'open google' in instruction:
                self.speak('Opening Google')
                webbrowser.open('https://www.google.com')

            elif 'open youtube' in instruction:
                self.speak('Opening YouTube')
                webbrowser.open('https://www.youtube.com')

            elif 'open gmail' in instruction:
                self.speak('opening gmail')
                webbrowser.open('https://www.gmail.com')

            elif 'open github' in instruction:
                self.speak('opening github')
                webbrowser.open('https://www.github.com')

            elif 'open instagram' in instruction:
                self.speak('opening instagram')
                webbrowser.open('https://www.instagram.com')

            elif 'show me the weather' in instruction:
                self.speak('sure, opening weather web app')
                webbrowser.open('https://bijaygurungweatherapp.000webhostapp.com/weather.html')

            elif 'shutdown' in instruction:
                self.speak('I am shutting down')
                self.close_window()

            else:
                self.speak('I did not understand, can you repeat again')

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = AssistanceGUI(root)
    root.mainloop()
