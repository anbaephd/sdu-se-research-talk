import time
from datetime import datetime

import requests

LOOP_INTERVAL = 2

URL: str = "http://localhost:8080"
DATA: dict = {"input_1": 13, "input_2": 9}


def main():

    while True:
        try:
            req = requests.post(URL, json=DATA)

        except requests.exceptions.RequestException as e:
            print(e)
            continue
        else:
            print(datetime.now(), req.json())
        time.sleep(LOOP_INTERVAL)


if __name__ == "__main__":
    main()
