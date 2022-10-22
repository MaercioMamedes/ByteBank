from models.client import Client
from models.agency import Agency
from models.checking_account import CheckingAccount


class TestClass:
    def test_when_you_create_an_account_it_registers_inside_the_agency_class(self):
        client_nathalia = Client(1, 'Nathalia')
        agency = Agency(1)
        checking_account = CheckingAccount(client_nathalia, agency)
        expected = checking_account.checking_account_number

        result = agency.registered_accounts[expected].checking_account_number

        assert expected == result

