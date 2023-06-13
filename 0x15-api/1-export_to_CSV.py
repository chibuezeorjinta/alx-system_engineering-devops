#!/usr/bin/python3
"""Introduction to API's using python"""
import csv
import requests
import sys

if __name__ == "__main__":
	"""function entry to avoid issues"""
	TOTAL_NUMBER_OF_TASKS = 0
	NUMBER_OF_DONE_TASKS = 0

	employeeID = int(sys.argv[1])

	users = requests.get('https://jsonplaceholder.typicode.com/users')
	employee = users.json()

	"""get employee name"""
	for i in employee:
		if i["id"] == employeeID:
			EMPLOYEE_NAME = i["name"]

	"""print todos"""
	response = requests.get(
		'https://jsonplaceholder.typicode.com/todos/{}/todos'.format(
                                                                     employeeID))
	TODO = response.json()
	for entry in TODO:
		TOTAL_NUMBER_OF_TASKS += 1
		if entry["completed"] is True:
			NUMBER_OF_DONE_TASKS += 1
	#print("Employee {} is done with tasks".format(EMPLOYEE_NAME) +
	#	"({}/{}):".format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
	#for entry in TODO:
	#	print("\t " + entry.get("title"))
	
	filename = str(employeeID) + '.csv'
	with open(filename, mode='w') as f:
		writer = csv.writer(f, delimiter=',', quotechar='"',
							quoting=csv.QUOTE_ALL, lineterminator='\n')
		for task in TODO:
			if task.get('userId') == int(employeeID):
				writer.writerow([employeeID, EMPLOYEE_NAME, str(task.get('completed')),
								 task.get('title')])
