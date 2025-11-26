
import random

answer = ''
while answer != 'n':
    x = random.randint(1, 9)
    n = -1
    while x != n:
        try:
            pref = "Wrong." if  n >= 0 else ""   
            n = input(f"{pref}Please input number (1 - 9): ")
            n = int(n)
        except:
            n = 0
    print("You win!!!")
    answer = ''
    while answer not in ('y', 'n'):
        try:
            answer = input("Another game? (y/n): ")
        except:
            answer = '' 

print("Game over")


