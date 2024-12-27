# Class imports
from evidence import Evidence
from ghosts import Ghosts
def UpdateAllData(GhostButtons,GhostDeterminations):
    for evidence in Evidence:
        for ghost,_ in GhostButtons.items():
            if evidence in Ghosts[ghost].value:
                print(f"Ghost {ghost} has evidence {evidence}")
        print(" ")