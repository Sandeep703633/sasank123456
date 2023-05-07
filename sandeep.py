import pandas as pd
import altair as alt
import streamlit as st

# Load the data
df = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\2-1.xlsx")

# Create a sidebar with buttons for navigation
nav = st.sidebar.radio("Navigate to", ["All Grades", "ECE Grades", "CSE Grades"])

if nav == "All Grades":
    # Visualize the number of high grades for all students
    fig1 = alt.Chart(df).mark_bar().encode(
        alt.X('Grade', bin=False),
        y='count()',
        color='Grade'
    ).properties(
        width=500,
        height=300,
        title='Number of Grades by Grade'
    )
    st.altair_chart(fig1, use_container_width=True)

elif nav == "ECE Grades":
    # Divide data by branch
    ece_data = df[df['Subcode'].str.contains('40[1-9]')]

    # Visualize the ECE grades
    fig2 = alt.Chart(ece_data).mark_bar().encode(
        alt.X('Grade', bin=False),
        y='count()',
        color='Grade'
    ).properties(
        width=500,
        height=300,
        title='Number of ECE Grades by Grade'
    )
    st.altair_chart(fig2, use_container_width=True)

elif nav == "CSE Grades":
    # Divide data by branch
    cse_data = df[df['Subcode'].str.contains('50[1-9]')]

    # Visualize the CSE grades
    fig3 = alt.Chart(cse_data).mark_bar().encode(
        alt.X('Grade', bin=False),
        y='count()',
        color='Grade'
    ).properties(
        width=500,
        height=300,
        title='Number of CSE Grades by Grade'
    )
    st.altair_chart(fig3, use_container_width=True)
