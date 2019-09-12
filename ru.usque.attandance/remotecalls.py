import json
import urllib
from urllib.request import urlopen
import os.path
from lxml.html import fromstring

MAIN_HOST = 'http://10.1.1.49'


def monthRequest(peoples, monthDateParam):
    requestResult = {}

    dataFileName = 'history/' + monthDateParam + '.txt'
    if os.path.exists(dataFileName):
        # print('use cache: ', dataFileName)
        loadedData = loadJsonFromFile(dataFileName)
        return filterData(peoples, loadedData)

    # REQUEST
    params = {'date': monthDateParam}
    parser = performRequest(params)
    for elem in parser.xpath('//*[@id="main"]/div/div[2]/table/tbody/tr'):
        fullName = str(elem.xpath('td[1]/text()')[0]).strip()
        workedDays = str(elem.xpath('td[2]/text()')[0]).strip()
        workedHours = str(elem.xpath('td[3]/text()')[0]).strip().replace(':', '.')
        surname = getSurname(fullName)

        avgWorked = float(format(float(workedHours) / float(workedDays), '.2f'))
        requestResult[surname] = {
            'workedDays': workedDays,
            'workedHours': workedHours,
            'avgWorked': avgWorked,

        }

    saveToFileObject(dataFileName, requestResult)
    return filterData(peoples, requestResult)


def dayRequest(peoples, dayDateParam=None):
    requestResult = {}
    params = {'date': dayDateParam}
    dataFileName = None
    if (dayDateParam is None):
        params = {}
    else:
        dataFileName = 'history/' + dayDateParam + '.txt'
        if os.path.exists(dataFileName):
            # print('use cache: ', dataFileName)
            loadedData = loadJsonFromFile(dataFileName)
            return filterData(peoples, loadedData)

    # REQUEST
    print('Request: ', dayDateParam)
    parser = performRequest(params)
    for elem in parser.xpath('//*[@id="main"]/div/div[2]/table/tbody/tr'):
        fullName = str(elem.xpath('td[1]/text()')[0]).strip()
        attendance = float(str(elem.xpath('td[4]/text()')[0]).strip().replace(':', '.'))
        surname = getSurname(fullName)
        requestResult[surname] = attendance

    if not dataFileName is None:
        saveToFileObject(dataFileName, requestResult)


    return filterData(peoples, requestResult)


def saveToFileObject(dataFileName, requestResult):

    # nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    # if not dataFileName.__contains__(nowDate):
    with open(dataFileName, 'w') as f:
        print('store to: ', dataFileName)
        json.dump(requestResult,
                  f,
                  sort_keys=True,
                  indent=4,
                  ensure_ascii=False)


def getSurname(fullName):
    surname = 'Incognito'
    if fullName.__contains__(' '):
        surname = fullName.split(' ')[0]
    return surname


def performRequest(params):
    encodedParams = urllib.parse.urlencode(params).encode('UTF-8')
    response = urlopen(MAIN_HOST, encodedParams)
    result = response.read().decode('utf-8')
    parser = fromstring(result)
    return parser


def loadJsonFromFile(dataFileName):
    with open(dataFileName, 'r') as f:
        loadedData = json.load(f)
    return loadedData


def filterData(peoples, data):
    result = {}
    if len(peoples) > 0:
        for item in data:
            if item in peoples:
                result[item] = data[item]
        return result
    else:
        return data
