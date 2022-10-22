from models.exceptions import OperationInvalid, InsuffcientBalance


class CheckingAccount:

    operation = {
        'deposit': 'depósito',
        'withdraw': 'saque',
        'transfer': 'transferência',
    }

    def __init__(self, client, agency):
        self._client = client
        self._checking_account_number = None
        self._agency = agency
        self._balance = 0

        self.__set_attributes(agency)
        self._agency.add_account(self)

    def __set_attributes(self, agency):
        account_number = agency.creator_number_account()
        self._checking_account_number = account_number

    def _validador(self, value, operation_type):

        if not (type(value) == int or type(value) == float):
            raise ValueError(f'valor para {self.operation[operation_type]} incorreto')

        elif value <= 0:
            raise OperationInvalid('value_negative')

        else:
            if operation_type == 'deposit':
                return True

            elif operation_type == 'withdraw':
                if self._balance >= value:
                    return True

                else:
                    raise InsuffcientBalance

            elif operation_type == 'transfer':
                if self._balance >= value:
                    return True

                else:
                    raise InsuffcientBalance

    def deposit(self,  value):
        # validador_value(self, value, 'deposit')
        operation_type = 'deposit'

        try:
            if self._validador(value, operation_type):
                self._balance += value

        except ValueError as E:
            print(E)
        except OperationInvalid as E2:
            print(E2)
        else:
            print('operação realizada com sucesso')

    def withdraw(self, value):
        operation_type = 'withdraw'

        try:
            if self._validador(value, operation_type):
                self._balance -= value

        except ValueError as E:
            print(E)
        except OperationInvalid as E2:
            print(E2)
        except InsuffcientBalance as E3:
            print(E3)
        else:
            print('operação realizada com sucesso')

    def transfer(self, favored, value):
        operation_type = 'transfer'

        try:
            if type(favored) == CheckingAccount:
                if favored.checking_account_number == self._checking_account_number and favored.agency == self._agency.id:
                    raise OperationInvalid('payer_equal_favored')
                elif self._validador(value, operation_type):
                    self._balance -= value
                    favored.balance += value
            else:
                raise ValueError("Conta do favorecido inválida")

        except ValueError as E:
            print(E)
        except OperationInvalid as E2:
            print(E2)
        except InsuffcientBalance as E3:
            print(E3)
        else:
            print('operação realizada com sucesso')

    def __str__(self):
        return f"cliente: {self._client}\nagência: {self._agency.id_agency}" \
               f"\nconta correte: {self._checking_account_number}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance += value

    @property
    def checking_account_number(self):
        return self._checking_account_number

    @property
    def agency(self):
        return self._agency.id_agency
