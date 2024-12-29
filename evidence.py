from enum import Enum

Evidence = [
    'EMF Level 5',
    'Ultraviolet',
    'Ghost Writing',
    'Freezing Temperatures',
    'D.O.T.S Projector',
    'Ghost Orb',
    'Spirit Box'
]


class Marks(Enum):
    POSITIVE = 1
    NEGATIVE = -1
    UNMARKED = 0
    SUSPICIOUS = 99