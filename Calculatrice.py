def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    while b == 0:
        b = float(input("Impossible de diviser par 0 ! Autre dénominateur : "))
    return a / b

def main():
    print("Bienvenu sur la calculatrice basique 1.0")
    user_num1 = float(input("Choisissez le premier nombre : "))
    user_num2 = float(input("Choisissez le deuxième nombre : "))
    user_choice = input("Choisissez entre 1 (addition), 2 (soustraction), 3 (multiplication), 4 (division) : ")
    
    if user_choice == "1":
        resultat = addition(user_num1, user_num2)
    elif user_choice == "2":
        resultat = soustraction(user_num1, user_num2)
    elif user_choice == "3":
        resultat = multiplication(user_num1, user_num2)
    elif user_choice == "4":
        resultat = division(user_num1, user_num2)
    else:
        print("Choix invalide")
        return
    
    print(f"Le résultat est : {resultat}")

if __name__ == "__main__":
    main()


        
    
   

   

    
