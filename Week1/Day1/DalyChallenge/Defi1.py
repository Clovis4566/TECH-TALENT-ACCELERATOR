Number=int(input("Enter a number: "))
length=int(input("enter the length:"))
liste_resultats = []
for i in range(1,length+1):
    liste_resultats.append(i * Number)
print(liste_resultats)