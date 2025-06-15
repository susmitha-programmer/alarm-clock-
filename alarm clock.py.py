import datetime
import time
from playsound import playsound  # Make sure you install this application

alarm_time = input("Enter alarm time in HH:MM format (24-hour): ")
alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}...")

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("Time to Wake Up")
        playsound("alarm.mp3")  # Replace with your alarm file
        break

    time.sleep(30) 