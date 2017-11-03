# Flight-Finder

Imagine you plan to travel to a different country but want to find a flight that fits into your budget! Isn't it kind of annoying to keep visiting flight site's daily to know if you can find a fare that is light on your pocket? Well, this is an attempt to automate this process via Splinter (a wrapper around Selenium), Python and Slack - for sending you updates. 

The bot sends you an update every half an hour (can be adjusted) so that you never miss an opportunity to book a budget airline! 

To install:
- Clone this repo.
- Run `pip3 install -r requirements.txt`
- Download Chrome Driver and place it in Python PATH
- Edit "BASE_PATH" variable in `settings.py`
- Run `python3 main.py`

Note: You need to get a Slack Token and have a Slack channel for this to work. Slack Message and the Commandline output is as shown in below:

Slack Message:
![Sample Slack Message](https://github.com/sachs7/Flight-Finder/blob/master/Slack_Message_Example.png?raw=true "Slack Message")

CommandLine:
![CommandLine Table](https://github.com/sachs7/Flight-Finder/blob/master/Flight_Details_CMD_line.png?raw=true "Flight_Details_CMD_line")
