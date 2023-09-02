a=""" 
# --------------------------------------------------------------------------------------- #
ЗАДАНИЕ                                                                                   #
Описать пример(в словесной или (и) в форме кода)  применения Абстрактного класса          #
                                                                                          #
Описать пример (в словесной или (и) в форме кода) Множественного наследования             #
# --------------------------------------------------------------------------------------- #
"""

# --------------------------------------------------------------------------------------- # 
# Множественного наследование это возможность у класса потомка наследовать                #
# функционал не от одного, а от нескольких родителей. Благодаря этому мы можем создавать  #
# сложные структуры, сохраняя простой и легко-поддерживаемый код.                         #
# --------------------------------------------------------------------------------------- #
#                                                                                         #
# Например, у нас есть класс автомобиля:                                                  #
# --------------------------------------------------------------------------------------- #
class Auto:
    def ride(self):
        print("Ездит по земле")

# Так же у нас есть класс для лодки:                                                      #
# --------------------------------------------------------------------------------------- #
class Boat:
    def swim(self):
        print("Ходит по воде")


# Теперь, если нам нужно запрограммировать автомобиль-амфибию, который будет плавать в    #
# воде и ездить по земле, мы вместо написания нового класса, можем просто унаследовать    #
# от уже существующих:                                                                    #
# --------------------------------------------------------------------------------------- #
class Amphibian(Auto, Boat):
    pass

a = Amphibian()
a.ride()
a.swim()
