#==============================================================================
# --- Day 13: Knights of the Dinner Table ---
#==============================================================================


class Person:
    def __init__(self, name, _rules):
        self.name = name
        self.left_neighbor = None
        self.right_neighbor = None
        self.rules = dict()
        if _rules:
            for current_rule in _rules:
                self.rules.update({current_rule[1] : current_rule[2]})


    def compute_happiness(self):
        left_value = self.rules.setdefault(self.left_neighbor, 0)
        right_value = self.rules.setdefault(self.right_neighbor, 0)
        return left_value + right_value


def execute(_link, _names, _persons):
    new_value= ""
    if len(_link) > 0:
        new_value = _link + " "
    if len(_names) == 1:
        new_value += _names[0]
        happiness = perform(new_value.split(), _persons)
        global max_happiness
        if happiness > max_happiness:
            print(f"Table : {new_value} --> {happiness}")
            max_happiness = happiness
    else:
        for current_index in range(len(_names)):
            current_name = _names.pop(current_index)
            new_value += current_name
            execute(new_value, _names, _persons)
            _names.insert(current_index, current_name)
            new_value = new_value[:len(new_value) - len(current_name)]


def create_persons_from_rules(_rules):
    names_set = set()
    for current_rule in _rules:
        names_set.add(current_rule[0])
    result_dic = dict()
    for current_name in names_set:
        current_rules = []
        for current_rule in _rules:
            if current_name == current_rule[0]:
                current_rules.append(current_rule)
        result_dic[current_name] = Person(current_name, current_rules)
    return result_dic


def perform(_datas, _persons):
    total_happiness = 0
    for current_index in range(0, len(_datas)):
        current_person = _persons[_datas[current_index]]
        previous_index = current_index - 1
        next_index = current_index + 1
        if current_index == 0:
            previous_index = len(_datas) - 1
        if current_index == len(_datas) - 1:
            next_index = 0
        current_person.left_neighbor = _datas[previous_index]
        current_person.right_neighbor = _datas[next_index]
        total_happiness += current_person.compute_happiness()
    return total_happiness


def read_rules(_filename):
    result_list = list()
    file = open(_filename, 'r')
    for line in file:
        line = line.strip().split()
        if line[2] == 'gain':
            result_list.append((line[0], line[10][:len(line[10]) - 1], int(line[3])))
        elif line[2] == 'lose':
            result_list.append((line[0], line[10][:len(line[10]) - 1], -1 * int(line[3])))
    return result_list


def run():
    global max_happiness
    print("--- Day 13: Knights of the Dinner Table ---")
    rules = read_rules("puzzle.txt")
    print("Etape 1")
    persons = create_persons_from_rules(rules)
    person_names = persons.keys()
    max_happiness = 0
    execute("", list(person_names), persons)
    print("Etape 2")
    for person in persons.values():
        person.rules.update({'Me': 0})
    persons.update({'Me' : Person('Me', None)})
    person_names = persons.keys()
    max_happiness = 0
    execute("", list(person_names), persons)


if __name__ == "__main__":
    run()