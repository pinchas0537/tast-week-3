from random import randint, choice
 
class Orc:
    
    static_weapon = ["knife","sword","ax"]
    
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.tape = "orc"
        self.speed = randint(0,5)
        self.power = randint(10,15)
        self.armor_rating = randint(2,8)
        self.weapon = choice(Orc.static_weapon)
        
    def speak(self):
        print(f"the {self.tape} {self.name} is angry")
        
    def attack(self,player):
        dice = randint(1,6)
        orc.speed += dice
        if orc.speed > player.speed or Orc.speed == player.speed:
            cube = randint(1,20)
            orc.speed += cube
            if orc.speed > player.armor_rating:
                dice2 = randint(1,6)
                if orc.weapon == "knife":
                    result = dice2 * 0.5
                elif orc.weapon == "sword":
                    result = dice2
                elif orc.weapon == "ax":
                    result = dice2 * 1.5
                player.power += result
                player.hp -= player.power
                if player.hp <= 0:
                    exit
            else:
                orc , player = player ,orc
        else:
            player.attack()