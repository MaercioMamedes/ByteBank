from models.agency import Agency
from models.client import Client
from models.checking_account import CheckingAccount
import pytest


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

    def test_when_user_maercio_transfers_50_to_user_nathalia_balance_maercio_equals_minus_50_and_balance_nathalia_equals_plus_50(self):
        client_maercio = Client(1, 'Maercio')
        client_nathalia = Client(2, 'Nathalia')
        agency = Agency(1)
        account_maercio = CheckingAccount(client_maercio, agency)
        account_nathalia = CheckingAccount(client_nathalia, agency)

        input_value_transfer = 50
        account_maercio.deposit(input_value_transfer)
        balance_expected_nathalia = 50
        balance_expected_maercio = 0
        account_maercio.transfer(account_nathalia, input_value_transfer)

        assert (account_nathalia.balance, account_maercio.balance) == (balance_expected_nathalia, balance_expected_maercio)
