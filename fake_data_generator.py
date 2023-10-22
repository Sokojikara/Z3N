from faker import Faker
import csv

fake = Faker()

num_users = 100

users = []
for _ in range(num_users):
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    }
    users.append(user)

csv_file_path = "fake_users.csv"

# Write the user data to a CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "address", "email", "phone_number", "birthdate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for user in users:
        writer.writerow(user)

print(f"Fake user data has been generated and saved in '{csv_file_path}'")
 
