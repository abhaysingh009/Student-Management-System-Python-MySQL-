import pymysql as sq
import time

#Stablish connection
con=sq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
mycur=con.cursor()
#create table if not exist
create='''create table if not exists Student  (
        st_roll INT PRIMARY KEY ,
        st_name varchar(40),
        st_email varchar(50),
        st_marks INT
)'''
mycur.execute(create)

while True:
    try:
        print("Enter Your Choice-->")
        choice=int(input("1.Add Student\n2.Delete Student\n3.Update Student\n4.Display Student\n5.Display All\n6.Exit...\n"))

#insert values
        if(choice==1):
            roll=int(input("Enter the Roll Number: "))
            name=input("Enter the Name: ")
            email=input("Enter the Email: ")

            if "@gmail.com" not in email:
                print("Enter a Valid Email !")
                continue

            marks=int(input("Enter Marks: "))
            if(marks<0 or marks>100):
                print("Enter valid marks ! ")
                continue
            #Query to insert
            q="Insert into Student Values(%s,%s,%s,%s)"
            x= mycur.execute(q,(roll,name,email,marks))

            if(x>0):
                print("Student Added Successfully !")
                con.commit()
            else:
                print("Faild to Add !")
#Delete Student
        elif(choice==2):  
            roll=int(input("Enter Student's Roll Number: "))
            q="Delete From Student where st_roll=%s"
            x=mycur.execute(q,(roll,))
            if(x>0):
                print("Student Deleted Successfully !")
                con.commit()
            else:
                print("Faild to Delete !")

#Update Student    
        elif(choice==3):
            #Take roll no 
            roll=int(input("Enter Student's Roll Number: "))
            #take updated values
            name=input("Enter New Name: ")
            email=input("Enter New Email: ")
            if "@gmail.com" not in email:
                print("Enter a Valid Email !")
                continue
            marks=int(input("Enter  New Marks: "))
            if(marks<0 or marks>100):
                print("Enter valid marks ! ")
                continue

            #update query
            q="Update student set st_name=%s,st_email=%s,st_marks=%s where st_roll=%s"
            x=mycur.execute(q,(name,email,marks,roll))
            if(x>0):
                print("Student Updated Successfully !")
                con.commit()
            else:
                print("Faild to Update !")



#Display Student
        elif(choice==4):
            roll=int(input("Enter Roll Number of Student: "))
            q="Select * From Student Where st_roll=%s" 
            mycur.execute(q,(roll,))
            res=mycur.fetchone()
            if res is None:
                print("No Students Found !")
                continue
            print(f"Roll No: {res[0]}, Name: {res[1]}, Email: {res[2]}, Marks: {res[3]}")

#Display All
        elif(choice==5): 
            q="Select * From Student" 
            mycur.execute(q)
            res=mycur.fetchall()
            if(len(res)==0):
                print("No Students Found")
                continue
            for i in res:
                print(f"Roll No: {i[0]}, Name: {i[1]}, Email: {i[2]}, Marks: {i[3]}")

#Exit                
        elif(choice==6):
            print("Exiting...")
            time.sleep(3)
            break; 
#Error handling
        else :
            print("Enter a Valid  choice!")
    except sq.err.IntegrityError:
        print("Duplicate Entry !")
    except Exception as e:
        print("Erorr: " ,e)
con.close()
print("Exited Successfully!")
# insert values 
# insert="I"
# display values 
# delete values