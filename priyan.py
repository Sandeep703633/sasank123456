from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the data
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

@app.route("/")
def home():
    # Display a bar chart of total grade points by department
    dept_grade_points = data.groupby('Dept')['Grade'].sum()
    plt.bar(dept_grade_points.index, dept_grade_points.values)
    plt.title('Total grade points by department')
    plt.xlabel('Department')
    plt.ylabel('Grade points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    dept_chart = plt.gcf()
    #plt.clf()
    plt.show()

    # Display a pie chart of grades by subject
    subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
    fig, ax = plt.subplots()
    ax.pie(subject_grade_percentages, autopct='%1.1f%%')
    ax.set_title('Percentage of grades by subject')
    ax.legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    subject_chart = plt.gcf()
    #plt.clf()
    plt.show()

    # Display a bar chart of highest grades by subject
    subject_max_grades = data.groupby('Subname')['Grade'].max()
    plt.bar(subject_max_grades.index, subject_max_grades.values)
    plt.title('Highest grade by subject')
    plt.xlabel('Subject')
    plt.ylabel('Grade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    max_chart = plt.gcf()
    #plt.clf()
    plt.show()

    # Display a table of top N grades (excluding F, E, D, C, B, ABSENT, and COMPLE)
    N = 10
    filtered_data = data[~data['Grade'].isin(['F', 'E', 'D', 'C', 'B', 'ABSENT', 'COMPLE'])]
    top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
    top_table = top_grades.to_html(index=False)

    # Render the template with the charts and table
    return render_template('home.html', dept_chart=dept_chart, subject_chart=subject_chart, max_chart=max_chart, top_table=top_table)

if __name__ == '__main__':
    app.run(debug=True)
