#Defi1
mot=input("Enter a word :")
dit_index = { } 
for indes,letter in enumerate(mot):
    if letter in dit_index:
        dit_index[letter].append(indes)
    else:
        dit_index[letter]=[indes]
print(dit_index)
#Defi2
intems_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet= "$10"
argent=int(wallet.replace("$",""))
basket = []
for articles,prise_str in intems_purchase.items():
   prise_articles = int(prise_str.replace("$","").replace(",",""))
   if prise_articles <= argent:
    basket.append(articles)
    argent = argent-prise_articles
if len(basket)==0:
   print("Nothing")
else:
  print(sorted(basket)) 
  #Defi2
  keys=("Ten", "Twenty", "Thirty")
  values =(10, 20, 30)
dict1 = dict(zip(keys,values))
print(dict1)

        


    





 

