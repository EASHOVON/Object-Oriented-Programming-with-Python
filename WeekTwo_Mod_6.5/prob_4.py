""" Create a chat bot that will understand if you are bored, then it will call the Bored API and suggest some activities to you in reply. It should also have the ability to tell the current time.

Example:
>> Hey robot, this house is boring. Any idea what I can do?
Bot:  You can learn Javascript.
>> thank you. What’s the time?
Bot: it’s 9:30 pm sir.
 """
import json
import requests
from datetime import datetime

def callApi():
    api_url = "http://www.boredapi.com/api/activity?type=recreational"
    response = requests.get(api_url)
    content = response.content.decode('UTF-8')
    dict_content = json.loads(content)
    getMsg = dict_content['activity']
    print(f'Bot: {getMsg}')

def showTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(f'Bot: it’s {current_time} sir')



while True:
    inputText = input("Ask Something: ")
    inputText = inputText.lower()
    breakText = inputText.split(" ")
    predictText = ['boring','bored','unhappy']

    for word in breakText:
        for pText in predictText:
            if word==pText:
                callApi()
                break
        if word=='time':
            showTime()
            break