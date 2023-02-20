import datetime
a = datetime.datetime.now()
print (a)
from datetime import datetime, timedelta
#1
now_day = datetime.now()
back5 = now_day - timedelta(days=5)
print("\n сегодня:", now_day,"\n")
print("5 дней назад:", back5)


#2


today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\nвчера ", yesterday)
print("сегодея ", today)
print("завтра ", tomorrow,'\n')


#3

now = datetime.now()
microsec = now.replace(microsecond=0)
print("\nсейчас", now)
print("без микросекунд", microsec,'\n')


# #4

date1 = datetime(2023, 2, 20, 12, 0, 0)
date2 = datetime(2023, 2, 20, 12, 0, 12)
date3 = datetime(2023, 2, 20, 12, 1, 40)

dif1 = (date2 - date1).total_seconds()
dif2 = (date3 - date1).total_seconds()
print("\nразница в секундах", dif1)
print("разница в секундах", dif2,'\n')

