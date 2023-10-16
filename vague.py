import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("vague.csv")
print("HEAD")
print(data.head())
print("TAIL")
print(data.tail())

print("INFO")
print(data.info())
print("DESCRIBE")
print(data.describe())

print("NAME")
print(data["Name"])
print("SINGLE NAME")
print(data["Name"][0])

print("MIN AGE")
print(data["Age"].min())
print("MEAN AGE")
print(data["Age"].mean())
print("MAX AGE")
print(data["Age"].max())

print("AGE DESCRIBE")
print(data["Age"].describe())

print("AGE > 30")
print(data[data["Age"] > 30])

print("NAMES WHERE AGE > 30")
print(data[data["Age"] > 30]["Name"])

print("COUNT OF NAMES WHERE AGE > 30")
print(data[data["Age"] > 30]["Name"].count())


plt.hist(data["Age"])
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.title("Age distribution")
plt.show()


