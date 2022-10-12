from datetime import datetime


class Agency:

    def __init__(self, id_agency):
        self._id_agency = id_agency
        self.registered_accounts = {}

    def add_account(self, account):
        self.registered_accounts[account.id] = account

    @property
    def id_agency(self):
        return self._id_agency

    def creator_number_account(self):
        number = datetime.now().microsecond
        if number not in self.registered_accounts.keys():
            return number
        else:
            self.creator_number_account()
