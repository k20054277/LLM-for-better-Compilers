import datetime

def main():
    today = datetime.date.today()
    assert today.weekday() == 0 or today.weekday() == 6, "Today is not a weekend day"
    print("Today is", today.strftime("%A"))

if __name__ == "__main__":
    main()