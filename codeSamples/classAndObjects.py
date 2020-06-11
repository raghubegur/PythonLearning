class Fruit():
    def __init__(self,name):
        # Constructor
        self.name = name

    # def getName(self):
    #     print(self.name)

    @property
    def name(self):
        print('Inside the getter')
        return self.__name

    @name.setter
    def name(self, value):
        print('Inside the setter')
        self.__name = value


fruit = Fruit('Orange')
# fruit.getName()
fruit.name = 'Apple'
print(fruit.name)
