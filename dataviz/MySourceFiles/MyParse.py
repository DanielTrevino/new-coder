"""
Data Visualization Project
Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.
Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.
Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.
"""

import csv


# Put the full path to your CSV/Excel file here
MY_FILE = "C:/users/hustlecrowe/projects/new-coder/dataviz/data/sample_sfpd_incident_all.csv"
WARRANT_FILE = "C:/users/hustlecrowe/projects/new-coder/dataviz/mysourcefiles/warrantfile.txt"
def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-like object"""

	# Open CSV file
	opened_file = open(raw_file)

	# Read the CSV data
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# Setup an empty list
	parsed_data = []
	# Skip over the first line of the file for the headers
	fields = csv_data.next()

	# Iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close the CSV file
	opened_file.close()

	return parsed_data
def warrantarrestparse(newd):

	f = open(WARRANT_FILE, 'w')
	for dict_item in newd:
		if dict_item["Descript"] == "WARRANT ARREST":
			#print dict_item["DayOfWeek"]
			#f.write 
			print dict_item
			print "--------"
			print "--------"
			print dict_item.keys()
			print "--------"
			print "--------"
			print dict_item.values()
			print "--------"
			print "--------"
		#else :
			#print "N/A"
		#print "I got here"

def main():
	# Call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")
	my_data = warrantarrestparse(new_data)

	# Let's see what the data looks like!
	#print new_data
	print my_data
if __name__ == "__main__":
	main()