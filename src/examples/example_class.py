class Product:

    def __init__(self, name, price, brand, inventory):
        self._name = name
        self._price = price
        self._brand = brand
        self._inventory = inventory

    @property
    def name(self):
        print("getter name")
        return self._name

    @name.setter
    def name(self, name):
        print("setter name")
        self._name = name

    @property
    def price(self):
        print("getter price")
        return self._price

    @price.setter
    def price(self, price):
        print("setter price")
        self._price = price

    def __repr__(self):
        return "Product[" + "name:" + str(self._name) + ", price:" + str(self._price) + ", inventory:" + str(self._inventory) +"]"

    def __str__(self):
        return "Product(" + "name=" + str(self._name) + ", price=" + str(self._price) + ")"

    def __eq__(self, other):
        return self.name == other.name


if __name__ == '__main__':
    product = Product("Calvin Klein Perfume 150ml", 110.0, "Calvin Klein", 0)

    product.name = "Mac"
    print(product.name)

    product.price = 50
    print(product.price)

    print(product)
    print(repr(product))
