# dataTransformation

A python script that transforms csv data to a JSON file to be used by mobile-presence application.

https://github.com/jirmed/mobile-presence

# Data

Script uses data which can be found in bmo_db.csv, the source of which can be found here.

https://data.brno.cz/dataset/?id=data-mobilnich-operatoru-pritomne-obyvatelstvo

These are data from mobile operators, tracking the presence of people in ZSJ units, which are small administrative units, during workdays and weekends.

The script finds the parent administrative units to each ZSJ, using the data which can be found in ZUJ.csv data file. ZUJ.csv contains information about administrative units in the Czech republic, the source of this data is ArcGIS.

# Command line argument

If ran though terminal, you can enter two arguments

First one should be the path to the source data, for which you would like to find parent administrative units. It must have the same structure as bmo_db.csv. If missing, the script will use bmo_db.csv as input data.

Second one is the path to the output file - if you wish to have the output written into a different file. If it is missing, the script will write the output into Zones.json by default.

# Output

The script enters the output into the Zones.json file.
