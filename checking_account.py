from validators import validator_integer, validador_value


class CheckingAccount:

    def __init__(self, client, agency):
        self._client = client
        self._checking_account_number = None
        self._agency = agency
        self._balance = 0

        self.__set_attributes(agency)
        self._agency.registered_accounts[self._checking_account_number] = self

    def __set_attributes(self, agency):
        account_number = agency.creator_number_account()
        validator_integer(account_number, 'Número da conta')
        self._checking_account_number = account_number

    def deposit(self,  value):
        validador_value(self, value, 'deposit')

    def withdraw(self, value):
        validador_value(self, value, 'withdraw')

    def __str__(self):
        return f"cliente: {self._client}\nagência: {self._agency.id_agency}" \
               f"\nconta correte: {self._checking_account_number}"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance += value
