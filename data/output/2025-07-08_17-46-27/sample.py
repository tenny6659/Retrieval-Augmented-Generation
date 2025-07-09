import pandas as pd

students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [20, 22, 21, 23],
    'Score': [85, 90, 78, 88]
})


pd.set_option('display.max_rows', None)
print(pd.read_csv("students").to_string())

students_df = pd.read_csv('students.csv')

stats = students_df['Score'].describe()
print(stats)
