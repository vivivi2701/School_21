#7709046585:AAGeu7jFiyrRjU9UUKPIpIBCwjpmn46uqa8
#582941991
import logging

NUM_OF_STEPS = 3
REPORT_TEMPLATE = """
    Report
    We have made {num_observations} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {tails_fraction:.2f}% and {heads_fraction:.2f}%, respectively. Our forecast is that in the next {num_of_steps} observations we will have: {tails_forecast} tail and {heads_forecast} heads.
"""
LOG_FILE = 'analytics.log'
LOG_FORMAT = '%(asctime)s %(message)s'
TELEGRAM_TOKEN = '7709046585:AAGeu7jFiyrRjU9UUKPIpIBCwjpmn46uqa8'
TELEGRAM_CHAT_ID = '582941991'
