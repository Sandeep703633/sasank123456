from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# Load the dataset
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/total_grade_points_by_dept')
def total_grade_points_by_dept():
    # Create a bar chart of total grade points by department
    dept_grade_points = data.groupby('Dept')['Grade'].sum()
    fig, ax = plt.subplots()
    ax.bar(dept_grade_points.index, dept_grade_points.values)
    ax.set_title('Total grade points by department')
    ax.set_xlabel('Department')
    ax.set_ylabel('Total grade points')
    # Convert the plot to an HTML image string
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('total_grade_points_by_dept.html', plot_url=plot_url)

@app.route('/grades_by_subject')
def grades_by_subject():
    # Create a pie chart of grades by subject
    subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
    fig, ax = plt.subplots()
    ax.pie(subject_grade_percentages, autopct='%1.1f%%')
    ax.set_title('Percentage of grades by subject')
    ax.legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    # Convert the plot to an HTML image string
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('grades_by_subject.html', plot_url=plot_url)

@app.route('/highest_grade_by_subject')
def highest_grade_by_subject():
    # Create a bar chart of highest grades by subject
    subject_max_grades = data.groupby('Subname')['Grade'].max()
    fig, ax = plt.subplots()
    ax.bar(subject_max_grades.index, subject_max_grades.values)
    ax.set_title('Highest grade by subject')
    ax.set_xlabel('Subject')
    ax.set_ylabel('Grade')
    # Convert the plot to an HTML image string
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('highest_grade_by_subject.html', plot_url=plot_url)

@app.route('/top_grades')
def top_grades():
    # Create a table of top N grades (excluding F, E, D, C, B, ABSENT, and COMPLE)
    N = 10
    filtered_data = data[~data['Grade'].isin(['F', 'E', 'D', 'C', 'B', 'ABSENT', 'COMPLE'])]
    top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
    return render_template('top_grades.html', top_grades=top_grades)

if __name__ == '__main__':
    app.run(debug=True)
