#==============================================================================
# --- Day 18: Like a GIF For Your Yard ---
#==============================================================================


cols = rows = 100
steps = 100


def create_empty_grid():
    arr = []
    for i in range(rows + 2):
        col = []
        for j in range(cols + 2):
            col.append('.')
        arr.append(col)
    return arr


def expand_grid(grid):
    arr = []
    col = []
    for i in range(cols + 2):
        col.append('.')
    arr.append(col)
    for r in range(rows):
        col = ['.']
        for c in range(cols):
            col.append(grid[r][c])
        col.append('.')
        arr.append(col)
    col = []
    for i in range(cols + 2):
        col.append('.')
    arr.append(col)
    return arr


def load_puzzle():
    puzzle = open("puzzle.txt", "r")
    arr = []
    for line in puzzle:
        current_line = line.strip()
        col = []
        for i in range(cols):
            col.append(current_line[i])
        arr.append(col)
    puzzle.close()
    return arr


def next_step_part1(initial_step):
    new_grid = create_empty_grid()
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            new_grid[r][c] = next_step_light(initial_step, r, c)
    return new_grid


def next_step_part2(initial_step):
    new_grid = create_empty_grid()
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            new_grid[r][c] = next_step_light(initial_step, r, c)
    new_grid[1][1] = new_grid[1][cols] = new_grid[rows][1] = new_grid[rows][cols] = '#'
    return new_grid


def next_step_light(grid, row, col):
    nb_off_lights = 0
    if grid[row - 1][col -1 ] == '.':
        nb_off_lights += 1
    if grid[row - 1][col] == '.':
        nb_off_lights += 1
    if grid[row - 1][col + 1] == '.':
        nb_off_lights += 1
    if grid[row][col -1] == '.':
        nb_off_lights += 1
    if grid[row ][col + 1] == '.':
        nb_off_lights += 1
    if grid[row + 1][col - 1] == '.':
        nb_off_lights += 1
    if grid[row + 1][col] == '.':
        nb_off_lights += 1
    if grid[row + 1][col + 1] == '.':
        nb_off_lights += 1
    nb_on_lights = 8 - nb_off_lights
    if grid[row][col] == '#':
        if nb_on_lights in (2, 3):
            return '#'
        else:
            return '.'
    else:
        if nb_on_lights == 3:
            return '#'
        else:
            return '.'


def run():
    print("--- Day 18: Like a GIF For Your Yard ---")
    grid_part1 = expand_grid(load_puzzle())
    grid_part2 = expand_grid(load_puzzle())
    grid_part2[1][1] = grid_part2[1][cols] = grid_part2[rows][1] = grid_part2[rows][cols] = '#'
    for i in range(steps):
        grid_part1 = next_step_part1(grid_part1)
        grid_part2 = next_step_part2(grid_part2)
    nb_on_lights = 0
    for row in grid_part1:
        for col in row:
            if col == '#':
                nb_on_lights += 1
    print(f'1ère étape : Nombre de lamps allumées après {steps} étapes : {nb_on_lights}')
    nb_on_lights = 0
    for row in grid_part2:
        for col in row:
            if col == '#':
                nb_on_lights += 1
    print(f'2ème étape : Nombre de lamps allumées après {steps} étapes : {nb_on_lights}')


if __name__ == "__main__":
    run()