from dataclasses import dataclass
from typing import List
from uuid import UUID
from payment_request import Currency, PaymentRequest, TransactionID
from datetime import datetime

@dataclass
class PaymentRequests:
    requests: List[PaymentRequest]

    def write_to_file(self, filename: str):
        with open(filename, 'w') as file:
            for request in self.requests:
                file.write(request.__str__() + "\n")


    @staticmethod
    def parse_request_from_string(req_string: str):
        params = req_string.split()

        return PaymentRequest(
                        id=UUID(params[0]),
                        payer_email=params[1],
                        amount=float(params[2]),
                        currency=Currency.from_string(params[3]),
                        payment_request_date=datetime.strptime(params[4], "%d/%m/%Y").date(),
                        payment_due_to_date=datetime.strptime(params[5], "%d/%m/%Y").date(),
                        transaction_id=TransactionID(params[6].split('-')[0], params[6].split('-')[1])
                    )


    def read_from_file(self, filename: str):
        with open(filename) as file:
            for line in file.readlines():
                self.requests.append(
                    self.parse_request_from_string(line)
                )

    def search(self, term: str):
        return PaymentRequests(list(filter(lambda request: term in request.__repr__(), self.requests)))

    def sort(self, field: str):
        self.requests = sorted(self.requests,
        key=lambda request: request.__getattribute__(field).lower() if type(request.__getattribute__(field)) == str else request.__getattribute__(field))

    def delete(self, request_id: UUID):
        self.requests = list(filter(lambda request: request.id != request_id, self.requests))

    def add(self, new_request: PaymentRequest):
        self.requests.append(new_request)

    def modify(self, request_id: UUID, updated_request: PaymentRequest):
        self.delete(request_id)
        self.add(updated_request)
