"""
Name :  N'din Assi 
Course: CIS 216 
Course name: Object Oriented Programming 1. 
Phase 3
"""

import datetime

print("Welcome to Payroll system") 
"""This program automates the payroll system 
"""
print("Developed by Assi")

def main():
    number_of_employees = 0
    total_hours = 0
    total_gross_pay = 0 
    total_net_pay = 0
    total_tax = 0
    employee_data = [] # List to store employee dictionaries

    program_terminator = "start"
    while program_terminator != "end": 
        program_terminator = input("Do you wish to add another employee? (end to finish): ").lower()
        if program_terminator == "end":
            save_employee_data(employee_data)  # Save data to file
            retrieve_and_display_data()  # Retrieve and display data
            break 
        
        from_date, to_date = date_from_to()
        employee_name = employee_name_input()
        total_hours_input = total_hours_input_func()
        hourly_rates_input = hourly_rates_input_func()
        income_tax_input = income_tax_input_func()
        gross_pay, income_tax_calculated, net_pay = calculate_gross_pay(total_hours_input, hourly_rates_input, income_tax_input)
        display_employee_info(employee_name, total_hours_input, hourly_rates_input, gross_pay, income_tax_calculated, net_pay)
        
        number_of_employees += 1 
        total_hours += total_hours_input
        total_gross_pay += gross_pay 
        total_net_pay += net_pay
        total_tax += income_tax_calculated

        employee_data.append({
            "From Date": from_date,
            "To Date": to_date,
            "Employee Name": employee_name,
            "Total Hours": total_hours_input,
            "Hourly Rate": hourly_rates_input,
            "Income Tax": income_tax_calculated
        })

        summary({"Number of Employees": number_of_employees,
                 "Total hours": total_hours, 
                 "Total tax": total_tax,
                 "Total net pay": total_net_pay})
   
def employee_name_input():
    return input("Enter Employee name: ").capitalize()

def total_hours_input_func():
    return float(input("Enter number of hours worked: "))

def hourly_rates_input_func():
    return float(input("Enter hourly rates: "))

def income_tax_input_func():
    return float(input("Enter Income Tax rate: "))

def calculate_gross_pay(total_hours, hourly_rates, tax_rate):
    gross_pay = total_hours * hourly_rates
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(employee_name, total_hours, hourly_rates, gross_pay, income_tax, net_pay):
    print("--------------------------")
    print("Added Employee information ")
    print(f"Employee Name: {employee_name}")
    print(f"Total Hours: {total_hours}")
    print(f"Hourly rates: {hourly_rates}")
    print(f"Gross pay:  {gross_pay}")
    print(f"Income Tax: {income_tax}")
    print(f" Net Pay: {net_pay} ")
    print("------------------------------")
    
def summary(dict_details):
    print("--------------------------")
    print("PAYROLL SUMMARY")
    for key, value in dict_details.items():
        print(f"{key}: {value}")

def date_from_to():
    from_date = input("Enter from date (mm/dd/yyyy): ")
    to_date = input("Enter to date (mm/dd/yyyy): ")
    return from_date, to_date

def save_employee_data(employee_data):
    with open("employee_data.txt", "a") as file:
        for employee in employee_data:
            file.write(f"{employee['From Date']}|{employee['To Date']}|{employee['Employee Name']}|{employee['Total Hours']}|{employee['Hourly Rate']}|{employee['Income Tax']}\n")

def retrieve_and_display_data():
    from_date_filter = input("Enter From Date for report (mm/dd/yyyy) or 'All': ").lower()
    
    number_of_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_net_pay = 0
    total_tax = 0
    
    try:
        with open("employee_data.txt", "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 6:
                    from_date, to_date, employee_name, hours, rate, tax_rate = data
                    
                    if from_date_filter == "all" or from_date == from_date_filter:
                        hours = float(hours)
                        rate = float(rate)
                        tax_rate = float(tax_rate)
                        
                        gross_pay = hours * rate
                        income_tax = gross_pay * tax_rate
                        net_pay = gross_pay - income_tax
                        
                        print("--------------------------")
                        print("Employee Report")
                        print(f"From Date: {from_date}")
                        print(f"To Date: {to_date}")
                        print(f"Employee Name: {employee_name}")
                        print(f"Hours Worked: {hours}")
                        print(f"Hourly Rate: {rate}")
                        print(f"Gross Pay: {gross_pay}")
                        print(f"Income Tax Rate: {tax_rate}")
                        print(f"Income Tax: {income_tax}")
                        print(f"Net Pay: {net_pay}")
                        print("--------------------------")
                        
                        number_of_employees += 1
                        total_hours += hours
                        total_gross_pay += gross_pay
                        total_net_pay += net_pay
                        total_tax += income_tax
        summary({"Number of Employees": number_of_employees,
                 "Total hours": total_hours,
                 "Total tax": total_tax,
                 "Total net pay": total_net_pay})
        
    except FileNotFoundError:
        print("Employee data file not found.")

if __name__ == "__main__":
    main()