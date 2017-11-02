SITE_NAME = 'https://google.com/flights'

FROM_PLACE = 'SFO'

TO_PLACE = 'BLR'

DEPARTURE_FROM_US = 'August 2'

DEPARTURE_FROM_INDIA = 'July 2'

CLICK_FROM = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[5]/table/tbody/tr[' \
           '1]/td[1]/div'
FROM = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[5]/table/tbody/tr[1]/td[' \
       '1]/div/input'

CLICK_TO = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[5]/table/tbody/tr[' \
           '1]/td[2]/div'
TO = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[5]/table/tbody/tr[1]/td[' \
     '2]/div/input'


CLICK_ORIGIN_DEPARTURE = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[' \
                  '5]/table/tbody/tr[2]/td[1]/div'

ENTER_ORIGIN_DEPARTURE_DATE = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[' \
                       '5]/table/tbody/tr[2]/td[1]/div/div[1]/div[2]/input'

CLICK_DESTINATION_DEPARTURE = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[1]/div[' \
                              '5]/table/tbody/tr[2]/td[2]/div'

ENTER_DESTINATION_DEPARTURE_DATE = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[' \
                                   '1]/div[5]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/input'

CLICK_FLEXIBLE_DATES = '/html/body/div[3]/div/div/div[1]/div[2]'

BASE_PATH = '/Users/suplaonkar/Desktop/python_first_docker/flight_price_screenbot/'

FLIGHT_DETAILS = '//*[@id="root"]/div[3]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div/div[3]/div[1]/div/div[' \
                 '2]/div[2]/div[1]/div['

# Send Slack message for every 45 minutes
SLEEP_INTERVAL = 45 * 60

SLACK_CHANNEL = '#flight_dates'

try:
    from private import *
    TOKEN_FOR_SLACK = SLACK_TOKEN
except Exception:
    pass
