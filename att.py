# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 09:15:54 2025

@author: yaser
"""

from datetime import datetime

print(" Welcome to the Package Delivery Logger")
print("Enter the name of the person receiving the package.")
print("Type 'done' when deliveries are complete.")
print("Type 'remove' to delete a wrong entry.\n")

delivery_log = {}  # Key: Name, Value: Timestamp

while True:
    name = input("Receiver Name (or 'done'/'remove'): ").strip()

    if name.lower() == 'done':
        break

    elif name.lower() == 'remove':
        to_remove = input("Enter name to remove from delivery log: ").strip()
        if to_remove in delivery_log:
            del delivery_log[to_remove]
            print(f" {to_remove}'s entry removed.\n")
        else:
            print(f" {to_remove} not found in delivery log.\n")
        continue

    elif name == "":
        print(" Name cannot be empty. Try again.\n")
        continue

    elif name in delivery_log:
        print(f" {name} has already received a package.\n")
        continue

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    delivery_log[name] = timestamp
    print(f"Package delivered to {name} at {timestamp}.\n")

# Final Output
print("\n All Deliveries Completed!")
print(f" Total packages delivered: {len(delivery_log)}")
print(" Final Delivery Log with Timestamps:")

for i in range(len(delivery_log)):
    keys_list = list(delivery_log.keys())  # Get a list of keys
    values_list = list(delivery_log.values())  # Get a list of values
    print(i + 1, keys_list[i], values_list[i])  # Access elements by index
