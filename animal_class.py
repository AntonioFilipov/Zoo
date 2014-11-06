import random
import json


class Animal():
    my_file = open("All_Mighty.json", 'r')
    species_json = json.load(my_file)

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        is_animal_in_json = False
        for animal in self.species_json:
            if self.species == animal:
                self.life_expectancy = Animal.species_json[animal]["life_expectancy"]
                self.food_type = Animal.species_json[animal]["food_type"]
                self.gestation_period = Animal.species_json[animal]["gestation_period"]
                self.newborn = Animal.species_json[animal]["newborn"]
                self.average_weight = Animal.species_json[animal]["average_weight"]
                self.weight_age = Animal.species_json[animal]["weight_age"]
                self.food_weight = Animal.species_json[animal]["food_weight"]
                is_animal_in_json = True
        if not is_animal_in_json:
            raise ValueError("No such animal in json")

    def __str__(self):
        return "{} : {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.species,
                                                                        self.age,
                                                                        self.name,
                                                                        self.gender,
                                                                        self.weight,
                                                                        self.life_expectancy,
                                                                        self.food_type,
                                                                        self.gestation_period,
                                                                        self.newborn,
                                                                        self.average_weight,
                                                                        self.weight_age,
                                                                        self.food_weight
                                                                        )

    def animal_grow(self, months):
        self.weight += months*self.weight_age
        self.age += months
        if self.weight > self.average_weight:
            self.weight = self.average_weight

    def animal_eat(self, food_type):
        if self.food_type == food_type:
            food = self.weight*self.food_weight
            shit = food / 2
            self.weight += food - shit
            if self.weight > self.average_weight:
                self.weight = self.average_weight
        else:
            return "Wrong food type"

    def animal_die(self):
        chance_of_dying = self.age / self.life_expectancy
        chance_of_dying *= 100
        dead = random.randrange(int(chance_of_dying), 100)
        if dead > 90:
            return True
        else:
            return False


