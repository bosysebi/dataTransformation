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

def createDict(data, tree):
    for line in data:
        if line[3]["NAZ_CZNUTS3"] in tree:
            if line[3]["NAZ_LAU1"] in tree[line[3]["NAZ_CZNUTS3"]]:
                if line[3]["NAZ_OBEC"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]:
                    if line[3]["NAZ_ZUJ"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]:
                        if line[3]["NAZ_KU"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]:
                            if line[3]["NAZ_UTJ"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]:
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
                            else:
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                        else:
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = line[0]
                    else:
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = line[0]
                else:
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = line[0]
            else:
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["name"] = line[3]["NAZ_LAU1"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
        else:
            tree[line[3]["NAZ_CZNUTS3"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]]["name"] = line[3]["NAZ_CZNUTS3"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["name"] = line[3]["NAZ_LAU1"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
    print(tree)
    return tree;



bmo = "bmo_db.csv"
testJson = "Zones.json"
zuj = "ZUJ.csv"
data = groupByCode(dataLoad(bmo))
zujDict = getZujData(zuj)
data = mergeDataSets(data, zujDict)
tree = createDict(data, tree())
with open(testJson, "w") as jsonFile:
    jsonFile.write(json.dumps(tree, indent=4))

