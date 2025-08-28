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

    if len(sys.argv) != 2:
        return

    input_str = sys.argv[1]

    if ',,' in input_str or ', ,' in input_str or ',  ' in input_str:
        return
    #  это проверка на двойные запятые или запятые с пробелом между ними - ничего не выводим

    parts = input_str.split(',') # разбиваем по запятой

    for part in parts:
        if part.strip() == '':
            return # пустой эл-т после удаления пробелов- ничего не выводим

    for expr in parts:
        expr_clean = expr.strip()
        expr_lower = expr_clean.lower()

        #яв-ся ли expr названием компании
        company_match = None
        for company in COMPANIES:
            if company.lower() == expr_lower:
                company_match = company
                break

        #яв-ся ли expr тикером
        ticker_match = None
        for ticker in STOCKS:
            if ticker.lower() == expr_lower:
                ticker_match = ticker
                break

        if ticker_match:
            company_name = None
            for comp, tick in COMPANIES.items():
                if tick.lower() == ticker_match.lower():
                    company_name = comp
                    break
            print(f"{ticker_match.upper()} is a ticker symbol for {company_name}")
        elif company_match:
            ticker = COMPANIES[company_match]
            price = STOCKS.get(ticker)
            print(f"{company_match} stock price is {price}")
        else:
            print(f"{expr_clean} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    main()
