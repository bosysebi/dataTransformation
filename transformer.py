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
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
                    else:
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
                else:
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["typ"] = "obec"
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["typ"] = "zakladna uzemna jednotka"
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
            else:
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["name"] = line[3]["NAZ_LAU1"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["typ"] = "lau1"
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["typ"] = "obec"
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["typ"] = "zakladna uzemna jednotka"
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
            tree[line[3]["NAZ_CZNUTS3"]]["typ"] = "kraj"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["name"] = line[3]["NAZ_LAU1"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["typ"] = "lau1"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["name"] = line[3]["NAZ_OBEC"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["typ"] = "obec"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["name"] = line[3]["NAZ_ZUJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["typ"] = "zakladna uzemna jednotka"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["name"] = line[3]["NAZ_KU"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["typ"] = "katastralne uzemie"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["name"] = line[3]["NAZ_UTJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["typ"] = "uzemna technicka jednotka"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]] = {}
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["name"] = line[3]["NAZ_ZSJ"]
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["typ"] = "zakladna uzemna jednotka"
            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]][line[3]["NAZ_ZSJ"]]["id"] = line[0]
    print(tree)
    return tree;

def createDict2(data, tree):
    i = 0;
    for line in data:
        if line[3]["NAZ_CZNUTS3"] in tree:
            if line[3]["NAZ_LAU1"] in tree[line[3]["NAZ_CZNUTS3"]]:
                if line[3]["NAZ_OBEC"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]:
                    if line[3]["NAZ_ZUJ"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]:
                        if line[3]["NAZ_KU"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]:
                            if line[3]["NAZ_UTJ"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]:
                                if line[3]["NAZ_ZSJ"] in tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]:
                                    print(line)
                                else:
                                    tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]]["workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]]["weekend"], line[2])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"], line[2])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        "workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            "workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        "weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            "weekend"], line[2])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]]["workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]]["workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]]["weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]]["weekend"], line[2])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["weekend"], line[2])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["workday"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["workday"], line[1])
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["weekend"] = addArrays(
                                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                            line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]]["weekend"], line[2])
                                    createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]
                                        [line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
                                    i += 1
                            else:
                                tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]]["workday"], line[1])
                                tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]]["weekend"], line[2])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"], line[1])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"], line[2])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"],line[1])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"],line[2])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["workday"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["workday"], line[1])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["weekend"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["weekend"], line[2])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["workday"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["workday"], line[1])
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["weekend"] = addArrays(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]]["weekend"], line[2])
                                createPath(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
                                i += 1
                                createPath(
                                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][
                                        line[3]["NAZ_ZUJ"]][
                                        line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
                                i += 1
                        else:
                            tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["workday"],line[1])
                            tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["weekend"],line[2])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"], line[1])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"], line[2])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"] = addArrays(
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"],line[1])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"] = addArrays(
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"],line[2])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["workday"] = addArrays(
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["workday"],line[1])
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["weekend"] = addArrays(
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]["weekend"],line[2])
                            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]],line[3]["NAZ_KU"], line, "ku", i)
                            i += 1
                            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
                            i += 1
                            createPath(
                                tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]]
                                [line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i
                            )
                            i += 1
                    else:
                        tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["workday"],line[1])
                        tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["weekend"],line[2])
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"], line[1])
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"], line[2])
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"] = addArrays(
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["workday"], line[1])
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"] = addArrays(
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]]["weekend"], line[2])
                        createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]],
                                   line[3]["NAZ_ZUJ"],
                                   line, "zuj", i)
                        i += 1
                        createPath(
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]],
                            line[3]["NAZ_KU"], line, "ku", i)
                        i += 1
                        createPath(
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                                line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
                        i += 1
                        createPath(
                            tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                                line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
                        i += 1
                else:
                    tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["workday"],line[1])
                    tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["weekend"],line[2])
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["workday"],line[1])
                    tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]]["weekend"],line[2])
                    createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]], line[3]["NAZ_OBEC"], line, "obec", i)
                    i += 1
                    createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]],
                               line[3]["NAZ_ZUJ"],
                               line, "zuj", i)
                    i += 1
                    createPath(
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]],
                        line[3]["NAZ_KU"], line, "ku", i)
                    i += 1
                    createPath(
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                            line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
                    i += 1
                    createPath(
                        tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                            line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
                    i += 1
            else:
                tree[line[3]["NAZ_CZNUTS3"]]["workday"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["workday"], line[1])
                tree[line[3]["NAZ_CZNUTS3"]]["weekend"] = addArrays(tree[line[3]["NAZ_CZNUTS3"]]["weekend"], line[2])
                createPath(tree[line[3]["NAZ_CZNUTS3"]], line[3]["NAZ_LAU1"], line, "lau1", i)
                i += 1
                createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]], line[3]["NAZ_OBEC"], line, "obec", i)
                i += 1
                createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]], line[3]["NAZ_ZUJ"],
                           line, "zuj", i)
                i += 1
                createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]],
                           line[3]["NAZ_KU"], line, "ku", i)
                i += 1
                createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                               line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
                i += 1
                createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][
                               line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
                i += 1
        else:
            createPath(tree, line[3]["NAZ_CZNUTS3"], line, "kraj", i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]], line[3]["NAZ_LAU1"], line, "lau1", i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]], line[3]["NAZ_OBEC"], line, "obec",  i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]], line[3]["NAZ_ZUJ"], line, "zuj", i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]], line[3]["NAZ_KU"], line, "ku", i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]], line[3]["NAZ_UTJ"], line, "tuj", i)
            i += 1
            createPath(tree[line[3]["NAZ_CZNUTS3"]][line[3]["NAZ_LAU1"]][line[3]["NAZ_OBEC"]][line[3]["NAZ_ZUJ"]][line[3]["NAZ_KU"]][line[3]["NAZ_UTJ"]], line[3]["NAZ_ZSJ"], line, "zsj", i)
            i += 1
    return tree

def createPath(tree, path, line, type, id):
    tree[path] = {}
    tree[path]["name"] = path
    tree[path]["id"] = id
    tree[path]["type"] = type
    tree[path]["workday"] = addArrays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], line[1])
    tree[path]["weekend"] = addArrays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], line[2])
    tree[path]["children"] = []

def appendChild(tree, path, line, type, id):
    newTree = {
        "name": path,
        "id": id,
        "type": type,
        "workday": line[1],
        "weekend": line[2],
    }
    tree["children"].append(newTree)



def addArrays(array1, array2):
    for i in range(len(array1)):
        array1[i] = array1[i] + array2[i]
    return array1


def changeFormat(tree):
    final = {}
    if len(tree) == 0:
        return
    for key, value in tree.items():
        if(type(tree[key]) is dict):
            print(tree[key]["name"])
            changeFormat(tree[key])
    return final



bmo = "bmo_db.csv"
testJson = "Zones.json"
zuj = "ZUJ.csv"
data = groupByCode(dataLoad(bmo))
zujDict = getZujData(zuj)
data = mergeDataSets(data, zujDict)
tree = createDict2(data, tree())
changeFormat(tree)
with open(testJson, "w") as jsonFile:
    jsonFile.write(json.dumps(tree, indent=4))

