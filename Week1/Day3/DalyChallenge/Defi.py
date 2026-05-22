class farm:
    
    def __init__(self, farm_name, animals_name):
        self.name = farm_name  
        self.animals = {} 

    
    def get_add_animals(self, anymal_type, count=1):
        if anymal_type in self.animals:
            self.animals[anymal_type] += count
        else:
            self.animals[anymal_type] = count

    
    def get_info(self):
        info_string = f"{self.name}'s farm\n\n"
        
        for animal, count in self.animals.items():
            info_string += f"{animal:<10} : {count}\n"
            

        info_string += "\n    EIEI-O!"
        
        return info_string      


my_farm = farm("My Farm", {})  
my_farm.get_add_animals("cow")
my_farm.get_add_animals("pig", 3)
my_farm.get_add_animals("horse", 2)


print(my_farm.get_info())