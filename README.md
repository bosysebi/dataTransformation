# dataTransformation

A python script that transforms csv data to a JSON file to be used by mobile-presence application.

https://github.com/jirmed/mobile-presence

# Data

Script uses data which can be found in bmo_db.csv, the source of which can be found here.

https://data.brno.cz/dataset/?id=data-mobilnich-operatoru-pritomne-obyvatelstvo

These are data from mobile operators, tracking the presence of people in ZSJ units, which are small administrative units, during workdays and weekends.

The script finds the parent administrative units to each ZSJ, using the data which can be found in ZUJ.csv data file. ZUJ.csv contains information about administrative units in the Czech republic, the source of this data is ArcGIS.
