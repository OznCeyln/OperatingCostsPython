import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

def save_to_file():
    with open('business_costs.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date", "description", "total_cost"])
        for item in data:
            writer.writerow([item["date"], item["description"], item["total_cost"]])

def calculate_cost():
    total_cost = 0

    personnel_cost = float(personnel_cost_entry.get())
    insurance_cost = float(insurance_cost_entry.get())
    taxes_cost = float(taxes_cost_entry.get())
    meal_cost = float(meal_cost_entry.get())
    rent_cost = float(rent_cost_entry.get())
    operation_cost = float(operation_cost_entry.get())
    advertising_cost = float(advertising_cost_entry.get())
    accounting_cost = float(accounting_cost_entry.get())
    maintenance_cost = float(maintenance_cost_entry.get())
    office_supplies_cost = float(office_supplies_cost_entry.get())
    lawyer_cost = float(lawyer_cost_entry.get())
    vehicle_cost = float(vehicle_cost_entry.get())
    transportation_cost = float(transportation_cost_entry.get())
    travel_cost = float(travel_cost_entry.get())
    description = description_entry.get()
    date = date_entry.get()

    total_cost = personnel_cost + insurance_cost + taxes_cost + meal_cost + rent_cost + operation_cost + advertising_cost + accounting_cost + maintenance_cost + office_supplies_cost + lawyer_cost + vehicle_cost + transportation_cost + travel_cost
    messagebox.showinfo("Total Cost", "Total Cost: " + str(total_cost))
    # Add the input to a data structure
    data.append({"date": date, "description": description, "total_cost": total_cost})
    #save the data to a file
    save_to_file()

def save_to_file():
    # save the data to a file, you can use csv, excel, json or any other format
    pass

data = []
root = tk.Tk()
root.title("Business Costs Calculator")

personnel_cost_label = tk.Label(root, text="Personnel Cost:")
personnel_cost_label.grid(row=0, column=0, padx=10, pady=10)
personnel_cost_entry = tk.Entry(root)
personnel_cost_entry.grid(row=0, column=1, padx=10, pady=10)

insurance_cost_label = tk.Label(root, text="Insurance Cost:")
insurance_cost_label.grid(row=1, column=0, padx=10, pady=10)
insurance_cost_entry = tk.Entry(root)
insurance_cost_entry.grid(row=1, column=1, padx=10,    pady=10)

taxes_cost_label = tk.Label(root, text="Taxes Cost:")
taxes_cost_label.grid(row=2, column=0, padx=10, pady=10)
taxes_cost_entry = tk.Entry(root)
taxes_cost_entry.grid(row=2, column=1, padx=10, pady=10)

meal_cost_label = tk.Label(root, text="Meal Cost:")
meal_cost_label.grid(row=3, column=0, padx=10, pady=10)
meal_cost_entry = tk.Entry(root)
meal_cost_entry.grid(row=3, column=1, padx=10, pady=10)

rent_cost_label = tk.Label(root, text="Rent Cost:")
rent_cost_label.grid(row=4, column=0, padx=10, pady=10)
rent_cost_entry = tk.Entry(root)
rent_cost_entry.grid(row=4, column=1, padx=10, pady=10)

operation_cost_label = tk.Label(root, text="Operation Cost:")
operation_cost_label.grid(row=5, column=0, padx=10, pady=10)
operation_cost_entry = tk.Entry(root)
operation_cost_entry.grid(row=5, column=1, padx=10, pady=10)

advertising_cost_label = tk.Label(root, text="Advertising Cost:")
advertising_cost_label.grid(row=6, column=0, padx=10, pady=10)
advertising_cost_entry = tk.Entry(root)
advertising_cost_entry.grid(row=6, column=1, padx=10, pady=10)

accounting_cost_label = tk.Label(root, text="Accounting Cost:")
accounting_cost_label.grid(row=7, column=0, padx=10, pady=10)
accounting_cost_entry = tk.Entry(root)
accounting_cost_entry.grid(row=7, column=1, padx=10, pady=10)

maintenance_cost_label = tk.Label(root, text="Maintenance Cost:")
maintenance_cost_label.grid(row=8, column=0, padx=10, pady=10)
maintenance_cost_entry = tk.Entry(root)
maintenance_cost_entry.grid(row=8, column=1, padx=10, pady=10)

office_supplies_cost_label = tk.Label(root, text="Office Supplies Cost:")
office_supplies_cost_label.grid(row=9, column=0, padx=10, pady=10)
office_supplies_cost_entry = tk.Entry(root)
office_supplies_cost_entry.grid(row=9, column=1, padx=10, pady=10)

lawyer_cost_label = tk.Label(root, text="Lawyer Cost:")
lawyer_cost_label.grid(row=10, column=0, padx=10, pady=10)
lawyer_cost_entry = tk.Entry(root)
lawyer_cost_entry.grid(row=10, column=1, padx=10, pady=10)

vehicle_cost_label = tk.Label(root, text="Vehicle Cost:")
vehicle_cost_label.grid(row=11, column=0, padx=10, pady=10)
vehicle_cost_entry = tk.Entry(root)
vehicle_cost_entry.grid(row=11, column=1, padx=10, pady=10)

transportation_cost_label = tk.Label(root, text="Transportation Cost:")
transportation_cost_label.grid(row=12, column=0, padx=10, pady=10)
transportation_cost_entry = tk.Entry(root)
transportation_cost_entry.grid(row=12, column=1, padx=10, pady=10)

travel_cost_label = tk.Label(root, text="Travel Cost:")
travel_cost_label.grid(row=13, column=0, padx=10, pady=10)
travel_cost_entry = tk.Entry(root)
travel_cost_entry.grid(row=13, column=1, padx=10, pady=10)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=14, column=0, padx=10, pady=10)
description_entry = tk.Entry(root)
description_entry.grid(row=14, column=1, padx=10, pady=10)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=15, column=0, padx=10, pady=10)
date_entry = ttk.Combobox(root, values=["01/01/2022", "01/02/2022", "01/03/2022", "01/04/2022", "01/05/2022"])
date_entry.grid(row=15, column=1, padx=10, pady=10)

calculate_cost_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_cost_button.grid(row=16, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()

