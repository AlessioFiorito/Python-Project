import time
import random
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

clear_screen()
sequence_initiale = ""
for i in range(4):  
    sequence_initiale += str(random.randint(0,9))

print("Jeu de mémoire")
time.sleep(2)
clear_screen()
score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    clear_screen()
    print(sequence_initiale)
    time.sleep(3)
    clear_screen()

    user_seq = input("Votre réponse : ")

    if user_seq == sequence_initiale:
        score += 1
        clear_screen()
        print("Réponse correcte")
        print(f"Votre score est de {score}")
        time.sleep(1)
        clear_screen()
        sequence_initiale += str(random.randint(0,9))
    else:
        print("Mauvaise réponse")
        print(f"La réponse était : {sequence_initiale}")
        print(f"Votre score est : {score}")
        exit()