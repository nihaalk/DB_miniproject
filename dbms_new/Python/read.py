import streamlit as st
import pandas as pd
from database import viewTables

def read():
    menu = ["Student", "Faculty", "Department", "Course", "FA", "Hostel","Rooms"]
    choice = st.sidebar.selectbox("**Menu**", menu)
    result = viewTables(choice)
    #print(result)
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Student ID", "Student Name", "Gender","DOB", "Department Number", "Semester","Section")) 
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Faculty ID", "Faculty Name", "Designation", "Salary", "Department Number", "Join Year"))
    elif choice==menu[2]:
        df = pd.DataFrame(result, columns=("Department Number", "Department Name"))
    elif choice==menu[3]:
        df = pd.DataFrame(result, columns=("Course ID", "Course Name", "Number of Credits", "Semester", "Department Number"))
    elif choice==menu[4]:
        df = pd.DataFrame(result, columns=("Faculty ID", "Student ID"))
    elif choice==menu[5]:
        df = pd.DataFrame(result, columns=("Hostel ID", "Hostel Name", "Capacity", "Fees"))
    elif choice==menu[6]:
        df = pd.DataFrame(result, columns=("Hostel ID", "Student ID", "Room No"))
    st.dataframe(df)
