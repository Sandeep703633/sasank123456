import streamlit as st
import pandas as pd

# Load the dataset from an Excel file
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\surya.xlsx")

# Bar chart of total grade points by department
st.write('Total grade points by department')
dept_points = data.groupby('Dept')['Grade'].sum()
st.bar_chart(dept_points)
print(dept_points)


# Bar chart of highest grades by subject
st.write('Highest grade by subject')
subject_grades = data.groupby('Subname')['Grade'].max()
st.bar_chart(subject_grades)


# Table of top N grades
N = 10
top_grades = data.sort_values('Grade', ascending=False).head(N)
st.table(top_grades)
st.write(f'Top {N} grades')
# Pie chart of grades by subject
subject_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
fig, ax = plt.subplots()
ax.pie(subject_percentages, labels=subject_percentages.index, autopct='%1.1f%%')
ax.set_title('Percentage of grades by subject')
st.pyplot(fig)
