import re
from datetime import *

class ExceptionPayment(Exception) :
    def __init__(self, message: str = ''):
        self.message = message

    def __str__(self) -> str:
        return self.message


def decoratorValidate(validate):
    def decorator(*args, **kwargs):
        try:
            validate(*args, **kwargs)
            return True
        except ValueError as message:
            raise ExceptionPayment("ПОМИЛКА перевірки " + str(args[1]) + ": " + str(message))
    return decorator


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def validate_is_str(key, value):
        if type(value) is not str:
            raise ValueError(key + " must be string")


    def validate_file(self, key, value):
        self.validate_is_str(key, value)

        if value.endswith('.txt') is not True:
            raise ValueError(value + "\033[91m має бути у форматі txt\033[0m")
        return True


    @staticmethod
    def validate_PAYMENT(key, item):
        Validation.validate_ID(lambda value : value)
        Validation.validate_amount(lambda value : value)
        Validation.validate_currency(lambda value : value)
        Validation.validate_email(lambda value : value)
        Validation.validate_transactionID(lambda value : value)
        Validation.validate_date(lambda value : value)
        Validation.validate_date(lambda value : value)


    @staticmethod
    def validate_ID(function):
        def decorator(*args, **kwargs):
            if type(args[1]) is int:
                if args[1] < 0 or args[1] > 999999:
                    raise ValueError("ID має бути не менше 0 і не більше 999999")
            Validation.validate_is_str("ID", str(args[1]))

            if not re.fullmatch(r'[0-9]{1,6}', str(args[1])):
                raise ValueError("ID повинен містити лише 1-6 цифр")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_amount(function):
        def decorator(*args, **kwargs):
            if type(args[1]) is int:
                if args[1] < 0 or args[1] > 999999:
                    raise ValueError("Сума має бути не менше 0 і не більше 999999")
            Validation.validate_is_str("Amount", str(args[1]))

            if not re.fullmatch(r'[0-9]{1,6}', str(args[1])):
                raise ValueError("Сума повинна містити лише 1-6 цифр")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_currency(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Date", str(args[1]))
            if args[1] != "usd" and args[1] != "eur" and args[1] != "uah":
                raise ValueError("Валюта має бути тільки usd/eur/uah")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_date(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Date", str(args[1]))
            [dd, mm, yyyy] = str(args[1]).split('.')
            day, month, year = int(dd), int(mm), int(yyyy)
            try:
                value = date(year, month, day)
            except ValueError:
                raise ValueError("Дата має бути в такому форматі: dd-mm-yyyy")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_two_dates(date1, date2):
        [d1, m1, y1] = str(date1).split('.')
        [d2, m2, y2] = str(date2).split('.')
        day, month, year = int(d1), int(m1), int(y1)
        _date1 = date(year, month, day)
        day, month, year = int(d2), int(m2), int(y2)
        _date2 = date(year, month, day)
        if _date1 > _date2:
            raise ExceptionPayment("'Due to date' не може бути пізніше ніж 'request to date'")


    @staticmethod
    def validate_email(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Payer email", str(args[1]))
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(args[1])):
                raise ValueError("Некоректна адреса")
            function(*args, **kwargs)
        return decorator


    @staticmethod
    def validate_transactionID(function):
        def decorator(*args, **kwargs):
            Validation.validate_is_str("Transaction ID", str(args[1]))
            if not re.fullmatch(r'\d{8}-\d{2}', str(args[1])):
                raise ValueError("Transaction ID має бути у форматі: ********-** і містити лише цифри")
            function(*args, **kwargs)
        return decorator