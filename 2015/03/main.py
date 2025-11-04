#==============================================================================
# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#==============================================================================


def move_step(direction):
    _x = 0
    _y = 0
    if direction == "^":
        _y -= 1
    elif direction == "<":
        _x -= 1
    elif direction == "v":
        _y += 1
    elif direction == ">":
        _x += 1
    return [_x, _y]


def run():
    print("--- Day 3: Perfectly Spherical Houses in a Vacuum ---")
    x = 0
    y = 0
    visited_houses = {(x, y)}

    fhand = open("puzzle.txt", "r")
    instructions = ''
    for line in fhand:
        instructions += line.rstrip()

    for c in instructions:
        array = move_step(c)
        x += array[0]
        y += array[1]
        visited_houses.add((x, y))

    print(f"Nombre de maison avec au moins un cadeau : {len(visited_houses)}")
    visited_houses.clear()

    x_santa = 0
    y_santa = 0
    x_robot = 0
    y_robot = 0
    for (santa, robot) in zip(instructions[0::2], instructions[1::2]):
        array = move_step(santa)
        x_santa += array[0]
        y_santa += array[1]
        visited_houses.add((x_santa, y_santa))
        array = move_step(robot)
        x_robot += array[0]
        y_robot += array[1]
        visited_houses.add((x_robot, y_robot))

    print(f"Nombre de maison avec au moins un cadeau (distribué par Santa et son robot) : {len(visited_houses)}")


if __name__ == '__main__':
    run()