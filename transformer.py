import csv
import json

# read csv and add to dictionary
bmo = "bmo_db.csv"
testJson = "Zones.json"

data = {}
with open(bmo) as bmo:
    csvReader = csv.DictReader(bmo, delimiter=";")
    for bmoRow in csvReader:
        ZSJ = bmoRow["KOD_ZSJ_P"]
        data[ZSJ] = bmoRow

with open(testJson, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))

print(data)