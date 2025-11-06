from random import randint, choice
from ..game import Game

class Player:
    
    static_profession = ["fighter","cure"]
    
    def __init__(self, name):
        self.name = name
        self.hp = 50  # חיים התחלתיים – .50 אם המקצוע הוא ”מרפא“ – +10 חיים נוספים. אם יורד מתחת ל0 - השחקן מת
        self.speed = randint(5,10) # מהירות, משפיע על מי תוקף ראשון
        self.power = randint(5,10) #  עוצמה, משפיע על הנזק בקרב. ערך אקראי בין 5–.10 אם המקצוע הוא ”לוחם“ – 2+ לעוצמה
        self.armor_rating = randint(5,15)
        self.profession = choice(Player.static_profession)
        
    def speak(self):
        print(f"Hello, it's me: {self.name}")
        
    def attack(self):
        dice = randint(1,6)
        Player.speed += dice
        if Player.speed > Game.choose_random_monster.speed or player.speed == Game.choose_random_monster.speed:
            cube = randint(1,20)
            Player.speed += cube
            if Player.speed > Game.choose_random_monster.armor_rating:
                dice2 = randint(1,6)
                Game.choose_random_monster.power += dice2
                Game.choose_random_monster.hp -= Game.choose_random_monster.power
                if Game.choose_random_monster.hp <= 0:
                    exit
            else:
                player , Game.choose_random_monster = Game.choose_random_monster ,player
            
        else:
            Game.choose_random_monster.attack()