import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="amirbaxxter",
    password="Amir@13761376",
    database="test"
)
mycursor = mydb.cursor()
sql = "insert into users (first_name,last_name,email,age) values (%s, %s, %s, %s)"
first_name = "amir"
last_name = "ahmadi"
email = "test@gmail.com.com"
age = "20"
val = (first_name, last_name, email, age)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
# mycursor.execute("select * from users")

# my_result = mycursor.fetchall()
# for i in my_result:
#     print(i)