# Class BadNPC merupakan child dari Class PlayableCharacter
from PlayableCharacter import PlayableCharacter

class BadNPC(PlayableCharacter):
    # private attributes
    __level = ""
    __bonus_exp = 0
    __bonus_coin = 0
    __status = ""
    
    # constructor
    def __init__(self, id = "", name = "", gender = '', hp = 0, atk = 0, level = "", bonus_exp = 0, bonus_coin = 0, status = ""):
        super().__init__(id, name, gender, hp, atk)
        self.__level = level
        self.__bonus_exp = bonus_exp
        self.__bonus_coin = bonus_coin
        self.__status = status
    
    # setter and getter
    def set_level(self, level): self.__level = level
    def set_bonus_exp(self, bonus_exp): self.__bonus_exp = bonus_exp
    def set_bonus_coin(self, bonus_coin): self.__bonus_coin = bonus_coin
    def set_status(self, status, mark): 
        if mark == 1:
            self.__status = "Died"
        else:
            self.__status = status
    
    def get_level(self): return self.__level
    def get_bonus_exp(self): return self.__bonus_exp
    def get_bonus_coin(self): return self.__bonus_coin
    def get_status(self): return self.__status
    
    # methods
    def display_enemies(self, mark):
        if mark == 1:
            if self.get_status().lower() == "alive":
                print("ENEMY ID  ->", self.get_id())
                print("Name       : " + self.get_name() + " (" + self.get_gender() + ')' )
                print("HP         :", self.get_hp())
                print("ATK        :", self.get_atk())
                print("Level      :", self.get_level())
                print("Bonus EXP  : $", self.get_bonus_exp())
                print("Bonus Coin :", self.get_bonus_coin())
    def display_reward(self):
        print("\n+--------------------------------------------------+")
        print("|             Succeeded defeating enemy!           |")
        print("+--------------------------------------------------+")
        print("  - Bonus Coin + $", self.get_bonus_coin())
        print("  - Bonus EXP  +", self.get_bonus_exp())
        print("+--------------------------------------------------+")
        print("  Dompet Anda:")