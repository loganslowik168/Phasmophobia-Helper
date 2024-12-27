# Lib imports
import tkinter as tk


def ButtonStateChange(newState, button):
    if newState == 'affirm':
        color = 'green'
        colorHovering = '#66b266'
    elif newState == 'reject':
        color = 'red'
        colorHovering = '#ff6666'
    elif newState == 'suspect':
        color = 'yellow'
        colorHovering = '#ffff66'
    else:
        raise NotImplementedError("The requested button state is currently not implemented.")
    button.config(bg=color, activebackground=colorHovering)