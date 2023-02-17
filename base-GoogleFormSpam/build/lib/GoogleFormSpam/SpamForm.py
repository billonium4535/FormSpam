import datetime
import requests
import random
import time
import multiprocessing


class SpamForm:
    def __init__(self, url, responses, realism_delay=False, threads=10):
        self.url = url
        self.responses = responses
        self.realism_delay = realism_delay
        self.threads = threads
        self.output_data = {}

    def shortAnswer(self, entry_number, data):
        self.output_data["entry.{}".format(entry_number)] = data

    def paragraph(self, entry_number, data):
        self.output_data["entry.{}".format(entry_number)] = data

    def multipleChoice(self, entry_number, option_name):
        self.output_data["entry.{}".format(entry_number)] = option_name

    def checkbox(self, entry_number, *option_names):
        self.output_data["entry.{}".format(entry_number)] = option_names

    def dropdown(self, entry_number, option_name):
        self.output_data["entry.{}".format(entry_number)] = option_name

    def sendForm(self, output=True, min_delay=0, max_delay=0):
        count = 0
        begin_time = datetime.datetime.now()
        for i in range(self.responses):
            if self.realism_delay:
                time.sleep(random.randint(min_delay, max_delay))
            requests.post(self.url, data=self.output_data)
            if output:
                count = count + 1
                print("Successfully sent {} responses so far".format(count))
        if output:
            print("\nSent {} responses in {}".format(self.responses, (datetime.datetime.now() - begin_time)))

    def print_data(self):
        return self.output_data
