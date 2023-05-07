import pandas as pd
import altair as alt
import streamlit as st

# Load the data
df = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\2-1.xlsx")

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

# Find the highest grade
highest_grade = df['Grade'].max()

# Calculate the number of students
num_students = df['Htno'].nunique()

# Divide data by branch
ece_data = df[df['Subcode'].str.contains('40[1-9]')]
cse_data = df[df['Subcode'].str.contains('50[1-9]')]

# Create a dropdown menu to select branch
selected_branch = st.sidebar.selectbox(
    'Select a branch',
    ['All', 'ECE', 'CSE']
)

# Visualize the selected branch grades
if selected_branch == 'All':
    # Show the overall grade distribution
    pass
elif selected_branch == 'ECE':
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
elif selected_branch == 'CSE':
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
