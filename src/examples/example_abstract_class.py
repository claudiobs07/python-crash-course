from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        print("Some implementation!")


class OtherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")


class AnotherSubclass(AbstractClassExample):
    pass


if __name__ == '__main__':

    OtherSubclass().do_something()

    AnotherSubclass()
