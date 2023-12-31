import streamlit as st
import pandas as pd
import plotly.express as px
from database import viewQueryResult
from database import viewTables
from database import execQuery

def predef_queries():
    q = [   "Tenure of each Teacher", 
            "Number of students residing in each Hostel", 
            "Number of Students in each Department",
            "Faculty Members who are not Faculty Advisors",
            "Professors",
            "Student's SGPA",
            "Teachers with greater than average salary for their department",
            "Revenue Generated by a Bus"]
    
    choice = st.selectbox("**Choose a Query:** ", q)
    print(choice)
    result = viewQueryResult(q.index(choice)+1)
    #print(result)
    if(choice==q[0]):
        df = pd.DataFrame(result, columns=("Teacher Name", "Department Number", "Working For"))
        st.dataframe(df)
    elif(choice==q[1]):
        df = pd.DataFrame(result, columns=("Hostel Name", "Number of Students"))
        st.dataframe(df)
    elif(choice==q[2]):
        df = pd.DataFrame(result, columns=("Department Name", "Number of Students"))
        st.dataframe(df)
    elif(choice==q[3]):
        df = pd.DataFrame(result, columns=("Faculty Id", "Faculty Name"))
        st.dataframe(df)
    elif(choice==q[4]):
        df = pd.DataFrame(result, columns=("Faculty Id", "Faculty Name","Designation","Department Name"))
        st.dataframe(df)
    elif(choice==q[5]):
        df = pd.DataFrame(result, columns=["SGPA"])
        st.dataframe(df)
    elif(choice==q[6]):
        df = pd.DataFrame(result, columns=["Faculty Name"])
        st.dataframe(df)
    elif(choice==q[7]):
        print(result)
        df = pd.DataFrame(result, columns=["Revenue Generated by the Bus"])
        st.dataframe(df)
    
def query_cmd():
    command = st.text_input("Enter Query")
    if command:
        result = execQuery(command)
        #print(result)
        df = pd.DataFrame(result) 
        st.dataframe(df)

    