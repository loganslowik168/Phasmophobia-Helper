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
    for ghostName, ghostEvidence in Ghosts.items():
        if ev in ghostEvidence:
            print(f"{ghostName} is a target!")
