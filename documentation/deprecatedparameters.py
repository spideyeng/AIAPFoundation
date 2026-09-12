import pandas as pd

# Sample data
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)  

# Can you identify the error in this line?   
# df.sort_values('A', inplace='True')  
df.sort_values('A', inplace=True)    
print(df)