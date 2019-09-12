# noinspection PyUnresolvedReferences
import datetime
import os

# noinspection PyUnresolvedReferences
from service import calculateWork

HISTORY_FOLDER = 'history'


def printWorker(worker):
    print('| %-14s %16s %22s %9s %9s %17s %11s %24s |' % (
        worker[0], worker[1], worker[2], worker[3], worker[4], worker[5], worker[6], worker[7]))


if not os.path.exists(HISTORY_FOLDER):
    os.mkdir(HISTORY_FOLDER)

nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
lastFileName = HISTORY_FOLDER + '/' + nowDate + '.txt'
peoples = [
    'Ситников',
    'Турнаев',
    'Рылов',
    'Зайчиков',
    'Кулиев',
    'Пузырев',
    'Суртаев',
    'Загоруйко',
    'Пупсиков',
]

peoplesData = []
for person in peoples:
    peoplesData.append(calculateWork(person, nowDate))

# if os.path.exists(lastFileName):
#     os.remove(lastFileName)
print('Time Attandance (v2.0): Python')
print(
    '+-----------------------------------------------------------------------------------------------------------------------------------+')
print(
    '| Фамилия       | Ср. (раб дни)  | Доработать (раб дни) | Сегодня | Раб дни | Ср. (отраб дни) | Отраб. дни | Доработать (отраб дни) |')
print(
    '+-----------------------------------------------------------------------------------------------------------------------------------+')

peoplesData = sorted(peoplesData, key=lambda kv: kv[1], reverse=True)
for d in peoplesData:
    printWorker(d)

print(
    '+-----------------------------------------------------------------------------------------------------------------------------------+')
