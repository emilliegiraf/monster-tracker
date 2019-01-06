from entity import create_entity

def read_entity_info(entity_info):
    entity_info = entity_info.split(",")
    name = entity_info[0]
    ac = int(entity_info[1])
    hp = int(entity_info[2])
    entity = create_entity(name, ac, hp)
    return entity

def interactive():
    entities = []
    nr = int(input("\nUnderstood! Please write the number of monsters: "))
    print("Let's define some monsters. I will need the following, seperated by comma.")

    for i in range(nr):
        entity_info = input(f"Name, AC, and HP of monster{i}: ")
        entity = read_entity_info(entity_info)
        entities.append(entity)

    return entities

def read_file():
    entities = []
    name = input("Understood! What is the name of the file? ")
    file = open(name, 'r')
    lines = file.readlines()

    for i in range(len(lines)):
        entity = read_entity_info(lines[i])
        entities.append(entity)

    return entities
