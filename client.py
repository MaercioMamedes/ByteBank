from validators import validator_integer


class Client:
    def __init__(self, client_id, name):
        validator_integer(client_id, 'ID do cliente')
        self._name: str = name
        self._id: int = client_id

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return self._name
