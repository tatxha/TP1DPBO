#  Class Good NPC merupakan child dari Class Character juga, Class ini memiliki informasi mengenai data Player, data misi, dan item yang dibeli dari Player
from Character import Character 
from Player import Player
from Missions import Missions 
from Items import Items 

class GoodNPC(Character):
    # private attributes
    __missions = []
    __items = []
    
    # constructor
    def __init__(self, name= "", gender = '', id = ""):
        super().__init__(name, gender, id)
        self.__items = []
        self.__missions = []
    
    # getter
    def get_items(self): return self.__items
    def get_mission(self): return self.__missions
    
    # methods
    def add_mission(self, mission : Missions):  # Metode untuk menambahkan misi
        self.__missions.append(mission)             
    def assign_mission_to_player(self, player, selected_mission):
        player.add_mission(selected_mission)
    def display_player_information(self, player : Player):
        print("+------------------------------------------------+")
        print("| ID         :", player.get_id())
        print("| Name       :", player.get_name() + " (" + player.get_gender() + ')' )
        print("| HP         :", player.get_hp())
        print("| Skill      :", player.get_skill())
        print("| ATK        :", player.get_atk())
        print("| Coin       : $", player.get_coin())
        print("| Key        :", player.get_key())
        print("+------------------------------------------------+")
    def buying_item(self, bought):
        self.__items_bought.append(bought)