from zoo_class import Zoo
from animal_class import Animal


def see_animals(zoo):
    if len(zoo.animals) != 0:
        for animal in zoo.animals:
            print (animal)
    else:
        print ("There is not any animals in the zoo")


def create_animal(species, name, age, gender, weight):
    animal = Animal(str(species), age, str(name), str(gender), weight)
    return animal


def main():
    my_zoo = Zoo(50, 1000)
    print("=======================================================================================================")
    print("Commands are:")
    print("see_animals - list of all animals in the zoo")
    print("accommodate <species> <name> <age> <gender> <weight> - adds an animal to the zoo")
    print("move_to_habitat <species> <name> - removes an animal from the zoo and returns it to its natural habitat")
    print("exit - exit the program")
    print("=======================================================================================================")

    while (True):
        command = input("Enter a command:")
        commands = command.split()
        if commands[0] == "see_animals":
            see_animals(my_zoo)
        elif commands[0] == "accommodate":
            new_animal = create_animal(commands[1], commands[2], commands[3], commands[4], commands[5])
            my_zoo.accommodate(new_animal)
        elif commands[0] == "move_to_habitat":
            for animal in my_zoo.animals:
                if (animal.species == commands[1] and animal.name == commands[2]):
                    my_zoo.animals.remove(animal)
        elif commands[0] == "exit":
            break

if __name__ == '__main__':
    main()

