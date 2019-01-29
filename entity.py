class create_entity:
    def __init__(self, name, ac, hp):
        self.name = name
        self.ac = ac
        self.cur_hp = hp
        self.max_hp = hp
        self.half_max_hp = hp / 2
        self.dead = False

    def print_entity(self):
        print(f"The enemy {self.name} with AC {self.ac} has {self.cur_hp}/{self.max_hp} HP left.")

    def hit_entity(self, roll):
        if (not(roll < self.ac)):
            return True
        else:
            return False

    def hurt_entity(self, damage):
        self.cur_hp -= damage
        if (self.cur_hp <= 0):
            self.dead = True
            return False
        elif ((self.cur_hp + damage) >= self.half_max_hp and
                self.cur_hp < self.half_max_hp):
            return True
        else:
            return False

def fight_over(entity_container):
    for i in range(len(entity_container)):
        if (entity_container[i].dead == False):
            return False
    return True

def find_entity_name(entity_container, name):
    for i in range(len(entity_container)):
        if ((entity_container[i].name).lower() == name.lower()):
            return i

def print_entities(entity_container):
    names = []
    for i in range(len(entity_container)):
        if (entity_container[i].dead == False):
            names.append(entity_container[i].name + f"({i+1})")

    print("\nThe enemies currently alive are: ", end="", flush=True)
    print(*names, sep = ", ")
