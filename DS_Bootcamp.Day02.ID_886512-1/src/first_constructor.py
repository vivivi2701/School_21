import sys
import os
class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if not os.path.exists(self.path):
            raise Exception("File not found")

        with open(self.path, 'r') as file:
            lines = file.readlines()

        if len(lines) < 2:
            raise Exception("File is too short or empty")

        header = lines[0].strip().split(',')
        if len(header) != 2:
            raise Exception("Incorrect header format")

        data_lines = lines[1:]
        for line_num, line in enumerate(data_lines, 2):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                raise Exception(f"Incorrect data format in line {line_num}: '{line}'. Expected two values.")
            if not (parts[0] in ['0', '1'] and parts[1] in ['0', '1']):
                raise Exception(f"Incorrect data values in line {line_num}: '{line}'. Expected '0' or '1'.")
            if parts[0] == parts[1]:
                 raise Exception(f"Incorrect data values in line {line_num}: '{line}'. Values cannot be the same.")
        return "".join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <file_path>. Pasiba.")
        return
    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        file_content = research.file_reader()
        print(file_content, end='')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
