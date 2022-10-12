from client import *
from agency import *
from checking_account import *

if __name__ == '__main__':
    client1 = Client(1, 'Maercio')
    agency = Agency(1)
    account = CheckingAccount(client1, agency)

    breakpoint()

