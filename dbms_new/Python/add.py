import streamlit as st
import pandas as pd
from datetime import date,timedelta
from database import get_student_no
from database import get_course_no
from database import add_student
from database import add_drug
from database import add_paint
from database import add_course
from database import add_faculty
from database import add_reg
from database import viewTables

def add():
    menu = ["Student", "Faculty","Course","Registred Courses"]
    choice = st.sidebar.selectbox("**Menu**", menu)
    min_date = date(2000, 1, 1)
    max_date = date.today() - timedelta(days=6574) 
    current_year = date.today().year
    default_date = date(2002, 1, 1) 
# Display the date input with the specified range

    #Student
    if choice==menu[0]:
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("Student ID(format->S000) :",)
            student_name = st.text_input("Student Name: ")
            gender = st.selectbox("Gender: ", ["Male","Female"])
            birth_date = st.date_input("Date of Birth:", min_value=min_date, max_value=max_date,value=default_date)
        with col2:
            dnumber = st.selectbox("Department Number:", list(range(1, 6)))
            sem = st.selectbox("Semester:", list(range(1, 9)))
            sec = st.selectbox("Section: ",["A","B","C"])

        if st.button("Add Student"):
            add_student(student_id, student_name, gender, birth_date,dnumber,sem,sec)
            st.success("Successfully added student: {}".format(student_name))
    
    #Faculty
    if choice==menu[1]:
        col1, col2 = st.columns(2)
        with col1:
            faculty_id = st.text_input("Faculty ID(Format->F000)")
            faculty_name = st.text_input("Faculty Name")
            designation = st.selectbox("Designation", ["Professor ", "Assistant Professor","Associate Professor "])
        with col2:
            salary = st.number_input("Salary:")
            dnumber = st.selectbox("Department Number:", list(range(1, 6)))
            joined = st.date_input("Joined:", value=date(current_year, 1, 1), min_value=date(1990, 1, 1), max_value=date(current_year, 12, 31)).year


        if st.button("Add Faculty Member"):
            add_faculty(faculty_id, faculty_name, designation, salary, dnumber,joined)
            st.success("Successfully added case: {}".format(faculty_name))

    #Course
    if choice==menu[2]:
        col1, col2 = st.columns(2)
        with col1:
            course_number = st.text_input("Course ID(format->C000):")
            course_name = st.text_input("Course Name:")
            number_of_credits = st.selectbox("Number of Credits:", list(range(1, 6)))
        with col2:
            dnumber = st.selectbox("Department Number:", list(range(1, 6)))
            sem = st.selectbox("Semester:", list(range(1, 9)))
        if st.button("Add Course"):
            add_course(course_number,course_name,number_of_credits,sem,dnumber)
            st.success("Successfully added a course: {}".format(course_name))

    #Register
    if choice==menu[3]: 
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.selectbox("Student ID :", [i[0] for i in get_student_no()])
            course_number = st.selectbox("Course ID :", [i[0] for i in get_course_no()])
            marks = st.number_input("Enter Grade:")
        
        if st.button("Add Student Registered Course"):
            add_reg(student_id, course_number,marks)
            st.success("Successfully Added")

    with st.expander("View Updated Table"):
        result = viewTables(choice)
        df = pd.DataFrame(result) 
        st.dataframe(df)