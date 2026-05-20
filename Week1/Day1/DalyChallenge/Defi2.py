Chaine_originale =input("enter a string: ")
Chaine_netoyee =""
for letter in Chaine_originale:
    if len(Chaine_netoyee) == 0 or letter != Chaine_netoyee[-1]:
        Chaine_netoyee += letter
print("Chaine_netoyee:", Chaine_netoyee)