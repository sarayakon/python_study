# Register Customer Name for Roboter App

import csv
import os
from pathlib import Path


class RegisterName:
    def __init__(self, folder_path):
        self.folder_path = Path(folder_path)
        os.makedirs(self.folder_path, exist_ok=True)

    def register_name(self, customer_name):
        data = []
        filename = os.path.join(self.folder_path, "customer_name.csv")

        if os.path.exists(filename):
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    row['Count'] = int(row['Count'])
                    data.append(row)

        exist = False
        for row in data:
            if row['Name'] == customer_name:
                row['Count'] += 1
                exist = True
                break

        if not exist:
            data.append({'Name': customer_name, 'Count': 1})

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            print(f'registered your name as {customer_name}.')
