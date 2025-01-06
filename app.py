from send import send_email
import schedule
import time
from datetime import datetime, date
import sys

def job():
    send_email()

def run_scheduler():
    schedule.every().day.at("08:30").do(job)
    schedule.every().day.at("13:45").do(job)
    schedule.every().day.at("19:00").do(job)

    while True:
        now = datetime.now()
        if now.weekday() < 5:
            schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    today = date.today()
    
    if today.weekday() in [5, 6]: # [5, 6]:
        sys.exit(0)
    
    print("Scheduler is running...")
    run_scheduler()
