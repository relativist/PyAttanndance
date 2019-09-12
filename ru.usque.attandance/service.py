# noinspection PyUnresolvedReferences
from remotecalls import monthRequest, dayRequest
# noinspection PyUnresolvedReferences
from dayoffService import getDatesDayOff

statusToHours = {
    1: 0,
    2: 7,
    0: 8
}


def calculateWork(surname, tillDate):
    totalHoursToWork = 0
    personTotalHoursToWork = 0
    workingDays = 0
    personWorked = 0
    dayOffMap = getDatesDayOff(tillDate)
    lastDayWorked = 0
    personWorkingDays = 0
    for day in dayOffMap:
        dayStatus = int(dayOffMap[day])

        if dayStatus in [0, 2]:
            workingDays += 1
        totalHoursToWork += statusToHours[dayStatus]

        request = dayRequest([surname], day)
        if len(request) > 0:
            lastDayWorked = request[surname]
            personWorked += lastDayWorked
            if dayStatus in [0, 2]:
                personWorkingDays += 1
                personTotalHoursToWork += statusToHours[dayStatus]

        # print(day, 'status=',dayStatus,'hours=',statusToHours[dayStatus], 'worked :',personWorked, 'working days:',workingDays)

    avgWorked = float(format(personWorked / workingDays, '.2f'))
    needToWork = float(format(totalHoursToWork - personWorked, '.2f'))
    personNeedToWork = float(format(personTotalHoursToWork - personWorked, '.2f'))
    personAvgWorked = 0.0
    if(personWorkingDays!=0):
        personAvgWorked = float(format(personWorked / personWorkingDays, '.2f'))

    return [surname, avgWorked, needToWork, lastDayWorked, workingDays, personAvgWorked , personWorkingDays, personNeedToWork]

# Test
# r = calculateWork('Ситников', '2019-09-12')
# print(r)

# f = getDatesDayOff('2019-09-11')
# print(f)
