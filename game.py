from core import orc , goblin
from random import randint,choice

class Game:
    static_monster = [orc.Orc , goblin.Goblin]
    def start():
       show = Game.show_menu()
       print(show)
            
    def show_menu():
        input_ch = input("Select a battle = b or exit = e request")
        if input_ch == "b":
            Game.start()
        else:
            exit
        return input_ch
       
    def create_player():
        pass
    
    
    def choose_random_monster():
        monster = choice(Game.static_monster)
        return monster
    
    
    def battle(self,player,monster):
        pass
    
    
    def roll_dice(self, sides):
        pass
