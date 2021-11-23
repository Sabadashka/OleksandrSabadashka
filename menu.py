from Validation import ExceptionPayment
from Payment_Request import PAYMENT_REQUEST
from Container_PaymentRequest import ContainerPAYMENT_REQUEST


def menu():
    action = input("\033[93mВиберіть операцію:\033[0m\n"
                   + "\033[96m1. Вивести список\033[0m\n"
                   + "\033[96m2. Пошук за значенням\033[0m\n"
                   + "\033[96m3. Сортувати за полем\033[0m\n"
                   + "\033[96m4. Видалити оплату за допомогою ID\033[0m\n"
                   + "\033[96m5. Додати нову оплату\033[0m\n"
                   + "\033[96m6. Змінити існуючу оплату\033[0m\n\n"
                   + "\033[91m7. Вихід з програми\033[0m\n")
    return action


def main():
    while True:
        try:
            container = read_in_container()
            break
        except ValueError as message:
            print(str(message))
            continue
        except FileNotFoundError:
            print("\033[91mФайл не знайдено\033[0m")
            continue

    dictionaryActions = {"1": print_container, "2": search_in_container, "3": sort_container,
                         "4": delete_from_container, "5": add_to_container, "6": edit_attribute_container}

    while True:
        try:
            action = menu()
            if action == "7":
                break
            else:
                dictionaryActions[action](container)
        except KeyError:
            print("Відсутній ключ. Cпробуйте ще раз")
        except (ValueError, ExceptionPayment) as message:
            print(str(message) + "\nСпробуйте ще раз")


def read_in_container():
    filename = input("\033[94mВведіть назву файла: \033[0m")
    _container = ContainerPAYMENT_REQUEST(filename)
    _container.read_from_file(filename)
    return _container


def print_container(container):
    print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
    print(container)


def search_in_container(container):
    attr = input("\033[93mВведіть значення для пошуку: \033[0m")
    array = container.search_in_container(attr)
    if len(array) > 0: print("\033[93mЗнайдено платежі:\n\n\033[0m" + str(array))


def sort_container(container):
    attr = input("\033[93mВиберіть варіант сортування:\033[0m\n" +
                 "\033[96m  1. ID\n\033[0m" +
                 "\033[96m  2. Cума\n\033[0m" +
                 "\033[96m  3. Валюта\n\033[0m" +
                 "\033[96m  4. Електронна пошта\n\033[0m" +
                 "\033[96m  5. Дата запиту(від)\n\033[0m" +
                 "\033[96m  6. Дата запиту(до)\n\033[0m" +
                 "\033[96m  7. Transaction id\n\033[0m")
    container.sort(attr)


def delete_from_container(container):
    print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
    print(container)
    id = input("\n\033[93mВведіть запис ID: \033[0m")
    container.delete(id)


def add_to_container(container):
    id = input("\033[93mВведіть ID: \033[0m")
    amount = input("\033[93mВведіть суму: \033[0m")
    currency = input("\033[93mВведіть валюту (usd/eur/uah): \033[0m")
    email = input("\033[93mВведіть пошту: \033[0m")
    transaction_id = input("\033[93mВведіть ідентифікатор транзакції: \033[0m")
    request_date = input("\033[93mВведіть дату(від): \033[0m")
    due_to_date = input("\033[93mВведіть дату(до): \033[0m")

    payment = PAYMENT_REQUEST(id, amount, currency, email, transaction_id, request_date, due_to_date)
    container.append(payment)


def edit_attribute_container(container):
    print(f"\033[93m{'-' * 45} Cписок {'-' * 45}\033[0m")
    print(container)
    id = input("\n\033[93mВведіть запис ID: \033[0m")
    attr = input("\033[93mВиберіть варіант:\033[0m\n" +
                 "\033[96m  1. ID\n\033[0m" +
                 "\033[96m  2. Cума\n\033[0m" +
                 "\033[96m  3. Валюта\n\033[0m" +
                 "\033[96m  4. Електронна пошта\n\033[0m" +
                 "\033[96m  5. Дата запиту(від)\n\033[0m" +
                 "\033[96m  6. Дата запиту(до)\n\033[0m" +
                 "\033[96m  7. Transaction id\n\033[0m")
    value = input("Введіть нове значення: ")
    container.edit(id, attr, value)


main()
