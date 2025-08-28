import sys

def get_call_center(clients, recipients):
    return list(set(clients) - set(recipients))

def get_potential_clients(participants, clients):
    return list(set(participants) - set(clients))

def get_loyalty_program(clients, participants):
    return list(set(clients) - set(participants))

def main():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
        ]

    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com'
        ]

    recipients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'
        ]
    #new_clients = set()
    #new_participants = set()
    #new_recipients = set()

    if len(sys.argv) != 2:
        raise Exception('Неверное кол-во аргументов')

    task = sys.argv[1].lower()

    if task == 'call_center':
        print(get_call_center(clients, recipients))
    elif task == 'potential_clients':
        print(get_potential_clients(participants, clients))
    elif task == 'loyalty_program':
        print(get_loyalty_program(clients, participants))
    else:
        raise Exception('Неизвестное имя задачи')

if __name__ == '__main__':
    main()
