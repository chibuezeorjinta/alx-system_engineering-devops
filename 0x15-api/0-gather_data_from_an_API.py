#!/usr/bin/python3
"""Introduction to API's using python"""
import requests
import sys

TOTAL_NUMBER_OF_TASKS = 0
NUMBER_OF_DONE_TASKS = 0

if len(sys.argv) == 2:
    employeeID = int(sys.argv[1])
else:
    print("input integer")
users = requests.get('https://jsonplaceholder.typicode.com/users')
employee = users.json()

"""get employee name"""
for i in employee:
    if i["id"] == employeeID:
        EMPLOYEE_NAME = i["name"]

"""print todos"""
response = requests.get(
    f'https://jsonplaceholder.typicode.com/todos/{employeeID}/todos')
TODO = response.json()
for entry in TODO:
    TOTAL_NUMBER_OF_TASKS += 1
    if entry["completed"] is True:
        NUMBER_OF_DONE_TASKS += 1
print(f"Employee {EMPLOYEE_NAME} is done with tasks" +
      "({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
for entry in TODO:
    print("\t " + entry.get("title"))
