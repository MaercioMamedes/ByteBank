class InsuffcientBalance(Exception):
    message_default: str = "saldo insuficiente para operação"

    def __init__(self, message_user=""):
        self.message: str = message_user or self.message_default

        super(InsuffcientBalance, self).__init__(self.message)


class WithdrawValueError(Exception):
    pass


class OperationInvalid(Exception):
    operations: dict = {
        'value_negative': 'O valor da operação não pode ser negativo ou nulo',
        'payer_equal_favored': 'O favorecido não pode ser igual ao pagador',
    }

    def __init__(self, operation):
        super(OperationInvalid, self).__init__(self.operations[operation])
