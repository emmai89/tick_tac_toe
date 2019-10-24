import random
import os
from Backend import begin

scores = [0, 0, 0]
while True :
    option = input("""\n\nWhat do you want to do?
    1. Play
    2. quit\n >>>> """)

    if option == "1":
        begin(scores)
        print("x = ", scores[0], " o = ", scores[1])
    else:
        print("bye")
        break
