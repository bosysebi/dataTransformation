import csv
import collections
import json
import sys
import logging
import os.path
from pathlib import Path

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
        #Goes through the data and creates a single array with user numbers, counts on the data used being correct
        #18 & 18 records per workday, weekend
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
#There was an issue with encoding, solved by opening with windows 1250 and writing using utf-8
def getZujData(zuj):
    data = {}
    with open(zuj, "r", encoding="windows-1250") as zj:
        csvReader = csv.DictReader(zj, delimiter=";")
        for zujRow in csvReader:
            ZSJ = zujRow["KOD_ZSJ"]
            data[ZSJ] = zujRow
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

#Definitin for default dictionary, I need a multidimensional dictionary
def tree():
    return collections.defaultdict(tree)

"""
#MAIN SORTING
#Uses default dictionary, checks for each key, if present, goes deeper, if not,
#creates and empty dictionary all the way to the NAZ_UTJ level
def createDict2(data, tree):
    i = 0
    unitName = ["NAZ_CZNUTS3", "NAZ_LAU1", "NAZ_OBEC", "NAZ_ZUJ", "NAZ_KU", "NAZ_UTJ", "NAZ_ZSJ"]
    shortName = ["kraj", "lau1", "obec", "zuj", "ku", "tuj", "zsj"]
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
                                    tempTree = tree[line[3][unitName[0]]][line[3][unitName[1]]][line[3][unitName[2]]][
                                        line[3][unitName[3]]][line[3][unitName[4]]][line[3][unitName[5]]]
                                    for j in range(6, len(unitName)):
                                        createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                                        i += 1
                                        tempTree = tempTree[line[3][unitName[j]]]
                                    tempTree = tree
                                    for k in range(6):
                                        tempTree[line[3][unitName[k]]]['workday'] = addArrays(
                                            tempTree[line[3][unitName[k]]]['workday'], line[1])
                                        tempTree[line[3][unitName[k]]]['weekend'] = addArrays(
                                            tempTree[line[3][unitName[k]]]['weekend'], line[2])
                                        if k + 1 != 6:
                                            tempTree = tempTree[line[3][unitName[k]]]
                            else:
                                tempTree = tree[line[3][unitName[0]]][line[3][unitName[1]]][line[3][unitName[2]]][
                                    line[3][unitName[3]]][line[3][unitName[4]]]
                                for j in range(5, len(unitName)):
                                    createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                                    i += 1
                                    tempTree = tempTree[line[3][unitName[j]]]
                                tempTree = tree
                                for k in range(5):
                                    tempTree[line[3][unitName[k]]]['workday'] = addArrays(
                                        tempTree[line[3][unitName[k]]]['workday'], line[1])
                                    tempTree[line[3][unitName[k]]]['weekend'] = addArrays(
                                        tempTree[line[3][unitName[k]]]['weekend'], line[2])
                                    if k + 1 != 5:
                                        tempTree = tempTree[line[3][unitName[k]]]

                        else:
                            tempTree = tree[line[3][unitName[0]]][line[3][unitName[1]]][line[3][unitName[2]]][line[3][unitName[3]]]
                            for j in range(4, len(unitName)):
                                createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                                i += 1
                                tempTree = tempTree[line[3][unitName[j]]]

                            tempTree = tree
                            for k in range(4):
                                tempTree[line[3][unitName[k]]]['workday'] = addArrays(
                                    tempTree[line[3][unitName[k]]]['workday'], line[1])
                                tempTree[line[3][unitName[k]]]['weekend'] = addArrays(
                                    tempTree[line[3][unitName[k]]]['weekend'], line[2])
                                if k + 1 != 4:
                                    tempTree = tempTree[line[3][unitName[k]]]
                    else:
                        tempTree = tree[line[3][unitName[0]]][line[3][unitName[1]]][line[3][unitName[2]]]
                        for j in range(3, len(unitName)):
                            createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                            i += 1
                            tempTree = tempTree[line[3][unitName[j]]]
                        tempTree = tree
                        for k in range(3):
                            tempTree[line[3][unitName[k]]]['workday'] = addArrays(tempTree[line[3][unitName[k]]]['workday'], line[1])
                            tempTree[line[3][unitName[k]]]['weekend'] = addArrays(tempTree[line[3][unitName[k]]]['weekend'], line[2])
                            if k + 1 != 3:
                                tempTree = tempTree[line[3][unitName[k]]]
                else:
                    tempTree = tree[line[3][unitName[0]]][line[3][unitName[1]]]
                    for j in range(2, len(unitName)):
                        createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                        i += 1
                        tempTree = tempTree[line[3][unitName[j]]]

                    tempTree = tree
                    for k in range(2):
                        tempTree[line[3][unitName[k]]]['workday'] = addArrays(tempTree[line[3][unitName[k]]]['workday'], line[1])
                        tempTree[line[3][unitName[k]]]['weekend'] = addArrays(tempTree[line[3][unitName[k]]]['weekend'], line[2])
                        if k + 1 != 2:
                            tempTree = tempTree[line[3][unitName[k]]]
            else:
                tempTree = tree[line[3][unitName[0]]]
                for j in range(1, len(unitName)):
                    createPath(tempTree, line[3][unitName[j]], line, shortName[j], i)
                    i += 1
                    tempTree = tempTree[line[3][unitName[j]]]
                tempTree = tree
                for k in range(1):
                    tempTree[line[3][unitName[k]]]['workday'] = addArrays(tempTree[line[3][unitName[k]]]['workday'], line[1])
                    tempTree[line[3][unitName[k]]]['weekend'] = addArrays(tempTree[line[3][unitName[k]]]['weekend'], line[2])
                    if k+1 != 1:
                        tempTree = tempTree[line[3][unitName[k]]]
        else:
            tempTree = tree
            for j in range(len(unitName)):
                createPath(tempTree, line[3][unitName[j]],  line, shortName[j], i)
                i += 1
                tempTree = tempTree[line[3][unitName[j]]]
    return tree
"""


#This was used to create the dictionary, code was refactored
def create_dict_refactor(data, tree):
    i = 0;
    unitName = ["NAZ_CZNUTS3", "NAZ_LAU1", "NAZ_OBEC", "NAZ_ZUJ", "NAZ_KU", "NAZ_UTJ", "NAZ_ZSJ"]
    shortName = ["kraj", "lau1", "obec", "zuj", "ku", "tuj", "zsj"]
    for line in data:
        #helper tells us with which unitName we start
        helper = 0
        temp_tree = tree
        #We start with the first key
        key = line[3][unitName[helper]]
        #We cycle through the tree until we find a key that is missing
        #If the key is found, we delve deeper into the tree using the key and move onto the next key
        while key in temp_tree:
            helper += 1
            temp_tree = temp_tree[key]
            key = line[3][unitName[helper]]
        #after we find the missing tree, we continue inside the tree where we left off and create a path
        #all the way to ZSJ
        for j in range(helper, len(unitName)):
            createPath(temp_tree, line[3][unitName[j]], line, shortName[j], i)
            i += 1
            temp_tree = temp_tree[line[3][unitName[j]]]
        tempTree = tree
        #Then we go back and add user numbers all the way to where the last key was found originally
        for k in range(helper):
            tempTree[line[3][unitName[k]]]['workday'] = addArrays(tempTree[line[3][unitName[k]]]['workday'], line[1])
            tempTree[line[3][unitName[k]]]['weekend'] = addArrays(tempTree[line[3][unitName[k]]]['weekend'], line[2])
            if k + 1 != helper:
                tempTree = tempTree[line[3][unitName[k]]]
    return tree

#Helper function, creates a path in the default dictionary
def createPath(tree, path, line, type, id):
    #a new dictionary has to be created inside before we can enter keys
    tree[path] = {}
    tree[path]["name"] = path
    tree[path]["id"] = id
    tree[path]["type"] = type
    tree[path]["workday"] = addArrays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], line[1])
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
        return children
    for key, value in tree.items():
        if(type(tree[key]) is dict):
            #goes through the tree recursively, changes the format to fit our schema
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
#goes through the tree recursicely
def removeSingleNodes(tree):
    for place in tree:
        #if it's the last node, return - only possible for the ZSJ units, every other node will have at least one
        if len(place["children"]) == 0:
            return tree
        removeSingleNodes(place["children"])
        #if it has only one child, replace it with children of the child
        if len(place["children"])==1:
            place["children"] = place["children"][0]["children"]
    return tree

#Sort the children in the tree
#simple insert sort to at least partially sort the tree
def sortEndTree(tree):
    for place in tree:
        if len(place["children"])==0:
            return tree
        sortEndTree(place['children'])
        for i in range(len(place['children'])):
            index = i
            for j in range(i, len(place['children'])):
                if place['children'][j]['name'] < place['children'][index]['name']:
                    index = j
            if index != i:
                placeholder = place['children'][i]
                place['children'][i] = place['children'][index]
                place['children'][index] = placeholder
        return tree
    return tree


#simple main method that acceps at least some command line arguments, in case different data need to be sorted
def createJSON():
    if len(sys.argv) == 2:
        inputfile = sys.argv[1]
        outputfile = "Zones.json"
    elif len(sys.argv) == 3:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]
    elif len(sys.argv)>3:
        logging.error("Too many arguments \n1:Input file \n 2:Output file")
        sys.exit(1)
    else:
        inputfile = "bmo_db.csv"
        outputfile = "Zones.json"
    zuj = "ZUJ.csv"
    if not os.path.isfile(inputfile):
        logging.error("Invalid path to csv source")
        sys.exit(1)
    if not os.path.isfile(zuj):
        logging.error("Cannot find ZUJ in directory, please check if it's present")
        sys.exit(1)
    processsing = groupByCode(dataLoad(inputfile))
    zujDict = getZujData(zuj)
    processsing = mergeDataSets(processsing, zujDict)
    processsing = create_dict_refactor(processsing, tree())
    processsing = (changeFormat(processsing))
    processsing = removeSingleNodes(processsing)
    #processsing = sortEndTree(processsing)
    final = {}
    final["data"] = processsing
    with open(outputfile, "w", encoding="utf8") as jsonFile:
        json.dump(final, jsonFile, ensure_ascii=False)





if __name__ == "__main__":
    createJSON();

