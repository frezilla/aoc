#==============================================================================
# --- Day 11: Corporate Policy ---
#==============================================================================


import re


def check_increasing_straight(password):
    password_length = len(password)
    previous_ascii = -1
    size = 0
    for i in range(password_length):
        current_ascii = ord(password[i])
        if previous_ascii + 1 == current_ascii:
            if size == 0:
                size = 1
            size += 1
        else:
            size = 0
        if size >= 3:
            return True
        previous_ascii = current_ascii
    return size >= 3


def check_invalid_letter(password):
    if re.search("[iol]", password):
        return False
    else:
        return True


def check_pairs(password):
    len_password = len(password)
    if len_password < 2:
        return False
    else:
        prev_letter = password[0]
        index = 1
        nb_pairs = 0
        while index < len_password:
            current_letter = password[index]
            if prev_letter == current_letter:
                nb_pairs += 1
                index += 2
                if index < len_password:
                    prev_letter = password[index - 1]
            else:
                prev_letter = current_letter
                index += 1
        return nb_pairs > 1


def inc_letter(letter):
    ascii_code_a = ord('a')
    ascii_code_z = ord('z')
    ascii_code = ord(letter[0])
    if ascii_code_a <= ascii_code <= ascii_code_z:
        ascii_code += 1
        if ascii_code > ascii_code_z:
            ascii_code = ascii_code_a
            carry = True
        else:
            carry = False
        return chr(ascii_code), carry
    else:
        raise ValueError('Invalid letter')


def inc_password(password):
    if not len(password) == 8:
        raise ValueError('Invalid password length')
    if "aaaaaaaa" <= password < "zzzzzzzzz":
        reversed_password = password[::-1]
        new_password = ""
        run = True
        for letter in reversed_password:
            if run:
                result = inc_letter(letter)
                add_letter = result[0]
                run = result[1]
            else:
                add_letter = letter
            new_password += add_letter
        return new_password[::-1]
    else:
        raise ValueError('Invalid password')


def run():
    print("--- Day 11: Corporate Policy ---")
    puzzle = open("puzzle.txt", "r")
    password = ''
    for line in puzzle:
        password += line.rstrip()
    puzzle.close()
    new_password = run_password(password)
    run_password(new_password)


def run_password(password):
    valid_password = False
    while not valid_password:
        password = inc_password(password)
        if check_increasing_straight(password) and check_invalid_letter(password) and check_pairs(password):
            print(f"New password : {password}")
            return password


if __name__ == "__main__":
    run()