import csv
import collections
import json

# read csv and add to dictionary
def dataLoad(name):
    zonedata = []
    with open(name) as file:
        i = 0
        for line in file:
            day = (line.strip('\n')).split(";")
            zonedata.insert(i, day)
            i = i + 1
    return zonedata

#Groups all our BMO data into one entry, with two arrays with numbers, one for weekend, one for workday
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

#Opens CSV ZUJ data
def getZujData(zuj):
    data = {}
    with open(zuj, "r", encoding="latin2") as bmo:
        csvReader = csv.DictReader(bmo, delimiter=";")
        for bmoRow in csvReader:
            ZSJ = bmoRow["KOD_ZSJ"]
            data[ZSJ] = bmoRow
    return data

#Merges the BMO data with ZUJ data to create an array, one line in array is one UTJ Unit data
#Merges them through ZSJ CODE
def mergeDataSets(data, dictionary):
    newDataSet = []
    for place in data:
        line = place
        line.append(dictionary[str(place[0])])
        newDataSet.append(line)
    return newDataSet

#Definitin for default dictionary, I need a multidimensional dicitonary
def tree():
    return collections.defaultdict(tree)

#MAIN SORTING
#Uses default dictionary, checks for each key, if present, goes deeper, if not,
#creates and empty dictionary all the way to the NAZ_UTJ level
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
                                    pass;
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


#Helper function, creates a path in the default dictionary
def createPath(tree, path, line, type, id):
    tree[path] = {}
    tree[path]["name"] = path
    tree[path]["id"] = id
    tree[path]["type"] = type
    tree[path]["workday"] = addArrays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], line[1])
    tree[path]["weekend"] = addArrays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], line[2])
    tree[path]["children"] = []


#helper function, returns array that is sum of two given
def addArrays(array1, array2):
    for i in range(len(array1)):
        array1[i] = array1[i] + array2[i]
    return array1

#changes dictionary format according to schema in mobile presence
def changeFormat(tree):
    children = []
    if len(tree) == 0:
        return
    for key, value in tree.items():
        if(type(tree[key]) is dict):
            newEle = {
                "name": tree[key]["name"],
                "id": tree[key]["id"],
                "type": tree[key]["type"],
                "workday": tree[key]["workday"],
                "weekend": tree[key]["weekend"],
                "children": changeFormat(tree[key])
            }
            children.append(newEle)
    return children


#Removes the inbetween nodes when node has only one descendant
def removeSingleNodes(tree):
    for place in tree:
        if len(place["children"])==0:
            return tree
        removeSingleNodes(place["children"])
        if len(place["children"])==1:
            place["children"] = place["children"][0]["children"]
    return tree

bmo = "bmo_db.csv"
result = "Zones.json"
zuj = "ZUJ.csv"
data = groupByCode(dataLoad(bmo))
zujDict = getZujData(zuj)
data = mergeDataSets(data, zujDict)
data = createDict2(data, tree())
data = (changeFormat(data))
data = removeSingleNodes(data)
final = {}
final["data"] = data
with open("result", "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

