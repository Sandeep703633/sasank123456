import matplotlib.pyplot as plt
def sample(data):
    dept_grade_points = data.groupby('Dept')['Grade'].sum()
    plt.bar(dept_grade_points.index, dept_grade_points.values)
    plt.title('Total grade points by department')
    plt.xlabel('Department')
    plt.ylabel('Grade points')
    plt.xticks(rotation=45)
    plt.tight_layout()
    dept_chart = plt.gcf()

    return plt.show()
