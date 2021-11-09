from payment_requests import PaymentRequests
from enum import IntEnum
from uuid import UUID
from uuid import uuid4

FILEPATH = "data/requests.txt"


def print_requests():
    r = open("data/requests.txt")
    for line in r:
        print(line, end='')


class Option(IntEnum):
    QUIT = 0
    ADD = 1
    DELETE = 2
    MODIFY = 3
    SORT = 4
    SEARCH = 5



def _add(requests: PaymentRequests) -> PaymentRequests:
    print(f"\033[93m{'-' * 7} Згенеровані ID (UUID) {'-' * 7}\033[0m")
    for i in range(5):
        print(uuid4())
    record_string = str(input("\033[93mВведіть ваш запис: \033[0m"))

    request = PaymentRequests.parse_request_from_string(record_string)
    requests.add(request)

    return requests


def _delete(requests: PaymentRequests) -> PaymentRequests:
    print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
    r = open("data/requests.txt")
    for line in r:
        print(line, end='')
    print(f"\033[93m{'-' * 98}\033[0m")
    record_uuid = UUID(str(input("\n\033[93mВведіть запис UUID: \033[0m")))

    requests.delete(record_uuid)

    return requests


def _modify(requests: PaymentRequests) -> PaymentRequests:
    print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
    r = open("data/requests.txt")
    for line in r:
        print(line, end='')
    print(f"\033[93m{'-' * 98}\033[0m")
    record_uuid = UUID(str(input("\n\033[93mВведіть запис UUID: \033[0m")))

    record_string = str(input("\n\033[93mВведіть оновлений запис: \033[0m"))
    request = PaymentRequests.parse_request_from_string(record_string)

    requests.modify(record_uuid, request)

    return requests


def _sort(requests: PaymentRequests) -> PaymentRequests:
    field = str(input("\033[93mВведіть поле для сортування: \033[0m"))

    requests.sort(field)

    return requests


def _search(requests: PaymentRequests) -> PaymentRequests:
    keyword = str(input("\033[93mВведіть ключове слово: \033[0m"))

    results = requests.search(keyword)
    for result in results.requests:
        print(result.__str__())

    return requests


def menu(requests):
    print("\n\033[93mВиберіть операцію:\033[0m")
    print("\033[96m1. Додати нову оплату\033[0m")
    print("\033[96m2. Видалити оплату за допомогою UUID\033[0m")
    print("\033[96m3. Змінити існуючу оплату\033[0m")
    print("\033[96m4. Сортувати за полем\033[0m")
    print("\033[96m5. Пошук за значенням\033[0m")
    print("\033[96m6. Вивести список\033[0m")
    print()
    print("\033[91m0. Вихід з програми\033[0m")

    option = int(input())
    if option == Option.ADD:
        return _add(requests), False
    elif option == Option.DELETE:
        return _delete(requests), False
    elif option == Option.MODIFY:
        return _modify(requests), False
    elif option == Option.QUIT:
        return requests, True
    elif option == Option.SORT:
        return _sort(requests), False
    elif option == Option.SEARCH:
        return _search(requests), False
    elif option == 6:
        print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
        print_requests()
        print(f"\033[93m{'-' * 98}\033[0m")
        return requests, False
    else:
        print("\033[91mВиберіть коректний варіант!\n\033[0m")
        return requests, False


if __name__ == "__main__":
    requests = PaymentRequests([])
    requests.read_from_file(FILEPATH)

    while True:
        try:
            requests, exit = menu(requests)
            requests.write_to_file(FILEPATH)
        except Exception as e:
            print(e)

        if exit:
            break

    print("\033[91mПрограма завершила роботу.\033[0m")
