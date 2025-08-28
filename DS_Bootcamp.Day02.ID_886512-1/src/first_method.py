class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            content = file.read()
        return content

def main():
    research = Research()
    file_content = research.file_reader()
    print(file_content)
if __name__ == '__main__':
    main()
