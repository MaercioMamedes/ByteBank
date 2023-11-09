from validators import validator_integer, validador_value
from exceptions import OperationInvalid


class CheckingAccount:

    def __init__(self, client, agency):
        self._client: Client = client
        self._checking_account_number: int = 0
        self._agency: Agency = agency
        self._balance: float = 0.0

        self.__set_attributes(agency)
        self._agency.registered_accounts[self._checking_account_number] = self

    def __set_attributes(self, agency) -> None:
        account_number = agency.creator_number_account()
        validator_integer(account_number, 'Número da conta')
        self._checking_account_number = account_number

    def deposit(self,  value) -> None:
        validador_value(self, value, 'deposit')

    def withdraw(self, value) -> None:
        validador_value(self, value, 'withdraw')

    def transfer(self, favored, value) -> None:
        if favored.checking_account_number == self._checking_account_number and favored.agency.id == self._agency.id:
            raise OperationInvalid('payer_equal_favored')

        if validador_value(self, value, 'transfer'):
            self._balance -= value
            favored.balance += value

    def __str__(self) -> str:
        return f"cliente: {self._client}\nagência: {self._agency.id_agency}" \
               f"\nconta correte: {self._checking_account_number}"

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value) -> None:
        self._balance += value

    @property
    def checking_account_number(self) -> int:
        return self._checking_account_number
