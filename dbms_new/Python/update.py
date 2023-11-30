import streamlit as st
from database import updateStatus,get_student_no, get_faculty_no
from database import viewTables
import pandas as pd


def update():
    menu = ["Student", "Faculty"]
    choice = st.sidebar.selectbox("**Menu**", menu)
    result = viewTables(choice)
    #print(result)
    if choice==menu[0]:
        df = pd.DataFrame(result, columns=("Student ID", "Student Name", "Gender","DOB", "Department Number", "Semester","Section")) 
    elif choice==menu[1]:
        df = pd.DataFrame(result, columns=("Faculty ID", "Faculty Name", "Designation", "Salary", "Department Number", "Join Year"))
    st.dataframe(df)
    c1, c2, c3 = st.columns(3)
    with c1:
        if (choice=="Student"):
            id=st.selectbox("Enter Student ID", [i[0] for i in get_student_no()])
        elif(choice=="Faculty"):
            id=st.selectbox("Enter Faculty ID", [i[0] for i in get_faculty_no()])
    with c2:
        if (choice=="Student"):
            status1 = st.selectbox("Semester:", list(range(1, 9)))
        elif(choice=="Faculty"):
            status1 = st.selectbox("Designation", ["Professor ", "Assistant Professor","Associate Professor "])
    with c3:
        if (choice=="Student"):
            status2 = st.selectbox("Section: ",["A","B","C"])
        elif(choice=="Faculty"):
            status2 = st.number_input("Salary:")
    if st.button("Update Record"):
            updateStatus(id, status1,status2, choice)
            st.success("Successfully updated record")
    result = viewTables(choice)
    df = pd.DataFrame(result)