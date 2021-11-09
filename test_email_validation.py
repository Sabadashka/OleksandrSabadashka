from payment_request_validator import PaymentRequestValidator

if __name__ == "__main__":
    valid_email = "bill.gates@gmail.com"
    invalid_email = "billiWilly"

    assert(PaymentRequestValidator.email_validate(valid_email))
    assert(not PaymentRequestValidator.email_validate(invalid_email))