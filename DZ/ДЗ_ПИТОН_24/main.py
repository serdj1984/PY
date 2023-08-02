###########################################################################################################################
#### 1. Написать код для https://github.com/makarova1507ana/python323/tree/main/.........                              ####
#### 1.1. Запрещено менять:                                                                                            ####
#### 1.1.1. list_products , атрибуты класса (должны остаться закрытыми )                                               ####
#### 1.2. необходимо реализовать возможность подсчета стоимости товаров в корзине                                      ####
###########################################################################################################################

from Product import *
from Shop import *
from ShopCart import *


shop = Shop('SHOP_2_0',Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000))
shop.show()

shop_cart = ShopCart()
while True:
        #номер товара определяет пользователь
        user_choice = input('would you like the product of number ... ')# дописать условия добавления и т.д. выход из системы
        if user_choice == '0':
            break
        #добавит блок проверки перед добавлением в корзину попапку 
        product = shop.products[int(user_choice)-1]
        
        shop_cart.append_product(product)
        
shop_cart.show()
print(shop_cart.cost_products)

sum(5,5)
