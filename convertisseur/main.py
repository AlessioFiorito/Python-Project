
def conversion(unit1, unit2, operator):
    print(f"Conversion {unit1} vers {unit2}")
    value_str = input(f"Combien de {unit1} à convertir (ou pressez q pour quitter): ")
    if value_str == "q":
        return True
    try:
        value_float= float(value_str)
    except ValueError:
        print("ERREUR: vous devez rentrer une valeur numérique ! ")
        print("(Utilisez le . et non la , pour les décimales)")
        return conversion(unit1, unit2, operator)
    answer = round(value_float*operator, 2)
    print(f"{value_str} {unit1} donne : {answer} {unit2}")
    return False

print("Convertisseur d'unité Inch et CM")
print()



    
while True:
    choice = input("(1)Inch->CM (2)CM->Inch. Tappez 1 ou 2 : ")
    if choice == "1":
        if conversion("Inch","CM",2.54):
            break
    elif choice == "2":
        if conversion("CM","Inch",0.394):
            break
