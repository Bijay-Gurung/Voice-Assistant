# Importing Modules
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk, Image

# Create Display Window
class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="Images/background.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="Images/Mic.png")
        centre_label = Label(self.root, image=self.centre)
        centre_label.place(x=100, y=100, height=400, width=100)

        # Start Button
        start_button = Button(self.root, text='Start', font=('Poppins', 14), command=self.start_option)
        start_button.place(x=150, y=520)

        # Close Button
        close_button = Button(self.root, text='Close', font=('Poppins', 14), command=self.close_window)
        close_button.place(x=350, y=520)

    def start_option(self):
        pass  

    def close_window(self):
        self.root.destroy()

# Main Program
if __name__ == "__main__":
    root = Tk()
    app = AssistanceGUI(root)
    root.mainloop()
