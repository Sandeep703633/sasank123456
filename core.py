from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

from sample import sample

app = Flask(__name__)

# Load the data
data = pd.read_excel(r"C:\\Users\\bandi\\Desktop\\sandeep\\Data Set.xlsx")

@app.route("/")
def home():
    sample(data)

    # Display a pie chart of grades by subject
    subject_grade_percentages = data.groupby('Subname')['Grade'].count() / len(data) * 100
    fig, ax = plt.subplots()
    ax.pie(subject_grade_percentages, autopct='%1.1f%%')
    ax.set_title('Percentage of grades by subject')
    ax.legend(subject_grade_percentages.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    subject_chart = plt.gcf()

    # Display a bar chart of highest grades by subject
    subject_max_grades = data.groupby('Subname')['Grade'].max()
    plt.bar(subject_max_grades.index, subject_max_grades.values)
    plt.title('Highest grade by subject')
    plt.xlabel('Subject')
    plt.ylabel('Grade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    max_chart = plt.gcf()

    # Render the template without the charts and table
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
