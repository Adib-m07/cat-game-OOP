#our cat enitity
class Cat:
# the constructor:
# - The constructor will create a cat for us in code 
#- To create a cat , we need given_name and given_colour
#- self is the cat that we are creating
   def __init__ (self,given_name,given_colour):
       #Name attribute
    self.name = given_name
       #Colour attribute
    self.colour = given_colour
    self.age=1
    self.energy=50
    self. intelligence=5
    self.weight=5
   def train(self):
       print(f'{self.name} is training....' )
       self.energy -=5
       self.intelligence +=1
       self.age +=0.1

   def feed(self):
       print(f'{self.name} is eating....' )
       self.energy +=10
       self.intelligence +=1
       self.age +=0.
   def sleep(self):
       print(f'{self.name} is sleeping....' )
       self.energy +=100
       self.intelligence +=10
       self.age +=0.1
   def play(self):
       print(f'{self.name} is playing....' )
       self.energy -=20
       self.intelligence +=2
       self.age +=0.1
   def show_stats
       print(f'{self.age},{self.energy},{self.intelligence},{self.weight}')
