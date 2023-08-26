ф="""
ЗАДАНИЕ 1 (Обязательно) 
на выбор два класса
1.	Создать класс кошелек с атрибутами в виде:
    a.	баланс 
    b.	магический метод на выбор:
        i.	увелечение баланса на n
        ii.	Сравнение двух кошельков
        iii.	проверку баланса на ноль
        iv.	предложить ваш метод
2.	Создать класс треугольник, с атрибутами в виде сторон(3 стороны обязательно) и магический метод на выбор:
    a.	 увеличение треугольник в n раз
    b.	 сравнение двух треугольников
    c.	 уменьшение треугольника на n 
    d.	предложить ваш метод
"""
class Wallets:
    def __init__(self, balance: int=0):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    def __add__(self, other):
        return Wallets(self.__balance + other)
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if self.__balance < other:
            raise 'для совершения операции на балансе не достаточно средств'
        elif self.__balance >= other:
            return Wallets(self.__balance - other)
        
    def __rsub__(self, other):
        return self - other

wallet = Wallets()
print(wallet.balance)

wallet = 52900 + wallet # Вызовет метод __radd__()
print(wallet.balance)

wallet = wallet - 30900
print(wallet.balance)

wallet = 900 - wallet # Вызовет метод __rsub__()
print(wallet.balance)

wallet = wallet - 23000 # Выдаст ошибку. raise 'для совершения операции на балансе не достаточно средств'
print(wallet.balance)
