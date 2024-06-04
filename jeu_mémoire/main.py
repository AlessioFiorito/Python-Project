import random
import os
import time
 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def generate_number():
    n = str(random.randint(0,9))
    return n


def add_number(suit):
    suit = generate_number()
    global n_init
    n_init += suit
    print("Retenez la séquence")
    time.sleep(1)
    clear_screen()
    print(n_init)
    time.sleep(3)
    clear_screen()
    
clear_screen()
n_init = ""
for i in range(4): 
    n_init += generate_number()
print("Retenez la séquence")
time.sleep(1)
clear_screen()
print(n_init)
time.sleep(3)
clear_screen()

user_response = str(input("Quel était la suite de chiffres ? : "))

game_over = False
score = 0

while game_over == False:
    if user_response == n_init:
        score += 1
        print(f"Bonne réponse !\nVotre score est : {score}")
        time.sleep(1)
        clear_screen()
        add_number(n_init)
        user_response = input("Quel était la suite de chiffres ? : ")
    elif user_response != n_init:
        print("GAME OVER")
        print(f"La bonne réponse était : {n_init}")
        print(f"Votre score : {score} points")
        game_over = True
        

quit()







