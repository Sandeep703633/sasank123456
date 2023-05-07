import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from an Excel file
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\surya.xlsx")

# Bar chart of total grade points by department
dept_points = data.groupby('Dept')['Grade'].sum()
fig, ax = plt.subplots()
ax.bar(dept_points.index, dept_points.values, color=['blue', 'orange', 'green', 'red'])
ax.set_title('Total grade points by department')
for i, v in enumerate(dept_points.values):
    ax.text(i, v, str(v), ha='center', va='bottom')
st.pyplot(fig)

# Bar chart of highest grades by subject
subject_grades = data.groupby('Subname')['Grade'].max()
fig, ax = plt.subplots()
ax.bar(subject_grades.index, subject_grades.values, color=['purple', 'pink', 'cyan', 'magenta'])
ax.set_title('Highest grade by subject')
for i, v in enumerate(subject_grades.values):
    ax.text(i, v, str(v), ha='center', va='bottom')
st.pyplot(fig)

# Pie chart of grades by subject
subject_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
fig, ax = plt.subplots()
ax.pie(subject_percentages, labels=subject_percentages.index, autopct='%1.1f%%')
ax.set_title('Percentage of grades by subject')
st.pyplot(fig)

# Table of top N grades
N = 10
top_grades = data.sort_values('Grade', ascending=False).head(N)
top_grades = top_grades.reset_index(drop=True)
top_grades.index += 1 
st.table(top_grades.style.hide_index())
st.write(f'Top {N} grades')
