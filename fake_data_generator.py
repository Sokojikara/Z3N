import pandas as pd
from faker import Faker
import random
import math
import csv

def FDG():
    """
    Generates fake user data using the Faker library and saves it to a CSV file.
    """
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

def CDG():
    """
    Generates fake user data using the Faker library and saves it to a CSV file.
    """
    def generate_random_data():
        temperature = random.uniform(0, 100)
        humidity = random.uniform(0, 100)
        pressure = random.uniform(900, 1100)
        altitude = random.uniform(-100, 5000)
        time = random.choice([None, f"{random.randint(0, 23)}:{random.randint(0, 59)}"])

        # Introduce NaN and None values in the data
        if random.random() < 0.2:
            temperature = math.nan
        if random.random() < 0.2:
            humidity = math.nan
        if random.random() < 0.2:
            pressure = None
        if random.random() < 0.2:
            altitude = None
        if random.random() < 0.2:
            time = None

        return {
            "Temperature": temperature,
            "Humidity": humidity,
            "Pressure": pressure,
            "Altitude": altitude,
            "Time": time
        }

    # Generate 100 random rows of data
    data = [generate_random_data() for _ in range(100)]

    # Create a pandas DataFrame from the generated data
    df = pd.DataFrame(data)

    # Save the data to a CSV file
    csv_file_path = "fake_data.csv"
    df.to_csv(csv_file_path, index=False)


if __name__ == "__main__":
    # FDG() # Generate Random User Data
    CDG() # Generate Random Sensor Data