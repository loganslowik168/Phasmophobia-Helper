# Lib imports
import math
import tkinter as tk
import tkinter.ttk as ttk

# Class imports
import setup as SetupFunctions
import buttonFunctions as ButtonFunctions
import logic as LogicFunctions
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

# Create buttons
EvidenceButtons = SetupFunctions.CreateEvidenceButtons(EvidenceFrame=EvidenceFrame)
GhostButtons = SetupFunctions.CreateGhostsButtons(GhostsFrame=GhostsFrame)

# Bind buttons-
for _,button in EvidenceButtons.items():
    button.bind("<Button-1>", lambda event, btn=button: ButtonFunctions.ChangeState('affirm', btn))
    button.bind("<Button-2>", lambda event, btn=button: ButtonFunctions.ChangeState('suspect', btn))
    button.bind("<Button-3>", lambda event, btn=button: ButtonFunctions.ChangeState('reject', btn))

LogicFunctions.UpdateAllData(GhostButtons=GhostButtons,GhostDeterminations=None)


# Draw buttons
EvidenceFrame.grid(row=0,column=0)
ttk.Separator(root,orient='horizontal').grid(row=1, columnspan=3,sticky='ew')
GhostsFrame.grid(row=2,column=0)

root.mainloop()