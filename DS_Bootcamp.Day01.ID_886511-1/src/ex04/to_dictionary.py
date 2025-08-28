def main():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    sorted_list = dict(sorted(list_of_tuples, key=lambda x: int(x[1])))
    for key, value in sorted_list.items():
        print(f"'{key}': '{value}'")

    #for country, number in sorted_list:
        #print(f"'{number}': '{country}'")

    '''number_to_countries = {}

    for country, number in list_of_tuples:
        if number not in number_to_countries:
            number_to_countries[number] = []
        number_to_countries[number].append(country)

    for number, countries in number_to_countries.items():
        print(f"'{number}': {countries}")

    #list_of_tuples = dict(list_of_tuples)
    #for key,value in list_of_tuples.items():
    #    print(key, value)
    #for tpl in list_of_tuples.items():
    #    print({*tpl}.__name__)
    '''

if __name__ == '__main__':
    main()
