import mysql.connector 
import streamlit as st

mydb = mysql.connector.connect(host="localhost", user="root", password="Guruprasad123", database="studentmanagementsystem")
c = mydb.cursor()

def viewTables(tableName):
    command = 'SELECT * FROM ' + tableName +';'
    print(command)
    c.execute(command)
    data = c.fetchall()
    return data

def updateStatus(id, status1,status2, choice):
    if choice=="Student":
        command = 'UPDATE student set sem = "' + str(status1) + '" where student_ID = "' + id + '"'
        command2 = 'update student set sec = "' +status2+'"where student_ID = "' + id + '"'
    elif choice=="Faculty":
        command = 'UPDATE faculty set designation = "' + status1 + '" where faculty_ID = "' + id + '"'
        command2 = 'UPDATE faculty set salary = "' + str(status2) + '" where faculty_ID = "' + id + '"'
    print(command)
    c.execute(command)
    print(command2)
    c.execute(command2)
    mydb.commit()


def execQuery(command):
    c.execute(command)
    data = c.fetchall()
    return data

def viewQueryResult(choice):
    command=""
    if choice==1:
        command = 'SELECT faculty_name AS Teacher_Name,dnumber AS Department_Number,YEAR(CURRENT_DATE) - joined AS Years_Working FROM faculty;'
    elif choice==2:
        command = 'SELECT hostel_name, COUNT(*) AS Number_of_Students FROM rooms natural join hostel GROUP BY hostel_id;'
    elif choice==3:
        command = 'SELECT department_name AS Department_Name,COUNT(*) AS Number_of_Students FROM student natural join department GROUP BY dnumber;'
    elif choice==4:
        command = 'SELECT f.faculty_id,f.faculty_name FROM faculty f LEFT JOIN fa ON f.faculty_id = fa.faculty_id WHERE fa.faculty_id IS NULL;'
    elif choice==5:
        command = "SELECT faculty_id, faculty_name, designation, department_name FROM faculty NATURAL JOIN department WHERE designation = 'professor';"
    elif choice==6:
        c.execute('select student_id from student;')
        s_ids =[row[0] for row in c.fetchall()]
        selected_s_id = st.selectbox("Select Student ID", s_ids)
        st.write(f"You selected bus ID: {selected_s_id}")

        command = f"SELECT calculate_sgpa('{selected_s_id}') as SGPA;"
    elif choice==7:
        command = 'SELECT faculty_name FROM faculty f WHERE salary > (SELECT AVG(salary) FROM faculty WHERE dnumber = f.dnumber);'
    elif choice==8:
        c.execute("SELECT b_id FROM bus")
        bus_ids = [row[0] for row in c.fetchall()]
        selected_bus_id = st.selectbox("Select Bus ID", bus_ids)
        st.write(f"You selected bus ID: {selected_bus_id}")
        command = f"SELECT calculate_bus_revenue('{selected_bus_id}') as BR;"
    c.execute(command)
    data = c.fetchall()
    return data

def get_student_no(): 
    c.execute('SELECT student_id FROM student') 
    data = c.fetchall()
    return data

def get_course_no(): 
    c.execute('SELECT course_number FROM course') 
    data = c.fetchall()
    return data

def get_faculty_no(): 
    c.execute('SELECT faculty_id FROM faculty') 
    data = c.fetchall()
    return data

def get_department_no(): 
    c.execute('SELECT dnumber FROM department') 
    data = c.fetchall()
    return data

def get_hostel_no(): 
    c.execute('SELECT hostel_id FROM hostel') 
    data = c.fetchall()
    return data

def get_paint_no(): 
    c.execute('SELECT PID FROM PAINT') 
    data = c.fetchall()
    return data

def delRec(id, choice):
    if choice=="Student":
        command = 'DELETE FROM student where student_ID = "' + id + '"'
    elif choice=="Faculty":
        command = 'DELETE FROM faculty where faculty_ID = "' + id + '"'
    elif choice=="Department":
        command = 'DELETE FROM department where dnumber = "' + str(id) + '"'
    elif choice=="Course":
        command = 'DELETE FROM course where course_number = "' + id + '"'
    elif choice=="Hostel":
        command = 'DELETE FROM hostel WHERE hostel_ID = "' + id + '"'
    
    print(command)
    c.execute(command)
    mydb.commit()

def add_student(student_id, student_name, gender, birth_date,dnumber,sem,sec):
    command = 'INSERT INTO student VALUES("'+student_id+'","'+student_name+'","'+gender+'","'+str(birth_date)+'","'+str(dnumber)+'","'+str(sem)+'","'+sec+'");'
    #print(command)
    c.execute(command)
    mydb.commit()

def add_reg(student_id, course_number,marks):
    command = 'Insert INTO  registered VALUES("'+student_id+'","'+course_number+'","'+str(marks)+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def add_faculty(faculty_id, faculty_name, designation, salary, dnumber,joined):
    command = 'Insert INTO faculty VALUES("'+faculty_id+'","'+faculty_name+'","'+designation+'","'+str(salary)+'","'+str(dnumber)+'","'+str(joined)+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def add_course(course_number,course_name,number_of_credits,dnumber, sem):
    command = 'INSERT INTO course VALUES("'+course_number+'","'+course_name+'","'+str(number_of_credits)+'","'+str(dnumber)+'","'+str(sem)+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def add_drug(cid, code, name, color, dclass, narc):
    command = 'INSERT INTO DRUGS VALUES("'+cid+'","'+code+'","'+name+'","'+color+'","'+dclass+'","'+narc+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def add_paint(cid, id, col, sol, bind, pigment, add):
    command = 'INSERT INTO PAINT VALUES("'+cid+'","'+id+'","'+col+'","'+sol+'","'+bind+'","'+pigment+'","'+add+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def add_criminalcase(cid, id):
    command = 'INSERT INTO CriminalCase VALUES("'+cid+'","'+id+'");'
    print(command)
    c.execute(command)
    mydb.commit()



