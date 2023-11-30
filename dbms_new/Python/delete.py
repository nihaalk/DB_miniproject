import streamlit as st
from database import delRec
from database import viewTables
import pandas as pd
from database import get_course_no
from database import get_faculty_no
from database import get_student_no, get_department_no,get_hostel_no


def delete():
    menu = ["Student", "Faculty", "Course", "Hostel"]
    choice = st.sidebar.selectbox("**Menu**", menu)
    result = viewTables(choice)
    df = pd.DataFrame(result)
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Student ID", "Student Name", "Gender","DOB", "Department Number", "Semester","Section")) 
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Faculty ID", "Faculty Name", "Designation", "Salary", "Department Number", "Join Year"))
    elif choice==menu[2]:
        df = pd.DataFrame(result, columns=("Course ID", "Course Name", "Number of Credits", "Semester", "Department Number"))
    elif choice==menu[3]:
         df = pd.DataFrame(result, columns=("Hostel ID", "Hostel Name", "Capacity", "Fees"))
    st.dataframe(df)
    list_of_id=[]
    if choice=="Student":
        list_of_id = [i[0] for i in get_student_no()]
    elif choice=="Faculty":
        list_of_id = [i[0] for i in get_faculty_no()]
    elif choice=="Course":
        list_of_id = [i[0] for i in get_course_no()]
    elif choice=="Department":
        list_of_id = [i[0] for i in get_department_no()] 
    elif choice=="Hostel":
          list_of_id = [i[0] for i in get_hostel_no()]
    id=st.selectbox("Enter ID", list_of_id)
    if st.button("Delete Record"):
            delRec(id, choice)
            st.success("Successfully deleted record")
    