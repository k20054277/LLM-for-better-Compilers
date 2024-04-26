from datetime import datetime

def main():
    # get current date and time
    now = datetime.now()

    # print current date and time
    print("Current Date:", now.date())
    print("Current Time:", now.time())

    # add 1 day to the current date
    future_date = now + datetime.timedelta(days=1)

    # print future date
    print("Future Date:", future_date.date())

if __name__ == "__main__":
    main()