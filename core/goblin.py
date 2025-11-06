from random import randint , choice

class Goblin:
    
    static_weapon = ["knife","sword","ax"]

    def __init__(self ,name):
        self.name = name
        self.hp = 20
        self.tape = "goblin"
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = 1
        self.weapon = choice(Goblin.static_weapon)
    
    def speak(self):
        print(f"the {self.tape} {self.name} is angry")
        
    def attack(self,player):
        dice = randint(1,6)
        goblin.speed += dice
        if goblin.speed > player.speed or goblin.speed == player.speed:
            cube = randint(1,20)
            goblin.speed += cube
            if goblin.speed > player.armor_rating:
                dice2 = randint(1,6)
                if goblin.weapon == "knife":
                    result = dice2 * 0.5
                elif goblin.weapon == "sword":
                    result = dice2
                elif goblin.weapon == "ax":
                    result = dice2 * 1.5
                player.power += result
                player.hp -= player.power
                if player.hp <= 0:
                    exit
            else:
                goblin , player = player ,goblin
        else:
            player.attack()