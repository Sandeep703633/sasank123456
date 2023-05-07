from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the dataset
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

@app.route('/')
def index():
    # Display a bar chart of total grade points by department
    dept_grade_points = data.groupby('Dept')['Grade'].sum()
    fig, ax = plt.subplots()
    rows, cols = 2, 3
    fig, ax = plt.subplots(rows, cols,
                       sharex='col', 
                       sharey='row')

    for row in range(rows):
        for col in range(cols):
            ax[row, col].text(0.5, 0.5, 
                          str((row, col)),
                          color="green",
                          fontsize=18, 
                          ha='center')
    plt.show()
    
    ax.bar(dept_grade_points.index, dept_grade_points.values)
    ax.set_xlabel('Department')
    ax.set_ylabel('Total grade points')
    ax.set_title('Total grade points by department')
    plt.xticks(rotation=90)
    dept_chart = fig_to_base64(fig)

    # Display a pie chart of grades by subject
    subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
    fig, ax = plt.subplots()
    ax.pie(subject_grade_percentages, autopct='%1.1f%%')
    ax.set_title('Percentage of grades by subject')
    ax.legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    subject_chart = fig_to_base64(fig)

    # Display a bar chart of highest grades by subject
    subject_max_grades = data.groupby('Subname')['Grade'].max()
    fig, ax = plt.subplots()
    ax.bar(subject_max_grades.index, subject_max_grades.values)
    ax.set_xlabel('Subject')
    ax.set_ylabel('Highest grade')
    ax.set_title('Highest grade by subject')
    plt.xticks(rotation=90)
    max_grade_chart = fig_to_base64(fig)

    # Display a table of top N grades (excluding F, E, D, C, B, ABSENT, and COMPLE)
    N = 10
    filtered_data = data[~data['Grade'].isin(['F', 'E', 'D', 'C', 'B', 'ABSENT', 'COMPLE'])]
    top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
    top_grades_table = top_grades.to_html(index=False)

    return render_template('index1.html', dept_chart=dept_chart, subject_chart=subject_chart,
                           max_grade_chart=max_grade_chart, top_grades_table=top_grades_table)

def fig_to_base64(fig):
    import io
    from base64 import b64encode
    fig_bytes = io.BytesIO()
    fig.savefig(fig_bytes, format='png', bbox_inches='tight')
    fig_bytes.seek(0)
    fig_base64 = b64encode(fig_bytes.read()).decode('ascii')
    return fig_base64

if __name__ == '__main__':
    app.run(debug=True)
