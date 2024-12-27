# Lib imports
import math
import tkinter as tk

# Class imports
from evidence import Evidence
from ghosts import Ghosts

def CreateEvidenceButtons(EvidenceFrame):
    # Evidence buttons
    EvidenceButtons = {}
    gridIndex = 0
    NUM_COLUMNS = 2
    for e in Evidence:
        b_key = e.value
        b_value = tk.Button(EvidenceFrame, text=e.value)
        EvidenceButtons[b_key]=b_value
        
        row = math.floor(gridIndex / NUM_COLUMNS)
        col = gridIndex % NUM_COLUMNS
        b_value.grid(row=row,column=col)
        gridIndex += 1
    return EvidenceButtons

def CreateGhostsButtons(GhostsFrame):
    # Ghost buttons
    GhostButtons = {}
    gridIndex = 0
    NUM_COLUMNS = 3
    for g in Ghosts:
        b_key = g.name
        b_value = tk.Button(GhostsFrame, text=g.name)
        GhostButtons[b_key]=b_value
        
        row = math.floor(gridIndex / NUM_COLUMNS)
        col = gridIndex % NUM_COLUMNS
        b_value.grid(row=row,column=col)
        gridIndex += 1
    return GhostButtons

