from core import orc , goblin
from random import randint,choice

class Game:
    static_monster = [orc.Orc , goblin.Goblin]

    def __init__(self):
        pass
    
    def start(self):
       self.show_menu(self)
       print(self.show_menu(self))
            
    def show_menu(self):
        input_ch = input("Select a battle = b or exit = e request")
        if input_ch == "b":
            self.create_player(self)
        else:
            exit
        return input_ch
       
    def create_player(self):
        pass
    
    
    def monster():
        monster = choice(Game.static_monster)
        return monster

    
    def battle(self,player,monster):
        
        pass
    
    
    def roll_dice(self, sides):
        pass