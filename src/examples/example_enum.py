from enum import Enum

class Color(Enum):
    red  = 1
    green = 2
    blue = 3

if __name__ == '__main__':
    for color in Color:
        print(color.name + ":" + str(color.value))
