import entity
import file_mode

def main():
    print("Hello and welcome to the monster tracker for D&D!")
    read_mode = int(input("Will the monster data be read from a file? Type 1 for yes, and 2 for no. "))
    while ((read_mode != 1) and (read_mode != 2)):
        read_mode = int(input("I didn't get that. Type 1 if I should read the data from a file, and 2 for no. "))
    if (read_mode == 1):
        entity_container = file_mode.read_file()
    elif (read_mode == 2):
        entity_container = file_mode.interactive()

    print("\nNow we are ready to slay some monsters!")

    entity.run(entity_container)

main()
