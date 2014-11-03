import random


class Animal():

    def __init__(self, species, age, name, gender, weight, life_expectancy,
            food_type, gestation_period, newborn, averageWeight, weight_age,
            food_weight):
        self.species = species
        self.age = age
        self.gender = gender
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.food_type = food_type
        self.gestation_period = gestation_period
        self.newborn = newborn
        self.averageWeight = averageWeight
        self.weight_age = weight_age
        self.food_weight = food_weight
        self.name = name

    def animal_grow(self, months):
        self.weight += months*self.weight_age
        self.age += months
        if self.weight > self.averageWeight:
            self.weight = self.averageWeight

    def animal_eat(self, food_type):
        if self.food_type == food_type:
            food = self.weight*self.food_weight
            shit = food / 2
            self.weight += food - shit
            if self.weight > self.averageWeight:
                self.weight = self.averageWeight
        else:
            print("Wrong food type")

    def animal_die(self):
        age = self.age / 12
        chance_of_dying = age // self.life_expectancy
        random.randrange(chance_of_dying, 1)
        dead = random.random()
        if dead == 1:
            return True
        else:
            return False

