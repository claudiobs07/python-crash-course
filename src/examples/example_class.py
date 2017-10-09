class Product:

    def __init__(self, name, price, brand, inventory):
        self.name = name
        self.price = price
        self.brand = brand
        self.inventory = inventory

    def __repr__(self):
        return "Product[" + "name=" + str(self.name) + ", price=" + str(self.price) + "]"

    def __eq__(self, other):
        return self.name == other.name

if __name__ == '__main__':
    pass
    #p1 = Product("Calvin Klein Perfume",110.0, "Calvin Klein", 0)
