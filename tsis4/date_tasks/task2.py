import datetime

today = datetime.datetime.today()
delta = datetime.timedelta(1)
tomorrow = today + delta
yesterday = today - delta

print(yesterday)
print(today)
print(tomorrow)
