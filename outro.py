
import datetime
import time
from playsound import playsound

def main():
    while True:
        now = datetime.datetime.now()
        # Calculate the target time: 58.5 seconds before midnight
        target_time = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0, 0)) - datetime.timedelta(seconds=58.5)
        
        # If the current time is past the target time, skip to the next day
        if now >= target_time:
            time.sleep(1)  # Prevent CPU overuse
            continue

        # Calculate the remaining time until the target time
        time_until_target = (target_time - now).total_seconds()

        if time_until_target > 0:
            while time_until_target > 0:
                print(f"Countdown: {int(time_until_target)} seconds remaining", end="\r")
                time.sleep(1)
                print(" ")
                print(f"Countdown: {int(time_until_target)} seconds remaining", end="\r")
                now = datetime.datetime.now()
                time_until_target = (target_time - now).total_seconds()

        # Play the sound
        playsound('outro.mp3')
        break

if __name__ == "__main__":
    main()
print("subscribe to https://www.youtube.com/@mycomputerthings")