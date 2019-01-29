import entities
from entity import create_entity

def read_entity_info(entity_info):
    entity_info = entity_info.split(",")
    name = entity_info[0]
    ac = int(entity_info[1])
    hp = int(entity_info[2])
    entity = create_entity(name, ac, hp)
    return entity

def interactive():
    entities.entity_container = []
    nr = int(input("\nUnderstood! Please write the number of enemies: "))
    print("Let's define some enemies. I will need the following, separated by comma.")

    for i in range(nr):
        entity_info = input(f"Name, AC, and HP of enemy{i+1}: ")
        entity = read_entity_info(entity_info)
        entities.entity_container.append(entity)

    return entities.entity_container

def read_file():
    entities.entity_container = []
    name = input("Understood! What is the name of the file? ")
    file = open(name, 'r')
    lines = file.readlines()

    for i in range(len(lines)):
        entity = read_entity_info(lines[i])
        entities.entity_container.append(entity)

    return entities.entity_container

def setup():
    print("Hello and welcome to the enemy tracker for D&D!")
    read_mode = input("Will the enemy data be read from a file? Type y for yes, and n for no. ")
    while ((read_mode != "y") and (read_mode != "n")):
        read_mode = input("I didn't get that. Type y if I should read the data from a file, and n for no. ")
    if (read_mode == "y"):
        entities.entity_container = read_file()
    elif (read_mode == "n"):
        entities.entity_container = interactive()

    print("\nNow we are ready to slay some enemies!")
