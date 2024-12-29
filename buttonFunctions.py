# Lib imports
import tkinter as tk
from colors import ButtonColors as bc
from logic import ReevaluatePossibleGhosts
from trackers import EvidenceData
from evidence import Marks

def ChangeEvidenceState(newState, button):
    newButtonState = None
    if newState == 'affirm':
        color = bc.AFFIRM_COLOR.value
        colorHovering = bc.AFFIRM_COLOR_HOVER.value
        newButtonState = Marks.POSITIVE
    elif newState == 'reject':
        color = bc.REJECT_COLOR.value
        colorHovering = bc.REJECT_COLOR_HOVER.value
        newButtonState = Marks.NEGATIVE
    elif newState == 'suspect':
        color = bc.SUSPECT_COLOR.value
        colorHovering = bc.SUSPECT_COLOR_HOVER.value
        newButtonState = Marks.SUSPICIOUS
    else:
        raise NotImplementedError("The requested button state is currently not implemented.")
    # check if newState same as old state
    if button.state == newButtonState:
        button.ResetState()
        return
    # otherwise
    button.state = newButtonState
    button.button.config(bg=color, activebackground=colorHovering)
    EvidenceData[button.text] = newButtonState
    ReevaluatePossibleGhosts(button.text)