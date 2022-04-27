from colorama import Fore, Back, Style
import time

n1 = "./replays/replay0.txt"

f = open(n1,"r")

for line in f:
    if line[0] == 'S':
        time.sleep(0.5)
        print("\n")
    
    else:
        print(line)
    
    
f.close()