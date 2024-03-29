class Pet:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):

    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats


class Cat(Pet):

    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs


if __name__ == '__main__':
    mister_pet = Pet("Mister", "Dog")
    mister_dog = Dog("Mister", True)
    mister_cat = Cat("Mister", True)
    print(isinstance(mister_cat, Pet))
    print(isinstance(mister_cat, Cat))
    print(isinstance(mister_cat, Dog))
