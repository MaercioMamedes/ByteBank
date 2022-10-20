from models.agency import Agency
from models.client import Client
from models.checking_account import CheckingAccount
import pytest
from models.exceptions import InsuffcientBalance


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

    def test_when_withdraw_50_balance_equals_30(self):
        client = Client(1, 'Maercio')
        agency = Agency(1)
        checking_account = CheckingAccount(client, agency)
        checking_account.deposit(80)

        input_data = 50
        expected = checking_account.balance - input_data
        checking_account.withdraw(50)
        result = checking_account.balance

        assert result == expected

    def test_when_withdraw_greater_than_balance_returns_insufficient_balance_error(self):
        with pytest.raises(Exception):
            client = Client(1, 'Maercio')
            agency = Agency(1)
            checking_account = CheckingAccount(client, agency)
            # initial balance equal a zero
            input_value_withdraw = 50

            assert checking_account.withdraw(input_value_withdraw)

