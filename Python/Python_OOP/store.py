class Store(object):
    def __init__(self, products, location):
        self.products = products
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.products.append(product)
        return self
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                idx = self.products.index
                self.products.pop(idx)
                break
        return self
    def inventory(self):
        for product in self.products:
            print product
        return self
