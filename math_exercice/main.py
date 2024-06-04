import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4

def poser_question():
    a = random.randint(NB_MIN,NB_MAX)
    b = random.randint(NB_MIN,NB_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 1:
        operateur_str = "-"
    elif o == 2:
        operateur_str = "*"
    elif o == 3:
        operateur_str = "/"
    
    reponse_str = input(f"Quel est la réponse à cette question ? : {a} {operateur_str} {b} ? : ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a-b
    elif o == 2:
        calcul = a*b
    elif o == 3:
        calcul = a/b
    
    if reponse_int == calcul:
        return True
        
    
    return False
        
    
nb_points = 0


for i in range(0,NB_QUESTIONS):
    print(f"Question {i+1} sur 4")
    if poser_question():
        print("Bravo bonne réponse !")
        nb_points += 1
    else:
        print("Mauvaise réponse !")

    print()
    
print(f"{nb_points} points sur 4")
moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points >= moyenne:
    print("Pas mal" )
elif nb_points < moyenne:
    print("Peut mieux faire")
