# Lib imports
import math
import tkinter as tk
import tkinter.ttk as ttk

# Class imports
import setup as SetupFunctions
import buttonFunctions as ButtonFunctions
import logic as LogicFunctions
from evidence import Evidence, Marks
from ghosts import Ghosts
from trackers import GhostData

# Tkinter stuff
root = tk.Tk()
root.title('Phasmophobia Helper')

EvidenceFrame = tk.Frame(root)
GhostsFrame = tk.Frame(root)

# Tracker stuff
ghostData = GhostData


# Create buttons
EvidenceButtons = SetupFunctions.CreateEvidenceButtons(EvidenceFrame=EvidenceFrame)
GhostButtons = SetupFunctions.CreateGhostsButtons(GhostsFrame=GhostsFrame)

# Bind buttons-
for evidence, button in EvidenceButtons.items():
    button.bind("<Button-1>", lambda event, btn=button, ev=evidence: ButtonFunctions.ChangeEvidenceState('affirm', btn, ev))
    button.bind("<Button-2>", lambda event, btn=button, ev=evidence: ButtonFunctions.ChangeEvidenceState('suspect', btn, ev))
    button.bind("<Button-3>", lambda event, btn=button, ev=evidence: ButtonFunctions.ChangeEvidenceState('reject', btn, ev))


# LogicFunctions.PrintGhostData(GhostButtons=GhostButtons,GhostDeterminations=None)


# Draw buttons
EvidenceFrame.grid(row=0,column=0)
ttk.Separator(root,orient='horizontal').grid(row=1, columnspan=3,sticky='ew')
GhostsFrame.grid(row=2,column=0)





# This hangs unfortunately
# cringe...
root.mainloop()

