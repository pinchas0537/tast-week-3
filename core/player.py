from random import randint, choice

class Player:
    
    static_profession = ["fighter","cure"]
    
    def __init__(self, name):
        self.name = name
        self.hp = 50  
        self.speed = randint(5,10) 
        self.power = randint(5,10) 
        self.armor_rating = randint(5,15)
        self.profession = choice(Player.static_profession)
        
    def speak(self):
        print(f"Hello, it's me: {self.name}")
            
    def attack(self,monster):
        if self.speed > monster.speed or player.speed == monster.speed:
            cube = randint(1,20)
            self.speed += cube
            if self.speed > monster.armor_rating:
                dice2 = randint(1,6)
                monster.power += dice2
                monster.hp -= monster.power
                if monster.hp <= 0:
                    exit
            else:
                player , monster = monster ,player
            
        else:
            monster.attack()