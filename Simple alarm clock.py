import time
from datetime import datetime

def alarm_clock():
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    print(f"Alarm set for {alarm_time}")
    
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up! Alarm ringing!")
            break
        time.sleep(1)

alarm_clock()
