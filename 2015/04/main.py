#==============================================================================
# --- Day 4: The Ideal Stocking Stuffer ---
#==============================================================================


import hashlib


def execute(nb_zeros):
    fhand = open("puzzle.txt", "r")
    secret_key = ''
    for line in fhand:
        secret_key += line.rstrip()
    answer = 0
    n = '0'
    while 1:
        str_value = str(answer)
        test_value = f"{secret_key}{str_value}"
        md5_value = hashlib.md5(test_value.encode()).hexdigest()
        if md5_value.startswith(n.zfill(nb_zeros)):
            break
        answer += 1
    print(f"Réponse : {answer}")


def run():
    print("--- Day 4: The Ideal Stocking Stuffer ---")
    execute(5)
    execute(6)


if __name__ == '__main__':
    run()