
import time
import schedule

def job():
    print("Job is running...")
    time.sleep(5)
    print("Job is finished.")

def main():
    # Schedule the job to run every minute at :01 past each hour
    schedule.every().minute.at(":01").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
