import os
import time


def clear_screen():  # -> Funcion realizada por el profe Juan.
    # Para Windows
    if os.name == "nt":
        os.system('cls')
    # Para Linux
    else:
        os.system('clear')

def pause_screen(second):
    time.sleep(second)