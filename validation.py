import sys


def validation(n):
    try:
        new_n = int(n)
        assert new_n > 0
    except ValueError:
        print("\n\033[91mПотрібно вводити число!!\nПрограма завершила роботу.\033[0m")
        sys.exit()
    except AssertionError:
        print("\n\033[91mЧисло повинне бути більшим за 0!\nПрограма завершила роботу.\033[0m")
        sys.exit()
    return new_n


def validation_for_a_b(x):
    try:
        new_x = int(x)
    except ValueError:
        print("\n\033[91mПотрібно вводити число!\nПрограма завершила роботу.\033[0m")
        sys.exit()
    return new_x
