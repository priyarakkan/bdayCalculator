from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


print("Birthday Calculator")
name = input("Enter name : ")
birthday_str = input("Enter birthday (MM/DD/YY): ")
birthday = datetime.strptime(birthday_str, '%m/%d/%y')
birthdayy_str = datetime.strftime(birthday,'%A, %B %d, %Y')
print(f'Birthday: {birthdayy_str}')
today = datetime.today()
format_today = today.strftime('%A, %B %d, %Y')
print(f'Today: {format_today}')

age = today.year - birthday.year

if (today.month, today.day) < (birthday.month, today.day):
    age-= 1
print(f'{age} years old.')

# days 
if (birthday.month == today.month):
    if (birthday.day - today.day == 0):
        print(f"{name}'s birthday is today!")
    elif (birthday.day - today.day == 1):
        print(f"{name}'s birthday is tomorrow!")
    elif (birthday.day - today.day == -1):
        print(f"{name}'s is yesterday!")
else:
    if (today.month < birthday.month):
        upcoming_bday = birthday + date(year = age)
        print(upcoming_bday)
        pass

    elif (today.month > birthday.month):
        pass

    elif (today.month == birthday.month):
        pass





# Marc's birthday is in 92 days.

