class Student:

    def __init__(self, name:str='', group:str='', gpa:int=0, id:int=100):
        self.__name = name
        self.__group = group
        self.__gpa = gpa # 100
        self.__id = id 
        
    def show(self):
         print(f'{self.__name}: группа - {self.__group}, средний балл - {self.__gpa}, id студента - {self.__id}', end=' | ')

    # тот же самый геттер, только лучше
    @property # @property -декоратор (для методов и функций даете новые вомзонжости)
    #геттер READ-ONLY
    def getgroup(self):
        return self.__group
    
    @property
    def getgpa(self):
        return self.__gpa
#====================================================================================#
# ---------  ГЕТЕР ДЛЯ id  --------------------------------------------------------- #
#                                                                                    #
    @property                                                                        #                                                  
    def getid(self):                                                                 #
        return self.__id                                                             #
# ---------------------------------------------------------------------------------- #
#====================================================================================#
    # для данной задачи не нужна
    def setGroup(self, group):
        if type(group) == type('str'):
            self.__group = group
        else:
            print( "atribute must be string" )
