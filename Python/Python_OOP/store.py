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
            if product['name'] == product_name:
                idx = self.products.index(product)
                self.products.pop(idx)
                break
        return self
    def inventory(self):
        print "******* Product List *********"
        for product in self.products:
            print product
        return self

safeway = Store([{'name': 'milk', 'exp': '6-17'}, {'name': 'cheese', 'exp': '6-19'}], 'Sunnyvale', 'MoolahBaby')
safeway.inventory()

safeway.add_product({'name': 'toe-fungus', 'exp': '6-30'})
safeway.inventory()

safeway.remove_product('milk')
safeway.inventory()
