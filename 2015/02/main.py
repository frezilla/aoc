#==============================================================================
# --- Day 2: I Was Told There Would Be No Math ---
#==============================================================================


def run():
    print("--- Day 2: I Was Told There Would Be No Math ---")
    fhand = open("puzzle.txt", "r")
    square_feet = 0
    feet_of_ribbon = 0
    for line in fhand:
        current_line = line.rstrip()
        tokens = current_line.split("x")
        l = int(tokens[0])
        w = int(tokens[1])
        h = int(tokens[2])

        side1 = l * w
        perimeter1 = (l + w) * 2
        side2 = w * h
        perimeter2 = (w + h) * 2
        side3 = h * l
        perimeter3 = (h + l) * 2

        side_min = min([side1, side2, side3])
        perimeter_min = min([perimeter1, perimeter2, perimeter3])

        current_square_feet = 2 * side1 + 2 * side2 + 2 * side3 + side_min
        square_feet += current_square_feet

        current_feet_of_ribbon = perimeter_min + (l * w * h)
        feet_of_ribbon += current_feet_of_ribbon

        print(f"Surface de la boite {l} * {w} * {h} = {current_square_feet} - longueur du ruban = {current_feet_of_ribbon}")

    print(f"Surface totale du papier d'emballage: {square_feet} - Longueur total du ruban : {feet_of_ribbon}")


if __name__ == '__main__':
    run()