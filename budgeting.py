import sys
import csv
import numpy as np

# CSV Structure
income_pos = (0, 1)
bill_num = 9
spending_num = 7
bill_start = (2, 0)
bill_end = (2 + bill_num, 3)
spend_start = (12, 0)
spend_end = (12 + spending_num, 3)
week_start = (20, 0)

# Global variables
file_name = "ex.csv"
weekly_income = 0
monthly_income = 0
data = [[]]
bills = [[]]
spending = [[]]
weeks = [[]]

# checks if a string is an int
def check_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False

# finds the index of an element in an array
def find_element(arr, element):
    return [(ix,iy) for ix, row in enumerate(arr) for iy, i in enumerate(row) if i == element]

# imports csv as 2d array from global var file_name
def import_csv():
    print("Importing CSV...")
    global data
    data = list(csv.reader(open(file_name)))
    data = np.array(data)
    return data

def convert_to_dict(array):
    labels = array[0]
    complete_dict = {}
    for row in array:
        print(row, labels)
        if(row is labels):
            continue
        else:
            temp_dict = {}
            complete_label = ""
            for element in row:
                if row.tolist().index(element) is 0:
                    complete_label = element
                else:
                    label = labels[row.tolist().index(element)]
                    temp_dict[label] = element
            complete_dict[complete_label] = temp_dict
    print(complete_dict)
    return complete_dict

# splits up the data from the csv and stores in 2D array
def split_data():
    print("Processing data from CSV...")
    global data, income_pos, weekly_income, monthly_income
    global bills, spending, weeks
    weekly_income = data[income_pos[0]][income_pos[1]]
    monthly_income = weekly_income * 4
    bills = data[bill_start[0]: bill_end[0], bill_start[1]: bill_end[1]]
    spending = data[spend_start[0]: spend_end[0], spend_start[1]: spend_end[1]]
    weeks = data[week_start[0]:, week_start[1]:]

def calculate_money_left(category, amount):
    global spending
    index = find_element(spending, category)
    row_num = index[0][0]
    return round(float(spending[row_num][2]) - float(amount), 2)

# prints out the specified week
def print_week(week_num):
    global weeks
    if (not check_int(week_num)):
        print("Week should be an int, try again")
        return
    if (int(week_num) > len(weeks) or int(week_num) <= 0):
        print("Week", week_num, "not stored, try again")
        return
    labels = ["Category", "Spent", "Left"]
    category = weeks[0]
    row = weeks[int(week_num)]
    print("\nWeek: " + row[1] + "\n")
    print("{: >16} {: >16} {: >16}".format(*labels))
    for x in range(2, len(category)):
        print_row = [category[x], row[x], calculate_money_left(category[x], row[x])]
        print("{: >16} {: >16} {: >16}".format(*print_row))
    print("\n")

# prints out asking for which category and amount
def print_add_spending():
    global weeks
    change = input("\nEnter category and amount:\n")
    category = change.split()[0]
    amount = float(change.split()[1])
    index = find_element(weeks, category)
    weeks[len(weeks) - 1][index[0][1]] = float(weeks[len(weeks) - 1][index[0][1]]) + amount
    print("Added", amount, "to", category, "\n")

# exports the changes made to the same csv with the file_name
def export_to_csv():
    global data, weeks
    print("Exporting to CSV...")
    data[week_start[0]:, week_start[1]:] = weeks
    with open("fake.csv","w", newline='') as my_csv:
        csvWriter = csv.writer(my_csv)
        for row in data:
            csvWriter.writerow(row)
    my_csv.close()

# main function for printing and handling commands
def handle_commands():
    global weeks
    command = ""
    while "exit" not in command.lower():
        command = input("Input commands:\n- exit\n- add spending\n- print week n\n")
        if ("print week" in command.lower()):
            if (len(command.split()) > 2):
                print_week(command.split()[2])
            else:
                print_week(len(weeks) - 1)
        elif ("add spending" in command.lower()):
            print_add_spending()
    export_to_csv()


def main():
    print("Budgeting Script")
    import_csv()
    split_data()
    handle_commands()

main()
