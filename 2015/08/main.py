#==============================================================================
# --- Day 8: Matchsticks ---
#==============================================================================


def encode_new_string(line):
    new_string = ""
    index = 0
    while index < len(line):
        if line[index] == "\"":
            new_string += "\\"
        elif line[index] == "\\":
            new_string += "\\"
        new_string += line[index]
        index += 1
    return "\"" + new_string + "\""


def len_memory(line):
    numbers_of_characters = 0
    hex_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    index = 0
    while index < len(line):
        if line[index] == "\\":
            if line[index + 1] == "x" and line[index + 2] in hex_array and line[index + 3] in hex_array:
                index += 4
            else:
                index += 2
            numbers_of_characters += 1
        else:
            if not line[index] == "\"":
                numbers_of_characters += 1
            index += 1
    return numbers_of_characters

def run():
    print("--- Day 8: Matchsticks ---")
    puzzle = open("puzzle.txt", 'r')
    numbers_encoded = 0
    numbers_characters = 0
    numbers_memory = 0
    for line in puzzle:
        line_part1 = line.strip()
        line_part2 = encode_new_string(line_part1)
        numbers_characters += len(line_part1)
        numbers_encoded += len(line_part2)
        numbers_memory += len_memory(line_part1)
    puzzle.close()
    print(f"Number of characters of code for string literals ({numbers_characters}) minus the number of characters in memory ({numbers_memory}) => {numbers_characters - numbers_memory}")
    print(f"Total number of characters to represent the newly encoded string ({numbers_encoded}) minus the number of characters of code for string literals ({numbers_characters}) => {numbers_encoded - numbers_characters}")


if __name__ == '__main__':
    run()