import datetime
today = datetime.date.today()
print(today)
today = today + datetime.timedelta(seconds=10000000000)
print(today)