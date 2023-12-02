import hashlib


def hash_md5_hex(string):
    result = hashlib.md5(string.encode())
    return result.hexdigest()


def find_smallest_number(key):
    number = 1
    while True:
        possible_string = key + str(number)
        hashed_string = hash_md5_hex(possible_string)

        valid = True
        for i in range(5):
            if hashed_string[i] != '0':
                valid = False

        if valid:
            break

        number += 1

    return number


print(find_smallest_number('abcdef'))
print(find_smallest_number('pqrstuv'))
print(find_smallest_number('iwrupvqb'))
