ф = """
ЗАДАНИЕ 1 (Обязательно) 
работа творческая, опишите в свободной форме идеи и зависимости вашего проекта
пример можно посмотреть здесь https://github.com/makarova1507ana/python323/tree/......... 
самое задание
Создать сервис по просмотру сериала
Для данного задания понадобится класс 
Сериал(название, год выхода, список актеров, режиссер, жанр, сезоны) 
(для сезона рекомендуется создать свой класс c атрибутами название кол-серий, список серий)
можете выбрать любые 2 функциональности из списка ниже
●	реализовать общий список сериалов
●	реализовать возможность добавлять список любимых сериалов
●	реализовать возможность добавлять список любимых сезонов
●	реализовать возможность добавлять список любимых серий
●	Необходимо реализовать поиск по номеру серии, названию сезонов, названию сериалов 
"""


from Serials import *
from Season import *
from serials_box import *

favorite_serials = []
favorite_season = []
favorite_series = []

while True: 
    btn()
    team = input('введите команду - ')
    if team == 'q': # Выход из программы
        break

    if team == 'a': # общий список сериалов
        for serial in serials:
            print(serials.index(serial)+1,*serial.show())
        
        while True:
            team = int(input('выберите номер сериала или 0 для выхода в главное меню - '))
            if team == 0:
                break
            if team in btn2(s):
                print('Сериал',*serials[team-1].show(), f'Содержит {len(s[team-1])} сезонов')
                i = int(input('выберите сезон - '))
                if i in btn2(s[team-1]):
                    a = Season(i,s[team-1][i-1])
                    a.show_series()
                    n = int(input('выберите серию - '))
                    if n in btn2(s[team-1][i-1]):
                        print(s[team-1][i-1][n-1].show())
                        favorite = input('добавить серию в избранное \'y\'- да \'n\'- Нет  ')
                        if favorite == 'y': # добавлять список любимых серий
                            favorite_series.append(s[team-1][i-1][n-1])
                    favorite = input('добавить сезон в избранное \'y\'- да \'n\'- Нет  ')
                    if favorite == 'y': # добавлять список любимых сезонов
                        favorite_season.append(s[team-1][i-1])

                else:
                    print('Не корректный ввод команд') 
            else:
                    print('Не корректный ввод команд') 

    if team == 'b': # поиск по номеру сезонов
        team = int(input('введите номер сезона '))
        for i1 in btn2(s):
            for i2 in btn2(s[i1-1]):
                if i2 == team:
                    print(btn2(s[i1-1][i2-1].show()))
    
    if team == 'c': # поиск по номеру серии
        team = int(input('введите номер серии '))
        for i1 in btn2(s):
            for i2 in btn2(s[i1-1]):
                for i3 in btn2(s[i1-1][i2-1]):
                    if i3 == team:
                        print(s[i1-1][i2-1][i3-1].name)

    if team == 'f': # показать избранное
        l = 0
        print('# ------ Любимые серии ------ #')
        for i in favorite_series:
            print(i.show())
        print('# ------ Любимые сезон ------ #')
        for ser in favorite_season:
            l+=1
            if l != 1:
                print('# ------------------------ #')
            for i in ser:
                print(i.show())

    else:
        print('Не корректный ввод команд')     

    

