
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Diana'], 
       'Age': [20, 22, 21, 23], 
       'Score': [85, 90, 78, 88]}
df = pd.DataFrame(data)

print(df)

summary_stats = df['Score'].describe()
print(summary_stats)