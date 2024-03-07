# Class Character
class Character():
    # private attributes
    __id = ""
    __name = ""
    __gender = ''
    
    # constructor
    def __init__(self, id = "", name = "", gender = ''):
        self.__id = id
        self.__name = name
        self.__gender = gender
    
    # setter dan getter
    def set_id(self, id): self.__id = id
    def set_name(self, name): self.__name = name
    def set_gender(self, gender): self.__gender = gender
    def get_id(self): return self.__id 
    def get_name(self): return self.__name 
    def get_gender(self): return self.__gender 
    