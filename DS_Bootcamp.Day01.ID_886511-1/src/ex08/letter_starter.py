import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 letter_starter.py <email>')
        return

    email = sys.argv[1]
    filename = 'employees.tsv'

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('Файл employees.tsv не найден.')
        return

    for line in lines[1:]:
        parts = line.strip().split('\t')
        if len(parts) == 3 and parts[2] == email:
            name = parts[0]
            print(f"Уважаемый {name}, добро пожаловать в нашу команду! Мы уверены, что Вам будет приятно работать с нами. Это обязательное условие дял специалистов, которых принимает на работу наша компания. Пасиба. ")
            return
        print('E-mail не найден в базе сотрудников. Пасиба.')

if __name__ == '__main__':
    main()
