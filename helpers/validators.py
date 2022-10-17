from models.exceptions import OperationInvalid, InsuffcientBalance


def validator_integer(client_id, msg):
    if (not isinstance(client_id, int)) or (client_id == ''):
        raise ValueError(f'valor do atributo {msg} incorreto')


def verify_accounts(obj):
    print(dir(obj))


def validador_value(account, value, operation_type):
    operation = {
        'deposit': 'depósito',
        'withdraw': 'saque',
        'transfer': 'transferência',
    }

    try:
        if not (type(value) == int or type(value) == float):
            raise ValueError(f'valor para {operation[operation_type]} incorreto')
        elif value <= 0:
            raise OperationInvalid('value_negative')
        else:
            if operation_type == 'deposit':
                account.balance = value
            elif operation_type == 'withdraw':
                if account.balance >= value:
                    account.balance = -value
                else:
                    raise InsuffcientBalance
            elif operation_type == 'transfer':
                if account.balance >= value:
                    return True
                else:
                    raise InsuffcientBalance

    except ValueError as E:
        print(E)
    except OperationInvalid as E2:
        print(E2)
    except InsuffcientBalance as E3:
        print(E3)

    else:
        print('operação realizada com sucesso')
