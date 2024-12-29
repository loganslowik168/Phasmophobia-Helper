# Lib imports
import tkinter as tk
from colors import ButtonColors as bc
from logic import ReevaluatePossibleGhosts

def ChangeEvidenceState(newState, button, evidence):
    if newState == 'affirm':
        color = bc.AFFIRM_COLOR.value
        colorHovering = bc.AFFIRM_COLOR_HOVER.value
    elif newState == 'reject':
        color = bc.REJECT_COLOR.value
        colorHovering = bc.REJECT_COLOR_HOVER.value
    elif newState == 'suspect':
        color = bc.SUSPECT_COLOR.value
        colorHovering = bc.SUSPECT_COLOR_HOVER.value
    else:
        raise NotImplementedError("The requested button state is currently not implemented.")
    button.config(bg=color, activebackground=colorHovering)
    ReevaluatePossibleGhosts(ev=evidence)