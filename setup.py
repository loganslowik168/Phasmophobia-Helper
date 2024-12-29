# Lib imports
import math
import tkinter as tk

# Class imports
from evidence import Evidence
from ghosts import Ghosts
from button import Button

def CreateEvidenceButtons(EvidenceFrame):
    # Evidence buttons
    EvidenceButtons = []
    gridIndex = 0
    NUM_COLUMNS = 2
    for e in Evidence:
        b = Button(e,EvidenceFrame)
        EvidenceButtons.append(b)
        
        row = math.floor(gridIndex / NUM_COLUMNS)
        col = gridIndex % NUM_COLUMNS
        b.button.grid(row=row,column=col)
        gridIndex += 1
    return EvidenceButtons

def CreateGhostsButtons(GhostsFrame):
    # Ghost buttons
    GhostButtons = []
    gridIndex = 0
    NUM_COLUMNS = 3
    for g in Ghosts:
        b = Button(g,GhostsFrame)
        GhostButtons.append(b)
        
        row = math.floor(gridIndex / NUM_COLUMNS)
        col = gridIndex % NUM_COLUMNS
        b.button.grid(row=row,column=col)
        gridIndex += 1
    return GhostButtons

