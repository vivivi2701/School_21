class Must_read:
    with open('data.csv', 'r') as file:
        content = file.read()
        print(content)

if __name__ == '__main__':
    Must_read()
