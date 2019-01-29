import entity
import entities
import file_mode
from run import run

def main():
    file_mode.setup()
    run(entities.entity_container)

main()
