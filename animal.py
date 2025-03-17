import random

class Animal:
    def __init__(self):
        self.__score = 0
        self.__across = random.randint(0, 39)
        self.__down = random.randint(0, 39)

    def get_across(self):
        return self.__across

    def get_down(self):
        return self.__down

    def get_score(self):
        return self.__score

    def move(self, desert):
        change_across = GenerateChangeInCoordinate(self.__across)
        change_down = GenerateChangeInCoordinate(self.__down)
        new_across = self.__across + change_across
        new_down = self.__down + change_down
        desert._grid[self.__across][self.__down] = "."
        self.__across = new_across
        self.__down = new_down
        desert._grid[self.__across][self.__down] = "A"
        if desert._food_location == (self.__across, self.__down):
            self.eat_food(desert)

    def eat_food(self, desert):
        self.__score += 1
        desert._food_location = None
        if len(desert._animal_list) < 20:
            new_animal = Animal()
            desert._animal_list.append(new_animal)
            x, y = new_animal.get_across(), new_animal.get_down()
            desert._grid[x][y] = "A"

        desert.generate_food()

class Desert:
    def __init__(self):
        self._grid = [["." for _ in range(40)] for _ in range(40)]
        self._animal_list = []
        self._step_counter = 0

        for _ in range(5):
            animal = Animal()
            self._animal_list.append(animal)
            x, y = animal.get_across(), animal.get_down()
            self._grid[x][y] = "A"

        self._food_location = None
        self.generate_food()

    def generate_food(self):
        while True:
            x = random.randint(0, 39)
            y = random.randint(0, 39)
            if self._grid[x][y] == ".":
                self._food_location = (x, y)
                self._grid[x][y] = "F"
                break


def GenerateChangeInCoordinate(coordinate):
    if coordinate == 0:
        return random.choice([0, 1])
    elif coordinate == 39:
        return random.choice([0, -1])
    else:
        return random.choice([-1, 0, 1])
    





desert = Desert()

for i in range(500):
    for animal in 500._animal_list:
        animal.move(500)
    desert._step_counter += 1
    for row in desert._grid:
        print(" ".join(row))
    print(f"Step: {desert._step_counter}, Animals: {len(desert._animal_list)}")
    print("-" * 80)


