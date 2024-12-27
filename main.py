# Lib imports
import math
import tkinter as tk
import tkinter.ttk as ttk

# Class imports
import setup as SetupFunctions
from evidence import Evidence
from ghosts import Ghosts

root = tk.Tk()
root.title('Phasmophobia Helper')

EvidenceFrame = tk.Frame(root)
GhostsFrame = tk.Frame(root)

'''
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
''' 


EvidenceButtons = SetupFunctions.CreateEvidenceButtons(EvidenceFrame=EvidenceFrame)
GhostButtons = SetupFunctions.CreateGhostsButtons(GhostsFrame=GhostsFrame)


EvidenceFrame.grid(row=0,column=0)
ttk.Separator(root,orient='horizontal').grid(row=1, columnspan=3,sticky='ew')
GhostsFrame.grid(row=2,column=0)

root.mainloop()