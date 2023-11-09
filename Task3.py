class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        self.products[product.name] = {'type': product.type, 'price': product.price * 1.3, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_name, info in self.products.items():
            if info[identifier_type] == identifier:
                self.products[product_name]['price'] *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name in self.products and self.products[product_name]['amount'] >= amount:
            self.products[product_name]['amount'] -= amount
            return self.products[product_name]['price'] * amount
        else:
            raise ValueError("Product not available or insufficient quantity")

    def get_income(self):
        return sum(info['price'] * info['amount'] for info in self.products.values())

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError("Product not found")
        
