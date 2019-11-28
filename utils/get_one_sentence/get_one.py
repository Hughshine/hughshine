# import os
import random
with open('./sentences.txt', 'r') as f:
    lines = f.readlines()
    print(lines[random.randint(0, len(lines)-1)].replace("\n", ""))
    