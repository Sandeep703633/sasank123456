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
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Total grade points by department
    ax[0].bar(dept_grade_points.index, dept_grade_points.values)
    ax[0].set_xlabel('Department')
    ax[0].set_ylabel('Total grade points')
    ax[0].set_title('Total grade points by department')
    plt.setp(ax[0].get_xticklabels(), rotation=45)

    # Display a pie chart of grades by subject
    subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
    ax[1].pie(subject_grade_percentages, autopct='%1.1f%%')
    ax[1].set_title('Percentage of grades by subject')
    ax[1].legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Display a bar chart of highest grades by subject
    subject_max_grades = data.groupby('Subname')['Grade'].max()
    fig2, ax2 = plt.subplots()
    ax2.bar(subject_max_grades.index, subject_max_grades.values)
    ax2.set_xlabel('Subject')
    ax2.set_ylabel('Highest grade')
    ax2.set_title('Highest grade by subject')
    plt.xticks(rotation=90)
    max_grade_chart = fig_to_base64(fig2)

    # Display a table of top N grades (excluding F, E, D, C, B, ABSENT, and COMPLE)
    N = 10
    filtered_data = data[~data['Grade'].isin(['F', 'E', 'D', 'C', 'B', 'ABSENT', 'COMPLE'])]
    top_grades = filtered_data.sort_values('Grade', ascending=False).head(N)
    top_grades_table = top_grades.to_html(index=False)

    # Save both charts to base64 strings
    dept_chart = fig_to_base64(fig)
    subject_chart = fig_to_base64(fig2)

    return render_template('index.html', subject_chart=subject_chart,
                           max_grade_chart=max_grade_chart, top_grades_table=top_grades_table,
                           dept_chart=dept_chart)

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
