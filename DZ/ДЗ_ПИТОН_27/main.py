"""
ЗАДАНИЕ 1 (Обязательно) 
представим себе игру стратегию. Напишите в комментариях логику, 
которую вы видете по взаимодействию с этими башнями.
Создать класс башня 
(есть броня и здоровье, а также регуляторы увеличения и уменьшения здоровья и брони). 
Создать класс стрелковая башня (умеет стрелять и все то, что и родитель)
"""
# -------------------------- Класс башня родитель ---------------------------------- #
class Towers:                                                                        #
    def __init__(self, heal: int=100, armor: int=100):                               #
        self.__h = heal
        self.__a = armor
        self.__heal = heal                                                           #
        self.__armor = armor                                                         #
        self.__heal_up = 30                                                          #
        self.__armor_up = 30                                                         #
                                                                                     #
    def domage(self, x):                                                             #
        self.__armor -= x                                                            #
        if self.__armor < 0:                                                         #
             self.__armor = 0                                                        #
        if self.__armor > 9: # пока броня больше 9 здоровья отнимается 2% от урона   #
            self.__heal -= x*0.2                                                     #
        elif self.__armor <= 1:                                                      #
            self.__heal -= x                                                         #
                                                                                     #
    @property                                                                        #
    def healing(self):                                                               #
        if self.__heal < self.__h:                                                   #
            self.__heal += self.__heal_up                                            #
            if self.__heal > self.__h:                                               #
                s = self.__heal - self.__h                                           #
                self.__heal -= s                                                     #
                                                                                     #
    @property                                                                        #
    def gain(self):                                                                  #
        if self.__armor < self.__a:                                                  #
            self.__armor += self.__armor_up                                          #
            if self.__armor > self.__a:                                              #
                c = self.__armor - self.__a                                          #
                self.__armor -= c                                                    #  
                                                                                     #
    def show(self):                                                                  #
        return 'Здоровье - ' + str(self.__heal) +'\nБроня - '+str(self.__armor)      #                    
# ---------------------------------------------------------------------------------- #

# --------------------------- Класс башня потомок ---------------------------------- #
class ShotTowers(Towers):                                                            #
    def __init__(self, shot: int=10):                                                #
        self.__shot = shot                                                           #
        super().__init__()                                                           #
                                                                                     #
    def show(self):                                                                  #
        return str(super().show()) + '\nУрон выстрела - ' + str(self.__shot)         #
                                                                                     #
    @property                                                                        #
    def shot(self):                                                                  #
        return self.__shot                                                           #
# ---------------------------------------------------------------------------------- #


t = Towers(200, 200) # создаем объект башня класса родителя
print(t.show()) # показываем характеристики

st = ShotTowers(30) # создаем объект башня класса потомка с умением стрелять
print(st.show()) # показываем характеристики

t.domage(st.shot) # Наносит урон 
print(t.show())

t.healing # повышение здоровья
t.gain # повышение защиты 
print('1  - ',t.show())
