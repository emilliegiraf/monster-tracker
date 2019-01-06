class create_entity:
    def __init__(self, name, ac, hp):
        self.name = name
        self.ac = ac
        self.cur_hp = hp
        self.max_hp = hp
        self.half_max_hp = hp / 2
        self.dead = False

    def print_entity(self):
        print(f"The monster {self.name} with AC {self.ac} has {self.cur_hp}/{self.max_hp} HP left.")

    def hit_entity(self, roll):
        if (not(roll < self.ac)):
            return True
        else:
            return False

    def hurt_entity(self, damage):
        self.cur_hp -= damage
        if (self.cur_hp < 0):
            self.dead = True
            return 3
        elif ((self.cur_hp + damage) > self.half_max_hp and
                self.cur_hp < self.half_max_hp):
            return 2
        else:
            return 1

def fight_over(entity_container):
    for i in range(len(entity_container)):
        if (entity_container[i].dead == False):
            return False
    return True

def find_entity_name(entity_container, name):
    for i in range(len(entity_container)):
        if ((entity_container[i].name).lower() == name.lower()):
            return i
    return -1

def print_entities(entity_container):
    names = []
    for i in range(len(entity_container)):
        if (entity_container[i].dead == False):
            names.append(entity_container[i].name)

    print("\nThe monsters currently alive are: ", end="", flush=True)
    print(*names, sep = ", ")

def run(entity_container):
    while (not fight_over(entity_container)):
        print_entities(entity_container)
        name = input("Write the name of the monster being attacked: ")
        nr = find_entity_name(entity_container, name)

        while(nr == -1):
            name = input("I can't find that monster. What is the name? ")
            nr = find_entity_name(entity_container, name)

        entity_container[nr].print_entity()
        roll = int(input("Roll to hit the monster: "))

        if (entity_container[nr].hit_entity(roll)):
            dmg = int(input("How much damage does the monster take? "))
            entity_container[nr].hurt_entity(dmg)

            if (entity_container[nr].dead):
                print(f"The monster {entity_container[nr].name} is dead.")
            else:
                entity_container[nr].print_entity()

        else:
            print("That does not hit :(\n")

    print("\nThis fight is now over! Thanks for using monster tracker!")
    exit()
