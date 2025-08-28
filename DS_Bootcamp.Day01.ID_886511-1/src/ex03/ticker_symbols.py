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
    input_arg = sys.argv[1].upper() #.title() # чтобы даже tesla читалась как Tesla - личное нововведение
      # print(sys.argv[0]) - выведется название скрипта
    #company_name = COMPANIES.get(company_name)
    #print(company_name)
    # Прроверчем, есть ли компания  в словаре
    if input_arg in COMPANIES:
        ticker = COMPANIES[input_arg]
        price = STOCKS.get(ticker)
        if price is not None:
            print(price)
        else:
            print('Неизвестная компания')
        return
    company_name = None
    for company, ticker in COMPANIES.items():
        if ticker == input_arg:
            company_name = company
            break

    if company_name:
        price = STOCKS.get(input_arg)
        if price is not None:
            print(f"{company_name} {price}")

        else:
            print('Неизвестная компания')

    else:
        print('Неизвестная компания')

if __name__ == '__main__':
    main()
