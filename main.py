from list import *
from validation import validation, validation_for_a_b
import sys


def menu_message():
    print(f"\033[93m{'-' * 30}\033[0m")
    print("\033[95m1. Згенерувати рандомний список від a до b\033[0m")
    print("\033[95m2. Ввести свій список\033[0m")
    print("\033[95m3. Додати на К позицію\033[0m")
    print("\033[95m4. Видалити з К позиції\033[0m")
    print("\033[95m5. Моє завдання (17)\033[0m")
    print("\033[95m6. Вивести список\033[0m")
    print("\033[95m7. Генератор\033[0m")
    print("\033[95m8. Ітератор\033[0m")
    print("\033[91m\n10. Вихід\033[0m")
    print(f"\033[93m{'-' * 30}\033[0m")



def menu():
    llist = SLinkedList()
    c = input()

    while c != "10":
        if c == "1":
            n = input("\033[32mВведіть n: \033[0m")
            n = validation(n)

            a = input("\033[32mВведіть а: \033[0m")
            a = validation_for_a_b(a)

            b = input("\033[32mВведіть b: \033[0m")
            b = validation_for_a_b(b)
            while a > b:
                print("\033[91mb повинне бути більшим за a\033[0m")
                b = input("\033[32mВведіть b: \033[0m")
                b = validation_for_a_b(b)
            llist.Generate(a, b, n)
            print(f"\033[93m{'-' * 15}\033[0m")
            llist.LListprint()
            print("\033[32mOK\033[0m")
            menu_message()

        elif c == "2":
            n = input("\033[32mВведіть n: \033[0m")
            n = validation(n)

            llist.EnterFromKeyboard(n)
            print(f"\033[93m{'-' * 15}\033[0m")
            llist.LListprint()
            print("\033[32mOK\033[0m")
            menu_message()
        elif c == "3":

            if llist.head is None:
                sys.exit("Список пустий. Програма завершила роботу.")
            llist.LListprint()
            k = input("\033[32mВведіть K: \033[0m")
            k = validation(k)

            data = input("\033[32mВведіть число: \033[0m")
            data = validation_for_a_b(data)

            llist.push_at(data, k)
            llist.LListprint()
            menu_message()

        elif c == "4":
            if llist.head is None:
                sys.exit("Список пустий. Програма завершила роботу.")
            llist.LListprint()
            k = input("\033[32mВведіть K: \033[0m")
            k = validation(k)

            llist.DeleteNode(k)
            llist.LListprint()
            menu_message()
        elif c == "5":
            # Визначити чи є його елементи по зростанню, якщо так, то суму різниць добутку сусідніх елементів, якщо ні, то обчислити суму додатніх
            llist.isSorted()
            menu_message()
        elif c == "6":
            llist.LListprint()
            menu_message()

        elif c == "7":
            n = input("\033[35mВведіть n: \033[0m")
            n = validation(n)
            a = input("\033[32mВведіть a: \033[0m")
            a = validation_for_a_b(a)
            b = input("\033[32mВведіть b: \033[0m")
            b = validation_for_a_b(b)
            while a > b:
                print("\033[91mb повинне бути більшим за a\033[0m")
                b = input("\033[32mВведіть b: \033[0m")
                b = validation_for_a_b(b)
            z = llist.add_rand_elem(n, range(a, b))
            llist.LListprint()
            menu_message()
        elif c == "8":
            for i in llist:
                print(i)
            menu_message()
        else:
            print("\033[91mВиберіть коректний варіант!\033[0m")
            menu_message()
        c = input()
    sys.exit("Програма завершила роботу")


if __name__ == '__main__':
    menu_message()
    menu()
