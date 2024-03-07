
class Missions:
    # private attributes
    __id_mission = ""
    __name = ""
    __detail = ""
    __level = ""
    __reward_exp = 0
    __reward_money = 0
    __status = ""
    
    #  constructor
    def __init__(self, id_mission = "", name = "", detail = "", level = "", reward_exp = 0, reward_money = 0, status = ""):
        self.__id_mission = id_mission
        self.__name = name
        self.__detail = detail
        self.__level = level
        self.__reward_exp = reward_exp
        self.__reward_money = reward_money
        self.__status = status
    
    #  setter dan getter
    def set_id_mission(self, id_mission): self.__id_mission = id_mission
    def set_name(self, name): self.__name = name
    def set_detail(self, detail): self.__detail = detail
    def set_level(self, level): self.__level = level
    def set_reward_exp(self, reward_exp): self.__reward_exp = reward_exp
    def set_reward_money(self, reward_money): self.__reward_money = reward_money
    def set_status(self, status, mark):
        if mark == 1:
            self.__status = "Completed"
        else:
            self.__status = status
    
    def get_id_mission(self): return self.__id_mission
    def get_name(self): return self.__name
    def get_detail(self): return self.__detail
    def get_level(self): return self.__level
    def get_reward_exp(self): return self.__reward_exp
    def get_reward_money(self): return self.__reward_money
    def get_status(self): return self.__status
    
    # methods
    def display_missions(self, mark):
        if mark == 1:
            if self.get_status().lower() == "not yet":
                print("MISSION ID ->", self.get_id_mission())
                print("Level       :", self.get_level())
                print("Name        :", self.get_name())
                print("Detail      :", self.get_detail())
                print("Reward      :  $", self.get_reward_money())
                print("Reward EXP  :", self.get_reward_exp())
                print("\n", end='')
    def display_reward(self):
        print("\n+--------------------------------------------------+")
        print("|                 Mission Completed!               |")
        print("+--------------------------------------------------+")
        print("  - Reward Coin + $", self.get_reward_money())
        print("  - Reward EXP  +", self.get_reward_exp())
        print("+--------------------------------------------------+")
        print("  Your Wallet :")
