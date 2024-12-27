from flask import Flask,jsonify, request
import pymysql

import pymysql.cursors

import mysql.connector

db = pymysql.connect(host="localhost", user="root", password="Naresh@954255", db="classicmodels")
# db=mysql.connector.connect(host="localhost", user="root", password="naresh123" )
# cursor = db.cursor()
app = Flask(__name__)

 
@app.route("/api/office/",methods=['GET'])
def get_offices():
    cursor = db.cursor(pymysql.cursors.DictCursor)
    query = "SELECT * FROM offices"
    cursor.execute(query)
    results = cursor.fetchall()
    print("query...", results)
    return jsonify(ok=True, data=results)


@app.route("/api/get_office_employees/<officeCode>/",methods=['GET'])
def get_clicked_employee(officeCode):
    cursor=db.cursor(pymysql.cursors.DictCursor)
    query=f"SELECT * FROM employees WHERE officeCode={officeCode}"
    cursor.execute(query)
    result=cursor.fetchall()
    return jsonify(ok=True,data=result)


@app.route("/api/new_employee/<officeCode>/",methods=['POST'])
def add_new_employee(officeCode):
 
    data=request.get_json()
    print(data)
    employeeNumber=int(data['employeeNumber'])
    firstName=data['firstName']
    lastName=data['lastName']
    extension=data['extension']
    email=data['email']
    officeCode=data['officeCode']
    reportsTo=int(data['reportsTo'])
    jobTitle=data['jobTitle']
    cursor = db.cursor()
    
    countprimarykey=f"SELECT COUNT(*) FROM employees WHERE employeeNumber={employeeNumber}"
    cursor.execute(countprimarykey)
    result = cursor.fetchone()
    print(result)
    if result[0] > 0:
        print(result)
        return jsonify(ok=False, error="Employee with same id already exists!")
    else:
        query=f"INSERT INTO employees (employeeNumber,firstName,lastName,extension,email,officeCode,reportsTo,jobTitle) VALUES ({employeeNumber},'{firstName}','{lastName}','{extension}','{email}',{officeCode},{reportsTo},'{jobTitle}')"
        # query="INSERT INTO employees (employeeNumber,firstName,lastName,extension,email,officeCode,reportsTo,jobTitle) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,)"
        cursor.execute(query)
        db.commit()
        cursor.close()
        return jsonify(ok=True)
        
         
if __name__=="__main__":
    app.run(debug=True)

