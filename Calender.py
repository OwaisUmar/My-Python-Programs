import calendar


def check_leap(yr):
    if yr % 400 == 0 or yr % 4 == 0:
        return True
    else:
        return False


def check_valid_date(dt, m, lf):
    days30 = [4, 6, 9, 11]
    days31 = [1, 3, 5, 7, 8, 10, 12]
    if dt <= 29 and m == 2 and lf:
        return True
    elif dt <= 28 and m == 2:
        return True
    elif dt <= 30 and m in days30:
        return True
    elif dt <= 31 and m in days31:
        return True
    else:
        return False


def get_day(di):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[di]


while True:
    year = int(input('Enter a year (From 1970) :  '))
    if year < 1970:
        print('Enter a valid year.')
    else:
        break

while True:
    month = int(input('Enter a month (1-12) :  '))
    if month < 1 or month > 12:
        print('Enter a month in the range (1-12).')
    else:
        break

leap = check_leap(year)
while True:
    date = int(input('Enter a date (1-31) :  '))
    if date > 0 and check_valid_date(date, month, leap):
        break
    else:
        print('Enter a valid date.')

day_index = calendar.weekday(year, month, date)
day = get_day(day_index)
print(date, '/', month, '/', year, 'falls on', day)

