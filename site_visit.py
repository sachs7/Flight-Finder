from prettytable import PrettyTable

from splinter import Browser
import time

from settings import *

SAVE_SCREENSHOT_AT_LOCATION = BASE_PATH + '1.png'

SAVE_TEXT_AT_LOCATION = BASE_PATH + 't.txt'


def search_flight():
    try:

        browser = Browser('chrome', headless=True)

        browser.visit(SITE_NAME)

        browser.find_by_xpath(CLICK_FROM).click()
        browser.find_by_xpath(FROM).fill(FROM_PLACE)

        browser.find_by_xpath(CLICK_TO).click()
        browser.find_by_xpath(TO).fill(TO_PLACE)

        browser.find_by_xpath(CLICK_ORIGIN_DEPARTURE).click()
        browser.find_by_xpath(ENTER_ORIGIN_DEPARTURE_DATE).fill(DEPARTURE_FROM_US)

        browser.find_by_xpath(CLICK_DESTINATION_DEPARTURE).click()
        browser.find_by_xpath(ENTER_DESTINATION_DEPARTURE_DATE).fill(DEPARTURE_FROM_INDIA)

        browser.find_by_xpath(CLICK_FLEXIBLE_DATES).click()
        time.sleep(5)

        browser.execute_script("window.scrollTo(0, 165)")

        browser.driver.save_screenshot(SAVE_SCREENSHOT_AT_LOCATION)
        time.sleep(10)

        diction = {}
        for i in range(4, 13):
            diction[i] = ' '.join(browser.find_by_xpath(FLIGHT_DETAILS + str(i) + ']').text.split('\n\n')).split('\n')

        table_1 = PrettyTable(['Price', 'Trip-Type', 'Timings', 'Airlines', 'Hours', 'Stops', 'Layover'])
        table_2 = PrettyTable(['Price', 'Trip-Type', 'Timings/Airlines', 'Hours', 'Stops', 'Layover'])

        for key, value in diction.items():
            if len(diction.get(key)) == 7:
                table_1.add_row(diction.get(key))
            elif len(diction.get(key)) == 6:
                table_2.add_row(diction.get(key))

        print(table_1)
        print('\n Addition flights... \n')
        print(table_2)
        data_1 = table_1.get_string()
        data_2 = table_2.get_string()
        with open('t.txt', 'w') as f:
            f.write(data_1)
            f.write('\n Additional flight details... \n')
            f.write(data_2)

        browser.quit()
    except AttributeError:
        print('Element has no attribute "text"')
    else:
        browser.quit()
