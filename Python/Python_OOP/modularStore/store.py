import product

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                idx = self.products.index(product)
                self.products.pop(idx)
                break
        return self
    def inventory(self):
        print "******* Product List *********"
        for product in self.products:
            product.displayInfo()
        return self


if __name__ != '__main__':
    safeway = Store([product.product1], 'Sunnyvale', 'MoolahBaby')
    safeway.inventory()

    safeway.add_product(product.product2)
    safeway.inventory()

    safeway.remove_product('undies')
    safeway.inventory()
