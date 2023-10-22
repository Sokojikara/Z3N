# Install Pandas: pip install pandas

# Import Pandas
import pandas as pd

# Create a Pandas dataframe from list of lists
data = [
    ['Alex',15], 
    ['Bob',12],
    ['Clarke',13]  
    ]
df = pd.DataFrame(data,columns=['Name','Age'])
print("DataFrame from List")
print(df)
print("\n\n")


# Few Dataframe operations
print("DataFrame Operations")
print("Shape of DataFrame: ", df.shape)
print("Size of DataFrame: ", df.size)
print("Columns of DataFrame: ", df.columns)
print("Index of DataFrame: ", df.index)
print("Values of DataFrame: ", df.values)
print("Head of DataFrame: ", df.head(2))
print("Tail of DataFrame: ", df.tail(2))
print("Describe of DataFrame: ", df.describe())
print("Transpose of DataFrame: ", df.T)
print("Sort by column of DataFrame: ", df.sort_values(by='Age'))
print("\n\n")


# Get a column from DataFrame
print("Get a column from DataFrame")
print(df['Name'])
print("\n\n")


# Get a row from DataFrame
print("Get a row from DataFrame")
print(df.iloc[0])
print("\n\n")


# Get a cell from DataFrame
print("Get a cell from DataFrame")
print(df.iloc[0,0])
print("\n\n")


# Read CSV file
print("Read CSV file")
df = pd.read_csv('pd_data.csv')
print(df)
print("\n\n")

# Few Dataframe Operations on CSV file
print("DataFrame Operations on CSV file")
print("Shape of DataFrame: ", df.shape)
print("Size of DataFrame: ", df.size)
print("Columns of DataFrame: ", df.columns)
print("Index of DataFrame: ", df.index)
print("Values of DataFrame: ", df.values)
print("Head of DataFrame: ", df.head(2))
print("Tail of DataFrame: ", df.tail(2))
print("Describe of DataFrame: ", df.describe())
print("Transpose of DataFrame: ", df.T)
print("Sort by column of DataFrame: ", df.sort_values(by='Age'))
print("\n\n")

