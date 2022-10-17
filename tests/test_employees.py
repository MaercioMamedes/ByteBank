from models.employees import Employee


class TestClass:
    def test_when_age_receives_13_03_2000_must_return_22(self):
        input_data = '13/03/2000'
        expected = 22
        employee = Employee('Maercio', input_data, 1212)
        result = employee.age()

        assert result == expected

    def test_when_value_receive_1000_returns_100(self):
        input_data = 1000
        expected = 100
        employee = Employee('Maercio', '23/05/1991', input_data)
        result = employee.calculate_bonus()

        assert result == expected

    def test_when_name_receives_maercio_mamedes_returns_mamedes(self):
        input_data = 'Maercio Mamedes'
        expected = 'Mamedes'
        employee = Employee(input_data, '23/05/1991', 1000)
        result = employee.last_name()

        assert result == expected



