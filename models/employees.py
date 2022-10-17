from datetime import date


class Employee:
    def __init__(self, name, birth_date, wage):
        self._name = name.strip()
        self._birth_date = birth_date
        self._wage = wage

    @property
    def name(self):
        return self._name

    @property
    def wage(self):
        return self._wage

    def last_name(self):
        full_name = self._name.split()
        return full_name[-1]

    def age(self):
        current_year = date.today().year
        birth_year = self._birth_date.split('/')[-1]
        return current_year - int(birth_year)

    def calculate_bonus(self):
        value = self._wage * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self):
        return f'Funcionario({self._name}, {self._birth_date}, {self._wage})'
