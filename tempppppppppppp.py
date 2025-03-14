import random
class Animal():
    def __init__(self):
        self.__score = 0
        self.__across = random.randint(0, 39)
        self.__down = random.randint(0, 39)
    
    def EatFood(self, desert):
        Desert.removefood(self.__across, self.__down)
        self.__score += 1
        Desert.generatefood()
        self.__init__

    def Move(self):
        self.__across = GenerateChangeInCoordinate(self.__across)
        self.__down = GenerateChangeInCoordinate(self.__down)
        if desert.foodat(self.__across, self.__down):
            self.EatFood(desert)


class Desert():
    def __init__(self):
        self.__grid = [[" " for i in range(40)] for i in range(40)]
        self.__AnimalList = []
        self.__StepCounter = 0

        for i in range(5):
            animal = Animal()
            self.__AnimalList.append(animal)
            
