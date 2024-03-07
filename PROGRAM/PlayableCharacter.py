# Class PlayableCharacter merupakan child dari Class Character
from Character import Character

class PlayableCharacter(Character):
    # private attributes
    __hp = 0
    __atk = 0
    __ulti_atk = 0
    
    #  constructor
    def __init__(self, id = "", name="", gender='', hp = 0, atk = 0, ulti_atk = 0):
        super().__init__(id, name, gender)
        self.__hp = hp
        self.__atk = atk
        self.__ulti_atk = ulti_atk
    
    # setter dan getter
    def set_hp(self, hp): self.__hp = hp
    def set_atk(self, atk): self.__atk = atk
    def set_ulti_atk(self, mark):
        if mark == 1:
            self.__ulti_atk = (self.get_atk() // 2)
        else:
            self.__ulti_atk = (self.get_atk() // 4)
    
    def get_atk(self): return self.__atk
    def get_hp(self): return self.__hp
    def get_ulti_atk(self): return self.__ulti_atk
    
    # methods
    def attack_enemy(self, enemy, mark): # player attack enemy
        enemy_hp = enemy.get_hp()
        if mark == 1:
            enemy.set_hp(enemy_hp - (self.get_atk() + self.get_ulti_atk()))
        else:
            enemy.set_hp(enemy_hp - self.get_atk())
    def attack_player(self, player, mark): # bad npc attack player
        player_hp = player.get_hp()
        if mark == 1:
            player.set_hp(player_hp - (self.get_atk() + self.get_ulti_atk()))
        else:
            player.set_hp(player_hp - self.get_atk())
    def heals(self, player):
        player.__hp = 100
    