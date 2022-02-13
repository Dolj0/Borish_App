import os
from typing import final
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import tkinter as tk
import pygame
import time
from tkinter import messagebox
import pyttsx3
import threading

## GUI class
class Graphics:
    
    # GUI constructor
    def __init__(self, main_windows):
        self.mainWindow = main_windows
        self.screenwidth = main_windows.winfo_screenwidth()
        self.screenheight = main_windows.winfo_screenheight()
        self.IMAGEFILE = 'BorisPicture.png'
        self.width = 900
        self.height = 625
        self.x = (self.screenwidth - self.width)/2
        self.y = ((self.screenheight - self.height)/2)
        self.mainWindow.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, (self.y-35)))
        self.mainWindow.title("Borish")
        self.mainWindow.resizable(0, 0)
        self.place_image()
        self.mainWindow.protocol("WM_DELETE_WINDOW", self.place_image())
        self.Title = tk.Label(self.mainWindow, text="Borish", font=("arial bold", 40), bg="white")
        self.Title.place(x=380, y=5)
        self.place_button()

    # Sets the background of the GUI
    def place_image(self):
        self.backCanvas = tk.Canvas(self.mainWindow, background="white")
        self.backCanvas.place(x=0, y=0, width=self.width, height=625)
        self.imgLogo = tk.PhotoImage(file=self.IMAGEFILE)
        self.background = self.backCanvas.create_image(450, 350, image=self.imgLogo)

    #This adds a button to the tkinter window (Finish, Next, Submit?)
    def place_button(self):
        self.entry = tk.Entry(self.mainWindow, width=55)
        self.entry.insert(tk.INSERT, 'E.g Mr Speaker, Coronavirus, Peppa Pig')
        self.entry.place(x=300, y=503)
        self.myButton = tk.Button(self.mainWindow, text="Generate Borish", command=self.display_speech, width=15)
        self.myButton.place(x=600, y=500)
        
    # This displays the generated speech within the text bubble
    def display_speech(self):

        try:
            self.displayText.destroy()
        finally:

            self.my_text = self.entry.get()
            self.my_text = self.get_text(self.my_text)
            local_text = self.my_text
            my_text_array = self.my_text.split(" ")
            self.my_text = " "
            for i in range(len(my_text_array)):
                self.my_text += my_text_array[i]
                if (i % 5) == 4:
                    self.my_text += "\n"
                else:
                    self.my_text += " "
            
            self.my_text += "\n\n Did this sound like Boris Y/N?"

            self.displayText = tk.Label(self.mainWindow, text=self.my_text, font=("arial bold", 10), bg="white")
            self.displayText.place(x=110, y=150)
            points = [520, 250, 450, 220, 450, 120, 100, 120, 100, 350, 450, 350, 450, 270]
            self.backCanvas.create_polygon(points, outline='black', fill='white', width=2)

            #So after the text box is filled with text, the button becomes "next"
            self.entry = tk.Entry(self.mainWindow, width=55)
            self.entry.place(x=300, y=503)
            self.myButton = tk.Button(self.mainWindow, text="Submit", command=self.check_quality, width=15)
            self.myButton.place(x=600, y=500)

            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.save_to_file(local_text, 'speech.mp3')
            engine.runAndWait()

            pygame.mixer.init()
            out = pygame.mixer.Sound("speech.mp3")
            pygame.mixer.Sound.play(out)
               

    # This expects the next entry to be "yes", "y" or "no", "n"
    def check_quality(self):
        try:
            self.displayText.destroy()
        finally:
            is_correct = self.entry.get().casefold()
            pygame.mixer.init()
            # If good, then play yay.mp3
            if is_correct in ["yes", "y"]:
                # Display congrats
            
                # Sound Congrats
                yay = pygame.mixer.Sound("Yay.mp3")
                pygame.mixer.Sound.play(yay)
                time.sleep(4)

                # Empty Text Box
                self.my_text += "\n\n Yay we did it!\n\n Try another sentence!"
                self.displayText = tk.Label(self.mainWindow, text=self.my_text, font=("arial bold", 10), bg="white")
                self.displayText.place(x=110, y=150)
                points = [520, 250, 450, 220, 450, 120, 100, 120, 100, 350, 450, 350, 450, 270]
                self.backCanvas.create_polygon(points, outline='black', fill='white', width=2)
                
                self.myButton = tk.Button(self.mainWindow, text="Generate Borish", command=self.display_speech, width=15)
                self.myButton.place(x=600, y=500)

            # If bad, then play forgive_me_clip
            elif is_correct in ["no", "n"]:
                forgive_me = pygame.mixer.Sound("Forgive_me_clip.mp3")
                pygame.mixer.Sound.play(forgive_me)
                time.sleep(3)

                # Empty Text Box
                self.my_text += "\n\n Forgive me!\n\n Try another sentence!"
                self.displayText = tk.Label(self.mainWindow, text=self.my_text, font=("arial bold", 10), bg="white")
                self.displayText.place(x=110, y=150)
                points = [520, 250, 450, 220, 450, 120, 100, 120, 100, 350, 450, 350, 450, 270]
                self.backCanvas.create_polygon(points, outline='black', fill='white', width=2)
                
                self.myButton = tk.Button(self.mainWindow, text="Generate Borish", command=self.display_speech, width=15)
                self.myButton.place(x=600, y=500)

            # If input invalid, play Answer_the_bloody_question
            else:
                answer_the_bloody_question = pygame.mixer.Sound("Answer_the_bloody_question.mp3")
                pygame.mixer.Sound(answer_the_bloody_question)
                pygame.mixer.Sound.play(answer_the_bloody_question)
                time.sleep(3)

                # Empty Text Box
                self.my_text += "\n\n Why are you avoiding the question prime minister?\n\n Try another sentence!"
                self.displayText = tk.Label(self.mainWindow, text=self.my_text, font=("arial bold", 10), bg="white")
                self.displayText.place(x=110, y=150)
                points = [520, 250, 450, 220, 450, 120, 100, 120, 100, 350, 450, 350, 450, 270]
                self.backCanvas.create_polygon(points, outline='black', fill='white', width=2)
                
                self.myButton = tk.Button(self.mainWindow, text="Generate Borish", command=self.display_speech, width=15)
                self.myButton.place(x=600, y=500)
            

    #Get Text
    def get_text(self, input):
        two_step = tf.saved_model.load('two_step')
        states = None 
        next_char = tf.constant([input])
        result = [next_char]
        for n in range(100):
            next_char, states = two_step.generate_one_step(next_char, states=states)
            result.append(next_char)
            if next_char == "." or next_char == "\n":
                break
        output = tf.strings.join(result)[0].numpy().decode("utf-8")

        return output

    def gtts(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(self.my_text)
        engine.runAndWait()



mainWindow = tk.Tk()
display = Graphics(mainWindow)
mainWindow.mainloop()
