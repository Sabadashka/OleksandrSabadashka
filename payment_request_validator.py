import re
from typing import Any, Union, Tuple


class PaymentRequestValidator:
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    @staticmethod
    def regex_validate(data: str, regex: Union[str, re.Pattern]):
        pattern = regex

        if type(pattern) == str:
            pattern = re.compile(pattern)

        return bool(pattern.fullmatch(data))

    @staticmethod
    def email_validate(email: str):
        return PaymentRequestValidator.regex_validate(
            email,
            PaymentRequestValidator.email_pattern
        )

    @staticmethod
    def range_validate(data: Any, rng: Tuple[Any, Any]):
        return data >= rng[0] and data <= rng[1]
