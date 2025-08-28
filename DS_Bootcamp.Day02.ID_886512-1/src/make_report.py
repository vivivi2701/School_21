import sys
from analytics import Research, Analytics
from config import NUM_OF_STEPS, REPORT_TEMPLATE
import logging
import os
#python3 make report.py data.csv
def make_forecast_report(predictions):
    heads_forecast = sum(1 for pred in predictions if pred[0] == 1)
    tails_forecast = sum(1 for pred in predictions if pred[0] == 0)
    return heads_forecast, tails_forecast

def main():
    logging.basicConfig(
        filename='analytics.log',
        level=logging.INFO,
        format='%(asctime)s %(message)s'
    )
    logging.info("Program started.")

    if len(sys.argv) != 2:
        logging.warning("Incorrect number of command-line arguments.")
        print("Usage: python3 make_report.py <file_path>.Pasiba.")
        return

    file_path = sys.argv[1]
    try:
        research = Research(file_path)
        data = research.file_reader()

        analytics = Analytics(data)
        heads, tails = analytics.counts()
        heads_fraction, tails_fraction = analytics.fractions(heads, tails)

        predictions = analytics.predict_random(NUM_OF_STEPS)
        heads_forecast, tails_forecast = make_forecast_report(predictions)

        report = REPORT_TEMPLATE.format(
            num_observations=len(data),
            tails=tails,
            heads=heads,
            tails_fraction=heads_fraction,
            heads_fraction=tails_fraction,
            num_of_steps=NUM_OF_STEPS,
            tails_forecast=tails_forecast,
            heads_forecast=heads_forecast
        )

        analytics.save_file(report, 'report', 'txt')
        analytics.send_telegram_message("The report has been successfully created.")
        logging.info("Program finished successfully.")

    except Exception as e:
        logging.error(f"An unhandled error occurred: {e}", exc_info=True)
        try:
            analytics.send_telegram_message("The report hasn’t been created due to an error.")
        except Exception as telegram_e:
            logging.error(f"Failed to send error message to Telegram: {telegram_e}")
        print(f"Error: {e}")
    finally:
        logging.info("Program execution finished.")

if __name__ == '__main__':
    main()
