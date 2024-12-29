# Lib imports
import tkinter as tk
# Class imports
from evidence import Marks
class Button:
    def __init__(self, text, frame):
        self.name = text
        self.text = text
        self.button = tk.Button(frame, text=text)
        self.state = Marks.UNMARKED
        self.ResetState()
        

    def ResetState(self):
        self.button.config(bg='white', activebackground='grey')
        self.state = Marks.UNMARKED