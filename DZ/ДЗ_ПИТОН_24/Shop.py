from Product import Product

# добавление товара в магазин
class Shop:
    def __init__(self, name:str = '', *products:Product):
        if not(type(name) == str): raise 'name is not str'
        if not(type(products) in [Product, tuple]): raise 'products is not Product or tuple'
        
        self.__name = name
        self.__products = []
        for product in products:
            self.__products.append(product)
            
# общий список товаров   
    def show(self):
        print(self.__name,' : ')
        for product in self.__products:
            product.show()
    
    # def get_product(self, i):
    #     return self.__products[i]
    
    @property
    def products(self):
        return self.__products
    
    def append_product(self, *products:Product):
        if not(type(products) in [Product, tuple]): raise 'products is not Product or tuple'
        for product in products:
            self.__products.append(product)

# удаление товара из магазина
    def del_product(self, product:Product):
        if not(type(product) == Product): raise 'products is not Product '
        self.__products.remove(product)

shop = Shop('SHOP_2_0',Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000))
shop.show()
#Shop() # == __new__()
