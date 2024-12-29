# Class imports
from evidence import Evidence
from ghosts import Ghosts
def PrintGhostData(GhostButtons,GhostDeterminations):
    for evidence in Evidence:
        for ghost,_ in GhostButtons.items():
            if evidence in Ghosts[ghost].value:
                print(f"Ghost {ghost} has evidence {evidence}")
        print(" ")

def ReevaluatePossibleGhosts(ev):
    for ghost in Ghosts:
        print(f"{ev}")
        print(f"if {Evidence[ev].key} in {ghost.value}:")

