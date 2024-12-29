from enum import Enum

class Evidence(Enum):
    EMF = 'EMF Level 5'
    UV = 'Ultraviolet'
    Writing = 'Ghost Writing'
    Freezing = 'Freezing Temperatures'
    DOTS = 'D.O.T.S Projector'
    Orbs = 'Ghost Orb'
    Box = 'Spirit Box'

class Marks(Enum):
    POSITIVE = 1
    NEGATIVE = -1
    UNMARKED = 0
    SUSPICIOUS = 99