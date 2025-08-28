import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 names_extractor.py <input_file>')
        return

    input_file = sys.argv[1]
    output_file = 'employees.tsv'

    with open(input_file, 'r', encoding='utf-8') as infile:
        emails = [line.strip() for line in infile if line.strip()]

    rows = []
    for email in emails:
        try:
            local, domain = email.split('@')
            first, last = local.split('.')
            first = first.capitalize()
            last = last.capitalize()
            rows.append((first, last, email))
        except ValueError:
            continue # пропускаем некоторые адреса

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("Name\tSurname\tE-mail\n")
        for row in rows:
            outfile.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")


if __name__ == '__main__':
    main()
