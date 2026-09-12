import pandas as pd  
  
data = {  
    'Name': ['Alice', 'Bob', 'Charlie'],  
    'Age': [25, 30, 35],  
    'Score': [88, 92, 95]  
}  
  
# df = pd.Dataframe(data)  
df = pd.DataFrame(data)  
# total_score = df.sum_all('Score')
# total_score = df.sum('Score')   
total_score = df['Score'].sum()  
print("Total Score:", total_score)

total_age = df['Age'].sum()  
print("Total Age:", total_age)

# columns_list = df.get_columns()  
columns_list = df.columns.tolist()
total_score = df['Score'].sum()  
print("Columns:", columns_list)

# print("Total Score:", total_score)  
# print("Columns:", columns_list)