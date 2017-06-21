class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
    def sell(self):
        self.status = 'sold'
        return self
    def addTax(self, tax):
        afterTax = self.price + (self.price * tax)
        return afterTax
    def Return(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        if reason == 'in box':
            self.status = 'for sale'
        if reason == 'box open':
            self.status = 'used'
            self.price = 0.8 * self.price
        return self
    def displayInfo(self):
        info = {}
        info['price'] = self.price
        info['name'] = self.name
        info['weight'] = self.weight
        info['brand'] = self.brand
        info['cost'] = self.cost
        info['status'] = self.status
        print info
        return self

if __name__ == '__main__':
    product1 = Product(25, 'undies', '2 kg', 'hanes', 2)
    product2 = Product(50, 'reeboks', '2 lb', 'grouch', 49)
    real_price = product1.addTax(0.08)
    print real_price
else:
    product1 = Product(25, 'undies', '2 kg', 'hanes', 2)
    product2 = Product(50, 'reeboks', '2 lb', 'grouch', 49)
