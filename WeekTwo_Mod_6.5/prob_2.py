from win10toast import ToastNotifier
import json
import time
import requests
# Api Url

while True:
    api_url = "http://www.boredapi.com/api/activity/"

    # Get the json
    response = requests.get(api_url)
    content = response.content.decode('UTF-8')


    # Convert string to json
    dict_content = json.loads(content)


    # Get the task
    task_msg = dict_content['activity']
    print(task_msg)

    # Notification to windows
    toaster = ToastNotifier()
    toaster.show_toast(task_msg,duration=10)
    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)
    time.sleep(1800)