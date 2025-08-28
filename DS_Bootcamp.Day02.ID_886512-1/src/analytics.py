import os
from random import randint
import logging
import requests

logging.basicConfig(
    filename='analytics.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

class Research:
    def __init__(self, path):
        logging.info(f"Research instance created with path: {path}")
        self.path = path

    def file_reader(self, has_header=True):
        logging.info("Starting file_reader method...")
        if not os.path.exists(self.path):
            logging.error("File not found")
            raise Exception("File not found")

        with open(self.path, 'r') as file:
            lines = file.readlines()

        if has_header and len(lines) < 2:
            logging.error("File is too short or empty.")
            raise Exception("File is too short or empty. Expected a header and at least one data line.")
        elif not lines:
            logging.error("File is empty.")
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
                logging.error(f"Incorrect data line format: '{line}'.")
                raise Exception(f"Incorrect data line format: '{line}'. Expected two values.")

            try:
                num1, num2 = int(parts[0]), int(parts[1])
                if not ((num1 == 0 and num2 == 1) or (num1 == 1 and num2 == 0)):
                    logging.error(f"Incorrect data values in line: '{line}'.")
                    raise Exception(f"Incorrect data values in line: '{line}'. Expected '0,1' or '1,0'.")

                result.append([num1, num2])
            except ValueError:
                logging.error(f"Data must be integers '0' or '1', found: '{line}'.")
                raise Exception(f"Data must be integers '0' or '1', found: '{line}'.")

        logging.info("File read successfully.")
        return result

    class Calculations:
        def __init__(self, data):
            logging.info("Calculations instance created.")
            self.data = data

        def counts(self):
            logging.info("Calculating the counts of heads and tails.")
            heads = sum(1 for row in self.data if row[0] == 1)
            tails = sum(1 for row in self.data if row[0] == 0)
            logging.info(f"Counts calculated: heads={heads}, tails={tails}")
            return heads, tails

        def fractions(self, heads, tails):
            logging.info("Calculating fractions.")
            total = heads + tails
            if total == 0:
                logging.warning("Total observations is 0. Returning 0.0 fractions.")
                return 0.0, 0.0

            heads_fraction = (heads / total) * 100
            tails_fraction = (tails / total) * 100
            logging.info(f"Fractions calculated: heads_fraction={heads_fraction}, tails_fraction={tails_fraction}")
            return heads_fraction, tails_fraction

class Analytics(Research.Calculations):
    def predict_random(self, num_of_steps):
        logging.info(f"Predicting random results for {num_of_steps} steps.")
        predictions = []
        for _ in range(num_of_steps):
            if randint(0, 1) == 0:
                predictions.append([0, 1])
            else:
                predictions.append([1, 0])
        logging.info(f"Random predictions generated: {predictions}")
        return predictions

    def predict_last(self):
        logging.info("Returning the last observation.")
        if not self.data:
            logging.warning("Data is empty. Cannot predict last observation.")
            return None
        last_item = self.data[-1]
        logging.info(f"Last observation returned: {last_item}")
        return last_item

    def save_file(self, data, filename, extension):
        logging.info(f"Attempting to save report to {filename}.{extension}.")
        try:
            full_path = f"{filename}.{extension}"
            with open(full_path, 'w') as f:
                f.write(data)
            logging.info(f"Report successfully saved to {full_path}.")
        except Exception as e:
            logging.error(f"Failed to save report: {e}")
            raise Exception(f"Failed to save report: {e}")

    def send_telegram_message(self, message):
        from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

        try:
            response = requests.post(url, json={'chat_id': TELEGRAM_CHAT_ID, 'text': message})
            response.raise_for_status()
            logging.info("Telegram message sent successfully.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send Telegram message: {e}")
            raise Exception(f"Failed to send Telegram message: {e}")
