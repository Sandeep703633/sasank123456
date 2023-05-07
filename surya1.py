import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from an Excel file
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

# Bar chart of total grade points by department
st.write('Total grade points by department')
dept_points = data.groupby('Dept')['Grade'].sum()
st.bar_chart(dept_points)

# Pie chart of grades by subject
subject_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
fig, ax = plt.subplots()
ax.pie(subject_percentages, labels=subject_percentages.index, autopct='%1.1f%%')
ax.set_title('Percentage of grades by subject')
st.pyplot(fig)



# Bar chart of highest grades by subject
st.write('Highest grade by subject')
subject_grades = data.groupby('Subname')['Grade'].max()
st.bar_chart(subject_grades)


# Table of top N grades
N = 10


# assuming the data is stored in a pandas DataFrame called 'data'
filtered_data = data[~data['Grade'].isin(['F', 'E', 'D','C','B','ABSENT','COMPLE'])]  # filter out 'F', 'E', and 'B'
top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
st.table(top_grades)
st.write(f'Top {N} grades (excluding F, E,D,C,B,ABSENT and COMPLE )')
