# Создать класс студент
# атрибуты:
# имя
# группа
# средний балл


class Student:
    def __init__(self, name:str='', group:str='', gpa:int=0, id__:int = 0):
        self.__id__ = id__# id
        self.__name = name
        self.__group = group
        self.__gpa = gpa# 100
    
    def show(self):
        print(self.__name,
        self.__group,
        self.__gpa,end=' | ')
    # тот же самый геттер, только лучше
    @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #геттер READ-ONLY
    def getgroup(self):
        return self.__group
    
    @property
    def getgpa(self):
        return self.__gpa
    
    
    # для данной задачи не нужна
    def setGroup(self, group):
        if type(group) == type('str'):
            self.__group = group
        else:
            print( "atribute must be string" )
    # #геттер
    # def getGroup(self):
    #     return self.__group
   
    #       # def group(self):
    #        #      return self.__group
    
    
    
    
    #   #    # @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #    # #геттер READ-ONLY
    #    # def getGroup(self):
    #    #     return self.__group

    #     def name(self):
    #     return self.__name
