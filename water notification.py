import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title =  "Water pilo bhai!",
            message = "Time to drink water! Stay hydrated for better health.",
            timeout = 10
        )
        #time.sleep(3) # for testing purposes, set to 3 seconds. Change to 3600 for hourly reminders.
        time.sleep(3600)  # Wait for 1 hour before sending the next notification
water_reminder()