from craft_control import chandrayaan_3

def main():
    initial_position = [0, 0, 0]
    initial_direction = "N"
    commands = ["f", "r", "u", "b", "l"]

    print("Starting Position:", initial_position)
    print("Initial Direction:", initial_direction)

    final_position, final_direction =  chandrayaan_3(initial_position, initial_direction, commands)

    print("Final Position:", final_position)
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    main()
