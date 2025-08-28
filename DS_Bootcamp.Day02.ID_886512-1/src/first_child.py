import sys
import os
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise Exception("File not found")

        with open(self.path, 'r') as file:
            lines = file.readlines()

        if has_header and len(lines) < 2:
            raise Exception("File is too short or empty. Expected a header and at least one data line.")
        elif not lines:
            raise Exception("File is empty.")

        if has_header:
            lines = lines[1:]

        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            if len(parts) != 2:
                raise Exception(f"Incorrect data line format: '{line}'. Expected two values.")

            try:
                num1, num2 = int(parts[0]), int(parts[1])
                if not ((num1 == 0 and num2 == 1) or (num1 == 1 and num2 == 0)):
                    raise Exception(f"Incorrect data values in line: '{line}'. Expected '0,1' or '1,0'.")

                result.append([num1, num2])
            except ValueError:
                raise Exception(f"Data must be integers '0' or '1', found: '{line}'.")

        return result

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(1 for row in self.data if row[0] == 1)
            tails = sum(1 for row in self.data if row[0] == 0)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0.0, 0.0

            heads_fraction = (heads / total) * 100
            tails_fraction = (tails / total) * 100
            return heads_fraction, tails_fraction

class Analytics(Research.Calculations):
    def predict_random(self, num_of_steps):
        predictions = []
        for _ in range(num_of_steps):
            if randint(0, 1) == 0:
                predictions.append([0, 1])
            else:
                predictions.append([1, 0])
        return predictions

    def predict_last(self):
        if not self.data:
            return None
        return self.data[-1]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 first_child.py <file_path>. Pasiba")
        return

    file_path = sys.argv[1]
    try:
        research_instance = Research(file_path)
        data = research_instance.file_reader()

        print(data)

        analytics_instance = Analytics(data)

        heads, tails = analytics_instance.counts()
        print(heads, tails)

        heads_fraction, tails_fraction = analytics_instance.fractions(heads, tails)
        print(heads_fraction, tails_fraction)

        random_predictions = analytics_instance.predict_random(3)
        print(random_predictions)

        last_prediction = analytics_instance.predict_last()
        print(last_prediction)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
