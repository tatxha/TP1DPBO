# Class Player merupan child dari Class Character dan Class Player memiliki item dari class item
from PlayableCharacter import PlayableCharacter
from Items import Items

class Player(PlayableCharacter):
    # private attributes
    __skill = ""
    __exp = 0
    __coin = 0
    __key = 0
    __items = []
    __missions = []
    
    
    # constructor
    def __init__(self, id = "", name = "", gender = '', hp = 0, atk = 0, skill = "", exp = 0, coin = 0, key = 0):
        super().__init__(id, name, gender, hp, atk)
        self.__skill = skill
        self.__exp = exp
        self.__coin = coin
        self.__key = key
        self.__items = []
        self.__missions = []
        
    # setter dan getter
    def set_skill(self, skill): self.__skill = skill
    def set_key(self, key): self.__key = key
    def set_coin(self, coin): self.__coin = coin
    def set_exp(self, exp): self.__exp = exp
    
    def get_skill(self): return self.__skill
    def get_key(self): return self.__key
    def get_missions(self): return self.__missions
    def get_items(self): return self.__items
    def get_coin(self): return self.__coin
    def get_exp(self): return self.__exp
    
    # methods
    def add_mission(self, mission):
        self.__missions.append(mission)
    def add_item(self, item  : Items):
        self.__items.append(item)
    def add_coin(self, reward): 
        self.__coin += reward
    def add_exp(self, reward): 
        self.__exp += reward
    def dislay_players(self):
        print("PLAYER ID -> ", self.get_id())
        print("Name       : " + self.get_name() + " (" + self.get_gender() + ')' )
        if self.get_hp() < 0:
            print("HP         : 0")
        else:
            print("HP         :", self.get_hp())
        print("Skill      :", self.get_skill())
        print("ATK        :", self.get_atk())
        print("Coin       : $", self.get_coin())
        print("EXP        :", self.get_exp())
        print("Key        :", self.get_key())
        print("---------------------------------------------")
    def sell_item(self, npc, selected_item):
        npc.buying_item(selected_item)
