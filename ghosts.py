# Lib imports
from enum import Enum
# Class imports
from evidence import Evidence as e

class Ghosts(Enum):
    
    Spirit = [e.Writing,e.EMF,e.Box]
    Wraith = [e.DOTS,e.EMF,e.Box]
    Phantom = [e.DOTS,e.UV,e.Box]
    Poltergeist = [e.Writing,e.UV,e.Box]
    Banshee = [e.DOTS,e.Orbs,e.UV]
    Jinn = [e.EMF,e.UV,e.Freezing]
    Mare = [e.Writing,e.Orbs,e.Box]
    Revenant = [e.Writing,e.Orbs,e.Freezing]
    Shade = [e.Writing,e.EMF,e.Freezing]
    Demon = [e.Writing,e.UV,e.Freezing]
    Yurei = [e.DOTS,e.Orbs,e.Freezing]
    Oni = [e.DOTS,e.EMF,e.Freezing]
    Yokai = [e.DOTS,e.Orbs,e.Box]
    Hantu = [e.Orbs,e.UV,e.Freezing]
    Goryo = [e.DOTS,e.EMF,e.UV]
    Myling = [e.Writing,e.EMF,e.UV]
    Onryo = [e.Orbs, e.Freezing,e.Box]
    Twins = [e.EMF,e.Freezing,e.Box]
    Raiju = [e.DOTS,e.EMF,e.Orbs]
    Obake = [e.EMF,e.Orbs,e.UV]


    # It's always bothered me how traditional tracking doesn't include ghost orbs in the evidence tracket.  It just creates more work.
    # It causes me to constantly have to check the 'Ghosts' tab in the journal to see which 3 evidence the Mimic possesses officially.
    # I will be marking Mimic as having all four evidence.  I generally find this to be more intuitive when marking it down in the journal.
    Mimic = [e.UV,e.Freezing,e.Box,e.Orbs]

    
    Moroi = [e.Writing,e.Freezing,e.Box]
    Deogen = [e.DOTS,e.Writing,e.Box]
    Thaye = [e.DOTS,e.Writing,e.Orbs]