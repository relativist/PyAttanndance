import json


class Person(object):
    # def __init__(self, surname, workedDays, workedHours, avgWorked, today, needToWork):
    #     """Constructor"""
    #     self.surname = surname
    #     self.workedDays = workedDays
    #     self.workedHours = workedHours
    #     self.avgWorked = avgWorked
    #     self.today = today
    #     self.needToWork = needToWork

    def __init__(self, dict):
        vars(self).update(dict)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def toJSONFile(self, file):
        return json.dump(self,file, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def printPerson(worker, structure):
        print('| %-10s %9s %12s %9s %4s |' % (
        worker, structure['avgWorked'], structure['needToWork'], structure['today'], structure['workedDays']))