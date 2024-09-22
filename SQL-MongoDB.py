import pymongo
import mysql.connector             #sql1 to mongo2
database_name_1=input("Enter the name of the database you want to convert from SQL: ")
table_name_1= input("Enter the table name you want to convert into collections from SQL: ")
database_name_2=input("Enter the name of the database you want in MongoDB: ")
table_name_2=input("Enter the name of the new collection: ")

mydb = mysql.connector.connect(
    host = "localhost",
    username="root",
    password=os.getenv("DB_PASSWORD", ""),
    port = 3306,
    database =database_name_1
)
#mydb = mysql.connector.connect(
    #host=os.getenv("DB_HOST", "localhost"),
    #username=os.getenv("DB_USER", "root"),
    #password=os.getenv("DB_PASSWORD", ""),
    #port=os.getenv("DB_PORT", 3306),
    #database=os.getenv("DB_NAME", "database_name_1")
#)

mycursor = mydb.cursor(dictionary=True)
query2 =(f"select * from {table_name_1}")
mycursor.execute(query2)
results1 = mycursor.fetchall()

#mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient[database_name_2]
mycollection =mydb[table_name_2]

for i in results1:
    mydict = i
    mycollection.insert_one(mydict)
print("Converted")
