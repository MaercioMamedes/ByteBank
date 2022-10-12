from validators import validator_integer


class Client:
    def __init__(self, client_id, name):
        self._id = None
        self._name = name

        validator_integer(client_id, 'ID do cliente')
        self._id = client_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name
