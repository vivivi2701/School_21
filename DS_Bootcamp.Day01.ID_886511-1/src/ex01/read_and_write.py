def convert_csv_to_tsv():
    with open('../other_materials/ds.csv', 'r', encoding='utf-8') as infile, \
         open('ds.tsv', 'w', encoding='utf-8') as outfile:
        for line in infile:
            new_line = []
            inside_quotes = False
            for char in line:
                if char == '"' :
                    inside_quotes = not inside_quotes # перекл. состояние
                    new_line.append(char)
                elif char == ',' and not inside_quotes:
                    new_line.append('\t')  # замена запятой на табуляцию только если вне кавычек
                else:
                    new_line.append(char)
            outfile.write(''.join(new_line))

if __name__ == '__main__':
    convert_csv_to_tsv()
