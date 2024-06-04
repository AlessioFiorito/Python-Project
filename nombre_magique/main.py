import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIES = 4
vie = NOMBRE_VIES

def demander_nombre(nb_min,nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})")
        try:
            nombre_int = int(nombre_str)
        except ValueError:
            print("Ce n'est pas un nombre !")
        else:
            if nombre_int < 1 or nombre_int > 10:
                print("Le nombre doit être compris entre 1 et 10 !")
                nombre_int = 0
        return nombre_int
        
nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)

while not nombre == NOMBRE_MAGIQUE and vie > 0:
    print(f"Il vous reste {vie} vies")
    nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo c'est le nombre magique !")
    elif nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand")
        vie -= 1
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vie -= 1

if vie == 0:
    print(f"Vous avez perdu ! Le nombre magique était {NOMBRE_MAGIQUE}")

nombre = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)



