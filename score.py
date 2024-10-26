import os
from utils import SCORES_FILE_NAME

file = './' + SCORES_FILE_NAME

def ensure_scores_file():
    """Check if the scores file exists; if not, create it."""
    if not os.path.exists(file):
        with open(file, 'w') as f:
            f.write("POINTS_OF_WINNING = 0\n")


def add_score(difficulty):
    ensure_scores_file()
    points = (difficulty*3) + 5

    with open(file, 'r') as f:
        lines = f.readlines()

        # Update the score
    for i, line in enumerate(lines):
        if line.startswith("POINTS_OF_WINNING"):
            current_score = int(line.split('=')[1].strip())
            new_score = current_score + points
            lines[i] = f"POINTS_OF_WINNING = {new_score}\n"
            break

        # Write the updated score back to the file
    with open(file, 'w') as f:
        f.writelines(lines)


add_score(3)
