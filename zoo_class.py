class Zoo():

    def __init__(self, animals, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    def accommodate(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        else:
            print ("{} is already in Zoo".format(animal))

    def animals_count(self):
        count_animals = 0
        for animal in self.animals:
            count_animals += 1
        return count_animals

    def daily_incomes(self):
        return self.animals_count()*60

    def type_of_food(self, food):
        meat_price = 4
        grass_prise = 2
        if food == "meat":
            return meat_price
        elif food == "grass":
            return grass_prise
        else:
            print "Wrong input"

    def daily_outcomes(self):
        expense = 0
        for animal in self.animals:
            expense += animal.food_weight*self.type_of_food
        return expense

    def animals_die(self):
        for animal in self.animals:
            if animal.animal_die():
                self.animals.remove(animal)


