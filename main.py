import sys
import csv
import numpy as np

# global variables:
data = [[]]
budget_sheet = {}
week_spending = {}
total_weeks = 0
file_name = "sheet1.csv"

def check_int(input_string):
    try:
        int(input_string)
        return True
    except ValueError:
        return False

def load_csv(file_name):
    global data
    print("Loading CSV...")
    data = list(csv.reader(open(file_name)))
    data = np.array(data)
    return data

def process_weeks():
    global total_weeks
    global week_spending
    global data
    row_num = data.shape[0]
    column_num = data.shape[1]
    # processing the weekly values from the budgeting app spreadsheet
    row_start = 21
    column_labels = 0
    column_goal = 1
    column_left = 2
    week_spending = {}
    all_weeks = data[row_start:row_num, column_labels+1:column_left+2]
    week_row = 0
    counter = all_weeks.shape[0] % 11
    total_weeks = counter
    while(week_row < all_weeks.shape[0]):
        current_week = {}
        for i in range(1, 8):
            goal = all_weeks[week_row+i:week_row+i+1,
                column_labels:column_left].flatten()[0]
            value = all_weeks[week_row+i:week_row+i+1,
                column_goal:column_left].flatten()[0]
            current_week[goal] = float(value)
        week_spending["week" + str(counter)] = current_week
        counter -= 1
        week_row += 11
    return week_spending

def process_goals():
    global budget_sheet
    global data
    row_num = data.shape[0]
    column_num = data.shape[1]

    # processing the main values from the budget app spreadsheet
    budget_sheet["goal_names"] = data[2:16, 1:2].flatten();
    budget_sheet["goal_values"] = data[2:16, 3:4].flatten();
    budget_sheet["savings"] = data[7:8, 5:6].flatten();
    budget_sheet["average_spendings"] = data[3:4, 5:6].flatten();

    return budget_sheet

def print_current_week(value):
    if (not check_int(value)):
        print("Week should be an int, try again")
        return
    if (int(value) > total_weeks):
        print("Week", value, "not stored, try again")
        return
    current_week = week_spending["week"+value]
    print('\n')
    print("Current Week:")
    row = ["Category", "Spent", "Left"]
    print("{: >16} {: >16} {: >16}".format(*row))
    for key, value in current_week.items():
        left = calculate_money_left(value, key)
        if (left is ""):
            continue
        row = [key, value, left]
        print("{: >16} {: >16} {: >16}".format(*row))
    print('\n')

def print_add_spending():
    current_week = week_spending["week"+str(total_weeks)]
    change = input("\nEnter category and amount:\n")
    current_week[change.split()[0]] += float(change.split()[1])
    print("Added",change.split()[1],"to", change.split()[0],"\n")

def calculate_money_left(value, category):
    global budget_sheet
    goal_names = budget_sheet["goal_names"].tolist()
    goal_values = budget_sheet["goal_values"].tolist()
    if (category in goal_names):
        return round(float(goal_values[goal_names.index(category)]) - value, 2)
    return ""

def export_to_csv():
    print("Exporting to csv... \n")


def save_to_google_drive():
    print("Saving to Google Drive... \n")

def  print_categories_and_goals():
    print("Printing Categories and Goals... \n")

def handle_commands():
    command = ""
    while "exit" not in command.lower():
        command = input("Input commands:\n- exit\n- add spending\n- print week n\n")
        if ("print week" in command.lower()):
            if (len(command.split()) > 2):
                print_current_week(command.split()[2])
            else:
                print_current_week(str(total_weeks))
        elif ("add spending" in command.lower()):
            print_add_spending()
    export_to_csv()

def main():
    print("Budgeting Script")

    data = load_csv(file_name)
    budget_sheet = process_goals()
    week_spending = process_weeks()
    handle_commands()

main()
