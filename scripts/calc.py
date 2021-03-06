#! /usr/bin/python
import re #Allow using regular expressions


Data = raw_input("Please specify the week again (e.g. 201549): ")
Data = Data + ".csv"


#Open the right file (ADD OPTION TO SPECIFY WEEK)
Week = open(Data,'r') #Open the file of the week to read in

SUMhTotal = 0	#Set the sum of total worked hours as a variable and start at 0
SUMhNormal = 0	#Set the sum of total worked hours excluding overtime etc. as a variable and start at 0

for Line in Week:
	SearchStr = '[^\t]+\t[^\t]+\t[^\t]+\t[^\t]+\t([^\t]+)\t([^\t]+)$'
	Result = re.search(SearchStr, Line)
	hTotal = float(Result.group(1))
	hNormal = float(Result.group(2))
	SUMhTotal = SUMhTotal + hTotal
	SUMhNormal = SUMhNormal + hNormal
	Overtime = SUMhTotal - SUMhNormal

print "Week %s had a total of %.2f worked hours" % (Data, SUMhTotal)	#print with 2 decimals
print "Of which %.2f were over-time" % Overtime		#print with 2 decimals
