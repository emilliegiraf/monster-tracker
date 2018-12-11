def init_monster(name, ac, hp):
    monster = {'name': name, 'ac': ac, 'hp': hp}

class monster:
    def __init__(self, name, ac, hp):
        self.name = name
        self.dead = False
        self.ac = ac
        self.half_max_hp = hp / 2
        self.hp = hp

    def print_monster(self):
        print("The monster", self.name, "with AC", self.ac, "has", self.hp,
        "HP left.")

    def hit_monster(self, roll):
        if (not(roll < self.ac)):
            return True
        else:
            return False

    def hurt_monster(self, damage):
        self.hp -= damage
        if (self.hp < 0):
            self.dead = True
            return 3
        elif ((self.hp + damage) > self.half_max_hp and
                self.hp < self.half_max_hp):
            return 2
        else:
            return 1

def main():
    #name = input("Let's slay a monster! I will need these things:\nName: ")
    #ac = int(input("The AC: "))
    #hp = int(input("HP: "))
    monster1 = monster('Ken', 12, 30)
    while (not monster1.dead):
        monster1.print_monster()
        roll = int(input("Roll to hit the monster: "))
        if (monster1.hit_monster(roll)):
            dmg = int(input("How much damage does the monster take? "))
            monster1.hurt_monster(dmg)
        else:
            print("That does not hit :(")

main()
