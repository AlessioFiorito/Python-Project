import time
import beepy

"""La fonction prend en paramètre un timer différent selon le choix de l'utilisateur
"""
def selected_timer(timer_selected):
    d = timer_selected
    min = d//60
    sec = d-min*60
    print(f"Temps restant : {min:02d}:{sec:02d} ")
    for i in range(d):
        d -= 10
        min = d//60
        sec = d-min*60
        if d == 0:
            print("CUISSON TERMINEE !")
            beepy.beep(sound="ping")
            quit()
        
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
       
        print()
        print(f"Temps restant : {min:02d}:{sec:02d}")
    

    
        

# Menu principal 

print()
print("***CUISSON DES OEUFS***")
print()
print("Sélectionnez le type de cuisson souhaitée")
print()
print("(1) Oeufs à la coque : 3 minutes")
print("(2) Oeufs mollets : 6 minutes")
print("(3) Oeufs durs : 9 minutes")
print()

# contrôle du choix utilisateur
while True:

    choice = input("Sélectionnez 1, 2 ou 3 : ")

    # gestion mauvais input
    if not choice == "1" or choice == "2" or choice == "3":
        print("Vous devez sélectionner entre 1, 2 ou 3 !")
    elif choice == "1":
        selected_timer(180)
    elif choice == "2":
        selected_timer(360)
    elif choice == "3":
        selected_timer(540)
    

    