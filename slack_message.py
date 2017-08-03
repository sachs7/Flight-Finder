import requests
import time
from slackclient import SlackClient

from settings import *
from site_visit import SAVE_SCREENSHOT_AT_LOCATION, SAVE_TEXT_AT_LOCATION


def slack_util():

    my_image_file = {
      'file': (SAVE_SCREENSHOT_AT_LOCATION, open(SAVE_SCREENSHOT_AT_LOCATION, 'rb'), 'png')
    }

    my_text_file = {
      'file': (SAVE_TEXT_AT_LOCATION, open(SAVE_TEXT_AT_LOCATION, 'rb'), 'txt')
    }

    image_name = str(time.ctime()) + '.png'

    file_name = 'Flight Details ' + DEPARTURE_FROM_US + '.txt'

    payload_1 = {
      "filename": image_name,
      "token": TOKEN_FOR_SLACK,
      "channels": ['#flight_dates'],
    }

    payload_2 = {
        'filename': file_name,
        'token': TOKEN_FOR_SLACK,
        'channels': ['#flight_dates'],
    }

    # Create a slack client.
    sc = SlackClient(TOKEN_FOR_SLACK)

    message = f'@here Found Round-Trip flight details *Origin:* `{FROM_PLACE}`, *Destination:* `{TO_PLACE}`'

    sc.api_call(
        "chat.postMessage", channel=SLACK_CHANNEL, text=message,
        username='pybot', icon_emoji=':robot_face:'
    )

    requests.post("https://slack.com/api/files.upload", params=payload_1, files=my_image_file)
    requests.post('https://slack.com/api/files.upload', params=payload_2, files=my_text_file)
