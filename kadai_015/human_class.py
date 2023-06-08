# %%
from typing import NoReturn


class Human:
    def __init__(self, name: str, age: int =0):
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return(self.__name)

    @property
    def age(self) -> int:
        return(self.__age)
    @age.setter
    def age(self, age:int):
        self.__age = age

    def add_age(self, add_age:int = 1):
        self.__age += add_age

    def printinfo(self):
        print(f'name: {self.__name}\n age: {self.__age}')

japanese = Human(name="S.Nakamoto", age=10)
japanese.add_age()

japanese.printinfo()

# %%
