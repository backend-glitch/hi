import pandas as pd
import os

data  = [ "name","address","number"]
df = pd.DataFrame(data)

df = pd.read_csv("contacts.csv")

def display():
    if df.empty:
        print("\nNo contacts found.\n")
    else:
        print("\nContacts List:\n", df.to_string(index=False), "\n")

def add():
    if df.empty:
        print("\nNo contacts found.\n")
    else:
        print("\nContacts List:\n", df.to_string(index=False), "\n")
        
    df.loc[len(df)] = [name, address, number]
    print("\nContact added successfully!\n")

def save_data():
    df.to_csv("part_1", index=False) # to save in cse file.

while True:
    print(" 1.display contacts :")
    print("2. add contacts : ")
    print("3. save and exit :")

    choice  = int(input("enter choice"))

    if choice == 1:
        display()
        print("done1")
    elif choice == 2:
        add()
        print("done2")
    elif choice == 3:
        save_data()
        print("done3")
        break
    
        