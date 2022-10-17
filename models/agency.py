from datetime import datetime

"""Módulo de definição da classe Agency"""


class Agency:

    def __init__(self, id_agency):
        self._id_agency = id_agency
        self.registered_accounts = {}  # Atributo onde serão armazenadas todas as Classes CheckingAccount relacionadas

    def add_account(self, account):
        self.registered_accounts[account.id] = account

    @property
    def id_agency(self):
        return self._id_agency

    """Gerador de número de contas da classe CheckingAccount"""

    def creator_number_account(self):
        number = datetime.now().microsecond  # O número da conta será definido por esse método
        if number not in self.registered_accounts.keys():
            return number
        else:
            self.creator_number_account()
