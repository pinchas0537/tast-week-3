from random import randint, choice

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