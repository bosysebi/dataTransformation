import csv
import collections
import json

# read csv and add to dictionary

"""data = {}
with open(bmo) as bmo:
    csvReader = csv.DictReader(bmo, delimiter=";")
    for bmoRow in csvReader:
        ZSJ = bmoRow["KOD_ZSJ_P"]
        data[ZSJ] = bmoRow

with open(testJson, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))"""

def dataLoad(name):
    zonedata = []
    with open(name) as file:
        i = 0
        for line in file:
            day = (line.strip('\n')).split(";")
            zonedata.insert(i, day)
            i = i + 1
    return zonedata

def groupByCode(data):
    i = 1;
    newData =  []
    while i < len(data):
        code = data[i][0]
        workday = []
        weekend = []
        while i < len(data) and data[i][2] == 'workday':
            workday.append(int(data[i][3]))
            i += 1
        while i < len(data) and data[i][2] == 'weekend':
            weekend.append(int(data[i][3]))
            i += 1
        line = [int(code)]
        line.append(workday)
        line.append(weekend)
        newData.append(line)
    return newData

def getZujData(zuj):
    data = {}
    with open(zuj, "r", encoding="latin2") as bmo:
        csvReader = csv.DictReader(bmo, delimiter=";")
        for bmoRow in csvReader:
            ZSJ = bmoRow["KOD_ZSJ"]
            data[ZSJ] = bmoRow
    return data

def mergeDataSets(data, dictionary):
    newDataSet = []
    for place in data:
        line = place
        line.append(dictionary[str(place[0])])
        newDataSet.append(line)
    return newDataSet

def tree():
    return collections.defaultdict(tree)

bmo = "bmo_db.csv"
testJson = "Zones.json"
zuj = "ZUJ.csv"
data = groupByCode(dataLoad(bmo))
zujDict = getZujData(zuj)
data = mergeDataSets(data, zujDict)
print(data)
tree = tree()