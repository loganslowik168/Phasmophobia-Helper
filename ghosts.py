# Lib imports
from enum import Enum
# Class imports
from evidence import Evidence as e

class Ghosts(Enum):
    Banshee = [e.DOTS,e.Orbs,e.UV]
    Demon = [e.Writing,e.UV,e.Freezing]
    Deogen = [e.DOTS,e.Writing,e.Box]
    Goryo = [e.DOTS,e.EMF,e.UV]
    Hantu = [e.Orbs,e.UV,e.Freezing]
    Jinn = [e.EMF,e.UV,e.Freezing]
    Mare = [e.Writing,e.Orbs,e.Box]
    Moroi = [e.Writing,e.Freezing,e.Box]
    Myling = [e.Writing,e.EMF,e.UV]
    Obake = [e.EMF,e.Orbs,e.UV]
    Oni = [e.DOTS,e.EMF,e.Freezing]
    Onryo = [e.Orbs, e.Freezing,e.Box]
    Phantom = [e.DOTS,e.UV,e.Box]
    Poltergeist = [e.Writing,e.UV,e.Box]
    Raiju = [e.DOTS,e.EMF,e.Orbs]
    Revenant = [e.Writing,e.Orbs,e.Freezing]
    Shade = [e.Writing,e.EMF,e.Freezing]
    Spirit = [e.Writing,e.EMF,e.Box]
    Thaye = [e.DOTS,e.Writing,e.Orbs]
    Mimic = [e.UV,e.Freezing,e.Box]
    Twins = [e.EMF,e.Freezing,e.Box]
    Wraith = [e.DOTS,e.EMF,e.Box]
    Yokai = [e.DOTS,e.Orbs,e.Box]
    Yurei = [e.DOTS,e.Orbs,e.Freezing]