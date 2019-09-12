import calendar, datetime
import os.path
from urllib.request import urlopen

# средняя за текущий месяц
# доработать с учетом работы по выходным
#
DAY_OFF_RESOURCE = "https://isdayoff.ru/api/getdata?year=2019&pre=1"

# возвращает Map дней текущего месяца на статус дня.
def getDatesDayOff(dateRequest):
    split = str(dateRequest).split('-')
    currentYear = int(split[0])
    currentMonth = int(split[1])
    currentDay = int(split[2])

    # now = datetime.datetime.now()
    # currentYear = now.year
    # currentMonth = now.month
    # currentDay = now.day



    fileOfWorkDays = str(currentYear) + '-workdays.txt'
    if not os.path.exists(fileOfWorkDays):
        print('Downloading working days...')
        response = urlopen(DAY_OFF_RESOURCE)
        result = response.read().decode('utf-8')

        with open(fileOfWorkDays, "w") as f:
            f.write(result)

    with open(fileOfWorkDays, "r") as f:
        workDays = f.read()
        # print('Restored workDays: ', workDays)

    allDays = []
    for month in range(1, 13):
        lastMonthDay = calendar.monthrange(currentYear, month)[1]
        days = [datetime.date(currentYear, month, day).strftime('%Y-%m-%d') for day in range(1, lastMonthDay + 1)]
        allDays.extend(days)

    date2Work = dict(zip(allDays, workDays))

    lastCurrentMonthDay = calendar.monthrange(currentYear, currentMonth)[1]
    currentMonthDays = [datetime.date(currentYear, currentMonth, day).strftime('%Y-%m-%d') for day in
                        range(1, currentDay + 1)]

    result = {}
    for d in currentMonthDays:
        result[d] = date2Work[d]

    return result

# s = getDatesDayOff('2019-08-10')
# print(s)