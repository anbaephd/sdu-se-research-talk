import time
from datetime import datetime

import requests

LOOP_INTERVAL = 5

URL: str = "http://localhost:8080"
DATA: dict = {"input_1": 13, "input_2": 9}


def main():

    while True:

        req = requests.post(URL, json=DATA)

        print(datetime.now(), req.json())

        time.sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    main()
