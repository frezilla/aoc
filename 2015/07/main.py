#==============================================================================
# --- Day 7: Some Assembly Required ---
#==============================================================================


class Node:
    def __init__(self, name, operation, value):
        self.name = name
        self.operation = operation
        self.value = value
        self.children = []
        self.parents = []


    def add_child(self, node):
        self.children.append(node)


    def add_parent(self, parent):
        parent.add_child(self)
        self.parents.append(parent)
        if parent.is_valued():
            self.compute()


    def compute(self):
        old_value = self.value
        nb_parents = len(self.parents)
        if nb_parents == 1 and self.parents[0].is_valued():
            if self.operation == "ASSIGN":
                self.value = self.parents[0].value
            elif self.operation == "NOT":
                self.value = do_not(self.parents[0].value)
        elif nb_parents == 2:
            first_parent = self.parents[0]
            second_parent = self.parents[1]
            if first_parent.is_valued() and second_parent.is_valued():
                if self.operation == "AND":
                    self.value = do_and(first_parent.value, second_parent.value)
                elif self.operation == "LSHIFT":
                    self.value = do_lshift(first_parent.value, second_parent.value)
                elif self.operation == "OR":
                    self.value = do_or(first_parent.value, second_parent.value)
                elif self.operation == "RSHIFT":
                    self.value = do_rshift(first_parent.value, second_parent.value)
        else:
            raise Exception("More than two parents")
        if old_value != self.value:
            self.update_children()


    def is_valued(self):
        return self.value is not None


    def update_children(self):
        for child in self.children:
            child.compute()


def convert_value(value):
    if value.isnumeric():
        return int(value)
    else:
        return None


def do_and(x, y):
    return x & y


def do_lshift(x, n):
    return x << n


def do_not(x):
    return x ^ 65535


def do_or(x, y):
    return x | y


def do_rshift(x, n):
    return x >> n


def get_from_node(name, value, dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        _node = Node(name, None, value)
        dictionary[name] = _node
        return _node


def get_to_node(name, dictionary):
    if name in dictionary:
        return dictionary[name]
    else:
        _node = Node(name, None, None)
        dictionary[name] = _node
        return _node


def run():
    print("--- Day 7: Some Assembly Required ---")
    puzzle = open("puzzle.txt", 'r')
    wire_name = 'a'
    dictionary = {}
    for line in puzzle:
        current_line = line.rstrip()
        datas = current_line.split()
        nb_datas = len(datas)
        if nb_datas == 3:
            node = get_to_node(datas[2], dictionary)
            node.operation = "ASSIGN"
            from_node = get_from_node(datas[0], convert_value(datas[0]), dictionary)
            node.add_parent(from_node)
        elif nb_datas == 4:
            node = get_to_node(datas[3], dictionary)
            node.operation = "NOT"
            from_node = get_from_node(datas[1], convert_value(datas[1]), dictionary)
            node.add_parent(from_node)
        elif nb_datas == 5:
            node = get_to_node(datas[4], dictionary)
            node.operation = datas[1]
            from_node1 = get_from_node(datas[0], convert_value(datas[0]), dictionary)
            node.add_parent(from_node1)
            from_node2 = get_from_node(datas[2], convert_value(datas[2]), dictionary)
            node.add_parent(from_node2)
        else:
            raise Exception(f"Parse error {current_line}")
    puzzle.close()
    print(f"Signal provided to wire {wire_name} is {dictionary[wire_name].value}")
    wire_name_to_override = 'b'
    dictionary[wire_name_to_override].value = dictionary[wire_name].value
    dictionary[wire_name_to_override].update_children()
    print(f"New signal provided to wire {wire_name} is {dictionary[wire_name].value}")


if __name__ == "__main__":
    run()