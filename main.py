from client import Client
from agency import Agency
from checking_account import CheckingAccount

if __name__ == '__main__':
    client1 = Client(1, 'Maercio')
    agency = Agency(1)
    account = CheckingAccount(client1, agency)

    breakpoint()

