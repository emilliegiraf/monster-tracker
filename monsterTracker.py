class monster:
    def __init__(self, name, ac, hp):
        self.name = name
        self.bloodied = False
        self.dead = False
        self.ac = ac
        self.half_max_hp = hp / 2
        self.hp = hp

    def print_monster(self):
        print("The monster", self.name, "with AC", self.ac, "has", self.hp,
              "HP left.")

    def hit_monster(self):
        roll = int(input("Roll to hit the monster: "))
        if (roll >= self.ac):
            self.hurt_monster()
        else:
            print("You did not hit.")

    def hurt_monster(self):
        damage = int(input("Roll your damage: "))
        self.hp -= damage
        if (self.hp < 0):
            self.dead = True
            print("The monster", self.name, "is dead!")
        elif ((self.hp + damage) > self.half_max_hp
              and self.hp <= self.half_max_hp):
            self.bloodied = True
            print("The monster", self.name, "is bloodied.")
        else:
            print("The monster has been damaged.")


def main():
    #name = input("Let's slay a monster! I will need these things:\nName: ")
    #ac = int(input("The AC: "))
    #hp = int(input("HP: "))
    monster1 = monster('Ken', 12, 30)
    while (not monster1.dead):
        monster1.print_monster()
        monster1.hit_monster()


main()
