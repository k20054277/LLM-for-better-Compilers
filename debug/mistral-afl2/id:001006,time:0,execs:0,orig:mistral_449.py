
import time
import schedule

def job():
    print("Job executed at: ", time.ctime())

# Schedule the job to run every 1 minute
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
