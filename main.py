from site_visit import search_flight
from slack_message import slack_util

import settings
import time

import sys
import traceback

if __name__ == "__main__":
    while True:
        print(f'{time.ctime()}: Collecting flight details...')
        try:
            search_flight()
            slack_util()
        except KeyboardInterrupt:
            print("Exiting....")
            sys.exit(1)
        except Exception as exc:
            print("Error wile collecting details:", sys.exc_info()[0])
            traceback.print_exc()
        else:
            print(f'{time.ctime()}: Successfully finished collecting flight details...')
        time.sleep(settings.SLEEP_INTERVAL)
