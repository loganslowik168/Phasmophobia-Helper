# Class imports
from evidence import Evidence, Marks
from ghosts import Ghosts
from trackers import EvidenceData

def PrintGhostData(GhostButtons,GhostDeterminations):
    for evidence in Evidence:
        for ghost,_ in GhostButtons.items():
            if evidence in Ghosts[ghost].value:
                print(f"Ghost {ghost} has evidence {evidence}")
        print(" ")

def ReevaluatePossibleGhosts(evidenceButtons, ghostButtons):
    for button in evidenceButtons:
        targetEvidenceState = button.state
        