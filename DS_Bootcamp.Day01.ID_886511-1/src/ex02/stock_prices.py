import sys

def main():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # sys.argv[0] - имя скрипта, аргументы нач-ся с sys.argv[1]
    if len(sys.argv) != 2:
        #нет аргументов или их больге одного- ничего не выводим
        return

    company_name = sys.argv[1].title() # чтобы даже tesla читалась как Tesla - личное нововведение
      # print(sys.argv[0]) - выведется название скрипта

    # Прроверчем, есть ли компания  в словаре
    if company_name in COMPANIES:
        ticker = COMPANIES[company_name]
        price = STOCKS.get(ticker)
        if price is not None:
            print(price)
        else:
            # на случай если тикер не нйден в STOCKS (что маловероятно)
            print('Неизвестная компания')
    else:
        print('Неизвестная компания')

if __name__ == '__main__':
    main()
