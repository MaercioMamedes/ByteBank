from models.agency import Agency
from models.client import Client
from models.checking_account import CheckingAccount


class TestClass:
    def test_when_deposit_50_balance_equals_balance_plus_50(self):
        client = Client(1, 'Maercio')
        agency = Agency(1)
        checking_account = CheckingAccount(client, agency)

        input_data = 50
        expected = checking_account.balance + 50
        checking_account.deposit(input_data)
        result = checking_account.balance

        assert result == expected

