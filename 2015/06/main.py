#==============================================================================
# --- Day 6: Probably a Fire Hazard ---
#==============================================================================


TURNED_OFF = False
TURNED_ON = True


class Data:
    def __init__(self, order, x1, y1, x2, y2):
        self.order = order
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def create_array_part1():
    array = []
    i = 0
    while i < 1000000:
        array.append(TURNED_OFF)
        i += 1
    return array


def create_array_part2():
    array = []
    i = 0
    while i < 1000000:
        array.append(0)
        i += 1
    return array


def get_index(x, y):
    return y * 1000 + x


def parse_line(line):
    working_line = line
    if working_line.startswith("toggle"):
        _order = "toggle"
    elif working_line.startswith("turn off"):
        _order = "turn off"
    else:
        _order = "turn on"
    working_line = working_line[len(_order) + 1:]
    index = working_line.find(",")
    x1 = int(working_line[:index])
    working_line = working_line[index + 1:]
    index = working_line.find(" ")
    y1 = int(working_line[:index])
    working_line = working_line[index + len("through "):]
    index = working_line.find(",")
    x2 = int(working_line[:index])
    working_line = working_line[index + 1:]
    y2 = int(working_line)
    return Data(_order, x1, y1, x2, y2)


def run():
    print("--- Day 6: Probably a Fire Hazard ---")
    print("Part 1")
    run_part1()
    print("Part 2")
    run_part2()


def run_part1():
    puzzle = open("puzzle.txt", "r")
    lights = create_array_part1()
    for line in puzzle:
        current_line = line.strip()
        data = parse_line(current_line)
        order = data.order
        index_x = data.x1
        while index_x <= data.x2:
            index_y = data.y1
            while index_y <= data.y2:
                current_index = get_index(index_x, index_y)
                index_y += 1
                if order == "turn on":
                    lights[current_index] = TURNED_ON
                elif order == "turn off":
                    lights[current_index] = TURNED_OFF
                else:
                    if lights[current_index] == TURNED_ON:
                        lights[current_index] = TURNED_OFF
                    else:
                        lights[current_index] = TURNED_ON
            index_x += 1
    puzzle.close()
    lit_lights = 0
    for x in lights:
        if x == TURNED_ON:
            lit_lights = lit_lights + 1
    print(f"Number of lit lights: {lit_lights}")


def run_part2():
    puzzle = open("puzzle.txt", "r")
    lights = create_array_part2()
    for line in puzzle:
        current_line = line.strip()
        data = parse_line(current_line)
        order = data.order
        index_x = data.x1
        while index_x <= data.x2:
            index_y = data.y1
            while index_y <= data.y2:
                current_index = get_index(index_x, index_y)
                index_y += 1
                if order == "turn on":
                    lights[current_index] = lights[current_index] + 1
                elif order == "turn off":
                    lights[current_index] = lights[current_index] - 1
                    if lights[current_index] < 0:
                        lights[current_index] = 0
                else:
                    lights[current_index] = lights[current_index] + 2
            index_x += 1
    puzzle.close()
    brightness = 0
    for x in lights:
        brightness += x
    print(f"Total brightness of all lights : {brightness}")


if __name__ == '__main__':
    run()