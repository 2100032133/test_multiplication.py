from pymongo import MongoClient
# import mongo client to connect
import pprint 
#Creating instance of mongoClinet 
client = MongoClient()
#Creating database
db = client.java
employee = {"id":"101","name":"CSE","profession":"SE"}
#Creating document
employees = db.employees
#inserting data
employees.insert_one(employee)
#fetching data
pprint.pprint(employees.find_one())