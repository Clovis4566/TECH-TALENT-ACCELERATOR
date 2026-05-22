#Defi
class cat:
  def __init__(self,cat_name,cat_age):
      self.cat_name=cat_name
      self.cat_age=cat_age
cat1=cat("Milo",5)
cat2=cat("gagou",12)
cat3=cat("Dev",2)
def  find_oldest_cat(c1,c2,c3):
  if c1.cat_age >= c2.cat_age and c1.cat_age >= c3.cat_age :  
   return c1
  elif c2.cat_age >= c1.cat_age and c2.cat_age >= c3.cat_age:
    return c2
  else:   return c3
oldest_cat=find_oldest_cat(cat1,cat2,cat3)
print("The oldest cat is {} and is {} years old.".format(oldest_cat.cat_name,oldest_cat.cat_age))
# defi2
class dog:
   def __init__(self,dog_name,dog_height):
        self.dog_name=dog_name
        self.dog_height=dog_height  
        
   def bark(self):
        print(f"{self.dog_name} fait ouaf !")
        return "Woof!"
   def jump(self):
       print(f"{self.dog_name} jumps {self.dog_height*2} cm high!")
dog1=dog("Hol",5)
dog2= dog("lili",4)
print(f" lE chien ")
dog1.bark()
dog1.jump()
print(f" lE chien ")
dog2.bark()
dog2.jump()
if dog1.dog_height > dog2.dog_height:
    print(f"{dog1.dog_name} is bigger than {dog2.dog_name}")
# defi3
class song:
    def __init__(self,lyrics) :  
        self.lyrics=lyrics
    def sing_me_a_song(self):
       for line in self.lyrics:
          print (line)
stairway = song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
  # defi4
class zoo:
   def __init__ (self,zoo_name):
       self.zoo_name=zoo_name
       self.animals=[]
   def add_animal(self,new_animal):
       if new_animal not in self.animals:
          self.animals.append(new_animal)
   def get_animals(self):
    print(self.animals)
   def sell_animal(self,animal_sold):
     if animal_sold in self.animals:
        self.animals.remove(animal_sold)
   def sort_animals(self):
    self.animals.sort()
    sorted_animals={}
    for animal in self.animals:
        first_letter=animal[0]
        if first_letter not in sorted_animals:
            sorted_animals[first_letter]=[animal]
        else:
            sorted_animals[first_letter].append(animal)
    return sorted_animals
         
   def get_groups(self): 
        groups = self.sort_animals()
        for letter, animals in groups.items():
           print(f"{letter}: {', '.join(animals)}") 
           
my_beatyful_zoo = zoo("My Beautiful Zoo")
my_beatyful_zoo.add_animal("Lion")
my_beatyful_zoo.add_animal("Tiger")
my_beatyful_zoo.add_animal("Bear")
my_beatyful_zoo.get_groups()

    