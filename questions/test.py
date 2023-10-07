import time
import os

def test():
    frames = []

    frames.append("""
     O
    /|\\
    / \\
    """)

    frames.append("""
     O
    /|/
    / \\
    """)

    os.system('cls' if os.name == 'nt' else 'clear')

    for _ in range(5):
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            print("Have a good day!")
            time.sleep(0.5)

test()
