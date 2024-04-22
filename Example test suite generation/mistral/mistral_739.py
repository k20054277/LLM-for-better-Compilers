
import time
import schedule

def job():
    print("Job is running...")
    time.sleep(5) # This job will run for 5 seconds

def main():
    schedule.every(1).minutes.do(job) # Schedule the job to run every minute
    
    while True:
        schedule.run_pending() # Run any scheduled jobs
        time.sleep(60) # Sleep for a minute before checking again

if __name__ == "__main__":
    main()
