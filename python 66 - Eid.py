import pyfiglet
from termcolor import colored
import random

def eid():
    colors=['red','gree','yellow','blue','magenta','cyan','white']
    ascii_art=pyfiglet.figlet_format("Eid Mubarak",font="slant")
    print(colored(ascii_art, color=random.choice(colors)))


eid()
