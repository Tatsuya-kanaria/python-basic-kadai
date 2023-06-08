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

    def check_adult(self):
        if self.age >= 20:
            check_result = '大人'
        else:
            check_result = '大人ではない'
        print(f'{self.name} は{check_result}です。')

    def printinfo(self):
        print(f'name: {self.__name}\n age: {self.__age}')

human_dict = {
    "japanese":{"name":"S.Nakanoto", "age":19},
    "american":{"name":"Elon Reeve Musk,", "age":51},
    "Russian":{"name":"アリサ・ミハイロヴナ・九条", "age":16},
    }

for instans_name, argment in human_dict.items():
    instans_name = Human(argment["name"], argment["age"])
    instans_name.printinfo()
    instans_name.check_adult()

japanese = Human(name="become adult", age=19)
japanese.printinfo()
japanese.check_adult()

japanese.add_age()
japanese.printinfo()
japanese.check_adult()


# %%
