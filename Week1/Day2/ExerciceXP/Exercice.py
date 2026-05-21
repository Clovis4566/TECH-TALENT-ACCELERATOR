#Defi2
keys=("Ten", "Twenty", "Thirty")
values =(10, 20, 30)
dict1 = dict(zip(keys,values))
print(dict1)
#Defi2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total=0
for name,age in family.items():
    if age < 3:
        prise =0
    elif 3 <= age <= 12:
        prise =10
    else :
        prise =15  

    print (f"{name} has to pay {prise} dollars")      
    
    total=total+prise    

print(f"the total cost for the family is {total} dollars")

#Defi2
brand={"name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]}   
}
brand["number_stores"]=2
print("les elements de type of clothes sont:",brand["type_of_clothes"])
brand["country_creation"]="Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand ["creation_date"]
print("le dernier element de internationnal competitors est ",brand["international_competitors"][-1])    
print (" les prinicaple couleurs sont:",brand["major_color"]["US"])
nomber_store=len(brand)
print("le nombre de key dans le dictionnaire est:",nomber_store)
more_on_Zara = {"creation_date":1975,'number_stores':7000}
brand.update(more_on_Zara)
print(brand)
#Defi2
def describe_city(city,country="unknown"):
     print(f"{city} is in {country}")
     describe_city("paris","france")
     describe_city("london","england") 
     describe_city("Abidjan")   
    #Defi2
import random
def random_nombre_choisie(nombre_dave):
     nombre_aleatoire=random.randint(1, 100)
     if nombre_aleatoire==nombre_dave:
        print("you are win")
     else: print("you are lose")
     print("the random number is",nombre_aleatoire,"and the nombre you choose is",nombre_dave)
random_nombre_choisie(50)
#Defi2
def make_shirt(size, message):
 print(f"the size of the shirt is {size} and the message is {message}")
make_shirt ("X","dave")
def make_shirt_defauts(size="l",text="i love python"):
 print(f"the size of the shirt is {size} and the message is {text}")
make_shirt_defauts()
def make_shirt (size="large",text="i love python"):
 print(f"the size of the shirt is {size} and the message is {text}")
make_shirt()
make_shirt(size="medium")
make_shirt(text="s",size="small")
make_shirt(size="small",text="x-large")
#Defi2
import random
def get_random_temp():
    return random.randint(-10, 40)
def main():
        get_random_temp()
        temp=get_random_temp()
        print(f"the temperature today is {temp} degree celsius")
        if  temp < 0:
         print("Brrr, it's freezing! Wear some extra layers today")
        elif temp in range(0,17):
         print("Quite chilly! Don't forget your coat")
        elif temp in range (17,25):
            print("The weather is nice today! Wear something light")
        elif  temp in range(25,33):
            print("It's getting hot! Make sure to stay hydrated")
        elif temp in range (33,41):
            print("It's scorching! Stay indoors if possible")

main()
import random


def get_random_temp():
    mois_str = input("Entrez le numéro du mois actuel (1-12) : ")
    mois = int(mois_str)

    # 1. On détermine la saison
    if mois in [12, 1, 2]:
        saison = "hiver"
    elif mois in [3, 4, 5]:
        saison = "printemps"
    elif mois in [6, 7, 8]:
        saison = "été"
    elif mois in [9, 10, 11]:
        saison = "automne"
    else:
        print("Mois invalide ! Par défaut, on choisit l'été.")
        saison = "été"
    if saison == "hiver":
        return random.uniform(-10.0, 5.0)
    elif saison == "printemps":
        return random.uniform(6.0, 18.0)
    elif saison == "été":
        return random.uniform(24.0, 40.0)
    elif saison == "automne":
        return random.uniform(5.0, 16.0)



temp = get_random_temp()

print(f"La température aujourd'hui est de {temp:.1f} degrés Celsius.")
# defi2
while True :
    user_inpt=input("entrer l'ingredient de votre pizza ou taper stop pour arreter: ")
    if user_inpt.lower() == "quit":
        for i in range (1,6):
          print(f"adding {user_inpt} to your pizza")
        break  
print("votre pizza est de 5 dollars chaque ingredient coute 1 dollar")    

    