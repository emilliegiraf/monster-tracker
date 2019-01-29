import entity
import entities

def run(entity_container):
    while (not entity.fight_over(entity_container)):
        if (len(entity_container) > 1):
            entity.print_entities(entity_container)
            nr = int(input("Write the number of the enemy being attacked: ")) - 1
        else:
            nr = 0

        while(nr == -1):
            name = input("I can't find that enemy. What is its number? ")
            nr = entity.find_entity_name(entity_container, name)

        cur_entity = entity_container[nr]
        cur_entity.print_entity()
        roll = int(input("Roll to hit the enemy: "))

        if (cur_entity.hit_entity(roll)):
            dmg = int(input("How much damage does the enemy take? "))
            bloodied = cur_entity.hurt_entity(dmg)
            if (bloodied):
                print(f"The entity {cur_entity.name} is bloodied!")

            if (cur_entity.dead):
                print(f"The enemy {cur_entity.name} is dead.")
            elif(nr != 0):
                cur_entity.print_entity()
            else:
                print("")

        else:
            print("That does not hit :(\n")

    print("\nThis fight is now over! Thanks for using enemy tracker!")
    exit()
