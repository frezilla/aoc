#==============================================================================
# --- Day 12: JSAbacusFramework.io ---
#==============================================================================


import queue
import re


def run():
    print("--- Day 12: JSAbacusFramework.io ---")
    puzzle = open("puzzle.txt", 'r')
    amount1 = 0
    amount2 = 0
    for line in puzzle:
        current_line = line.strip()
        result1 = re.findall("-?[0-9]+", current_line)
        for number in result1:
            amount1 += int(number)
        lifo = queue.LifoQueue()
        new_line = ""
        index = 0
        for current_char in current_line:
            new_line += current_char
            if current_char == "{":
                lifo.put(index)
            elif current_char == "}":
                if not lifo.empty():
                    begin_index = lifo.get()
                    substring = new_line[begin_index:]
                    if ":\"red\"" in substring:
                        new_line = new_line[:begin_index]
                        index = len(new_line) - 1
            index += 1
        result2 = re.findall("-?[0-9]+", new_line)
        for number in result2:
            amount2 += int(number)
    puzzle.close()
    print(f"Part 1 : Somme des nombres : {amount1}")
    print(f"Part 2 : Somme des nombres : {amount2}")


if __name__ == "__main__":
    run()
