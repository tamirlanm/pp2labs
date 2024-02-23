from datetime import date, timedelta
from datetime import datetime
from datetime import datetime,time
#task1
#Write a Python program to subtract five days from current date.
dt = date.today() - timedelta(5)
print('Current Date:',date.today())
print('5 days before current date:',dt)
print()

#task2
#Write a Python program to print yesterday, today, tomorrow.
print('Yesterday:', date.today()-timedelta(1))
print('Today', date.today())
print('Tomorrow', date.today()+timedelta(1))

#task3
#Write a Python program to drop microseconds from datetime.
#Write a Python program to drop microseconds from datetime.
current_datetime=datetime.now()
current_datetime_without_micrs = current_datetime.replace(microsecond=0)
print(current_datetime)
print(current_datetime_without_micrs)

#task4
def diff_in_sec(dt2,dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2017-08-10 01:00:00', '%Y-%m-%d %H:%M:%S')
date2=datetime.now()
print("%d seconds" %(diff_in_sec(date2, date1)))