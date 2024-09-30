import sys


class Cat:
    says: str = "Meow"

    def __init__(self, color, age, sex):
        self.color = color
        self.age = age
        self.sex = sex
        self.__sound = "prr"


if __name__ == "__main__":
    # kitty = Cat("grey", 5, "Male")
    # print(kitty.__dict__)
    # print(kitty.__sound)

    l = []
    print(sys.getsizeof(l))
    