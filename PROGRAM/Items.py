# Class Items
class Items:
    # private attributes
    __id = ""
    __name = ""
    __price = 0
    __status = ""
    
    #  constructor
    def __init__(self, id = "", name = "", price = 0, status = ""):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__status = status

    # setter and getter
    def set_id(self, id): self.__id = id
    def set_name(self, name): self.__name = name
    def set_price(self, price): self.__price = price
    def set_status(self, status, mark): 
        if mark == 1: 
            self.__status = "Sold"
        else:
            self.__status = status
    
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_price(self): return self.__price
    def get_status(self): return self.__status
    
    # methods
    def display_item(self):
        if self.__status.lower() == "ready":
            print("ITEM ID ->", self.get_id())
            print("Name     :", self.get_name())
            print("Price    : $", self.get_price())