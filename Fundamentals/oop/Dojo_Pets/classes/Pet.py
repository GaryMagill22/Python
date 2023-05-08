

# implement __init__( name , type , tricks ):
class Pet:
    def __init__(self, name, type, tricks, health, energy) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        print(f"{self.name} is sleeping, do not disturb. Increasing {self.energy} by 25.")
        self.energy += 25

    
    def eat(self):
        print(f"{self.name} is eating! Increasing {self.energy} by 5 and {self.health} by 10!")

    
    def play(self):
        print(f"{self.name} is playing! Increasing {self.health} by 5.")
    
    def noise(self):
        print("Woooof wooooooof!")


Pet1 = Pet('Frankie', 'Dog', 'fetch beer')
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound