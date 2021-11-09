from dataclasses import dataclass

from datetime import date, datetime
from uuid import uuid4, UUID
from enum import IntEnum, auto
from payment_request_validator import PaymentRequestValidator


class Currency(IntEnum):
    USD = auto()
    EUR = auto()
    UAH = auto()

    def __str__(self) -> str:
        return 'usd' if self.value == Currency.USD else 'eur' if self.value == Currency.EUR else 'uah'

    @staticmethod
    def from_string(curr: str):
        if curr == 'usd':
            return Currency.USD
        elif curr == 'eur':
            return Currency.EUR
        else:
            return Currency.UAH


@dataclass
class TransactionID:
    clver: str
    clend: str

    def validate(self):
        return all(ch.isdigit() for ch in self.clver) and \
               all(ch.isdigit() for ch in self.clend) and \
               len(self.clver) == 8 and len(self.clend) == 2

    def __post_init__(self):
        if not self.validate():
            raise ValueError("Invalid transaction id.")

    def __str__(self):
        return f'{self.clver}-{self.clend}'


@dataclass
class PaymentRequest:
    payer_email: str
    amount: float
    currency: Currency
    payment_request_date: date
    payment_due_to_date: date
    transaction_id: TransactionID

    id: UUID = ""

    def __str__(self) -> str:
        return f'{self.id} {self.payer_email} {self.amount} {self.currency.__str__()} ' + \
               f'{self.payment_request_date.strftime("%d/%m/%Y")} {self.payment_due_to_date.strftime("%d/%m/%Y")} ' + \
               f"{self.transaction_id}"

    def validate(self):
        if not PaymentRequestValidator.email_validate(self.payer_email): return False
        if not PaymentRequestValidator.range_validate(self.amount, (0, 3e6)): return False
        if self.payment_request_date >= self.payment_due_to_date: return False
        if self.payment_request_date > datetime.now().date(): return False

        return True

    def __post_init__(self):
        if not self.validate():
            raise ValueError(f"Invalid payment request object `{self.__str__}`.")

        if not self.id:
            self.id = uuid4()