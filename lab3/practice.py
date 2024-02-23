class Person():
    def __init__(self,name,year):
            self.name = name
            self.year = year
    def func(self):
        if self.year==3:
            return f"{self.name} is {self.year} course"
for i in range(4):
    name = input()
    year = int(input())
pp = Person(name,year)
result = pp.func()
print(result)
"""
class Person():
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def func(self):
        if self.year == 3:
            return f"{self.name} is in {self.year}rd year."
        else:
            return f"{self.name} is not in the 3rd year."
name = input("Enter name: ")
year = int(input("Enter year: "))
pp = Person(name, year)
result = pp.func()
print(result)
"""