#==============================================================================
# --- Day 15: Science for Hungry People ---
#==============================================================================


max_score = 0


class Teaspoon:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def add(self, teaspoon):
        _capacity = self.capacity + teaspoon.capacity
        _durability = self.durability + teaspoon.durability
        _flavor = self.flavor + teaspoon.flavor
        _texture = self.texture + teaspoon.texture
        _calories = self.calories + teaspoon.calories
        return Teaspoon(_capacity, _durability, _flavor, _texture, _calories)

    def multiply(self, m):
        _capacity = self.capacity * m
        _durability = self.durability * m
        _flavor = self.flavor * m
        _texture = self.texture * m
        _calories = self.calories * m
        return Teaspoon(_capacity, _durability, _flavor, _texture, _calories)

    def score(self):
        return max(self.capacity, 0) * max(self.durability, 0) * max(self.flavor, 0) * max(self.texture, 0)



def create_teaspoons(_filename):
    puzzle = open(_filename, "r")
    result_dict = dict()
    for line in puzzle:
        current_line = line.strip()
        datas = current_line.replace(":", "").replace(",", "").split()
        result_dict.update(
            {
                datas[0]:
                Teaspoon(int(datas[2]), int(datas[4]), int(datas[6]), int(datas[8]), int(datas[10]))
            }
        )
    puzzle.close()
    return result_dict


def run_part1(_teaspoons, _teaspoons_index, _nb = 0, _max = 101, selected_teaspoons = dict()):
    if _teaspoons_index == 0:
        selected_teaspoons.update({list(_teaspoons)[_teaspoons_index]: 100 - _nb})
        result_teaspoon = Teaspoon(0, 0, 0, 0, 0)
        for current_teaspoon in selected_teaspoons.keys():
            _ct = _teaspoons.get(current_teaspoon).multiply(selected_teaspoons[current_teaspoon])
            result_teaspoon = result_teaspoon.add(_ct)
        current_score = result_teaspoon.score()
        global max_score
        if current_score > max_score:
            max_score = current_score
            print(f"{selected_teaspoons} ==> {result_teaspoon.score()}")
        selected_teaspoons.popitem()
    else:
        for nb in range(_max):
            selected_teaspoons.update({list(_teaspoons)[_teaspoons_index]: nb})
            run_part1(_teaspoons, _teaspoons_index - 1, _nb + nb, _max - nb, selected_teaspoons)
            selected_teaspoons.popitem()


def run_part2(_teaspoons, _teaspoons_index, _nb = 0, _max = 101, selected_teaspoons = dict()):
    if _teaspoons_index == 0:
        selected_teaspoons.update({list(_teaspoons)[_teaspoons_index]: 100 - _nb})
        result_teaspoon = Teaspoon(0, 0, 0, 0, 0)
        for current_teaspoon in selected_teaspoons.keys():
            _ct = _teaspoons.get(current_teaspoon).multiply(selected_teaspoons[current_teaspoon])
            result_teaspoon = result_teaspoon.add(_ct)
        if result_teaspoon.calories == 500:
            current_score = result_teaspoon.score()
            global max_score
            if current_score > max_score:
                max_score = current_score
                print(f"{selected_teaspoons} ==> {result_teaspoon.score()}")
        selected_teaspoons.popitem()
    else:
        for nb in range(_max):
            selected_teaspoons.update({list(_teaspoons)[_teaspoons_index]: nb})
            run_part2(_teaspoons, _teaspoons_index - 1, _nb + nb, _max - nb, selected_teaspoons)
            selected_teaspoons.popitem()


def run():
    global max_score
    print("--- Day 15: Science for Hungry People ---")
    teaspoons = create_teaspoons("puzzle.txt")
    max_score = 0
    print("Part 1: ")
    run_part1(teaspoons, len(teaspoons) - 1)
    print("Part 2: ")
    max_score = 0
    run_part2(teaspoons, len(teaspoons) - 1)


if __name__ == "__main__":
    run()
