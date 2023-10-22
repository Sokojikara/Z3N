import csv
from faker import Faker
import random

fake = Faker()

num_users = 100

user_data = []

for _ in range(num_users):
    name = fake.name()
    age = random.randint(18, 99)
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    
    user_data.append([name, age, email, phone_number, address])

csv_file_path = "fake_data.csv"

with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Email", "Phone Number", "Address"])
    writer.writerows(user_data)

print(f"Random user data has been generated and saved to '{csv_file_path}' file.")
