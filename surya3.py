import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

# Display a bar chart of total grade points by department
st.write('Total grade points by department')
dept_grade_points = data.groupby('Dept')['Grade'].sum()
st.bar_chart(dept_grade_points)

# Display a pie chart of grades by subject
st.write('Grades by subject (percentage)')
subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
fig, ax = plt.subplots()
ax.pie(subject_grade_percentages, autopct='%1.1f%%')
ax.set_title('Percentage of grades by subject')
ax.legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
st.pyplot(fig)

# Display a bar chart of highest grades by subject
st.write('Highest grade by subject')
subject_max_grades = data.groupby('Subname')['Grade'].max()
st.bar_chart(subject_max_grades)

# Display a table of top N grades (excluding F, E, D, C, B, ABSENT, and COMPLE)
N = 10
filtered_data = data[~data['Grade'].isin(['F', 'E', 'D', 'C', 'B', 'ABSENT', 'COMPLE'])]
top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
st.write(f'Top {N} grades (excluding F, E, D, C, B, ABSENT, and COMPLE)')
st.table(top_grades)
