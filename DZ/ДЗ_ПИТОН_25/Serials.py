class Serials:

    def __init__(self, name, date,):
        self.__name =  name
        self.__date = date
        
    
    @property
    def name(self):
        return self.__name
    
    @property
    def date(self):
        return self.__date
    
    def show(self):
        return self.__name, self.__date
    

    

