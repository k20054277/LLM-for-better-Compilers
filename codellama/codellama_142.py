from datetime import date, timedelta

today = date.today()
print(today)

yesterday = today - timedelta(days=1)
print(yesterday)

tomorrow = today + timedelta(days=1)
print(tomorrow)