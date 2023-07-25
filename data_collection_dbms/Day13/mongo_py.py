from pymongo import MongoClient
client=MongoClient("mongodb://127.0.0.1:27017")
db=client['dbda']
emp=db['emp']

def getAllEmp():
    emps=emp.find();
    for e in emps:
        print(e['_id'],",",e['ename'],",",e['sal'])

def addNewEmp():
    newEmp={'_id':101,'ename':'Nita','sal':1000,'job':'trainner','deptno':20}
    emp.insert_one(newEmp)
    print("insreted ...")

def deleteEmp():
    emp.delete_one({'_id':7369})
    print("emp deleted ...")


def updateEmp():
    emp.update_one({'_id':101 },{"$set":{'ename':"Neeta"}})
    print("emp updated ...")


# getAllEmp()
# addNewEmp()
# getAllEmp()
# deleteEmp()
# getAllEmp()
updateEmp()
getAllEmp()
