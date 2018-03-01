import sys
import csv
import numpy as np

def check_float(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def print_current_week(budget_sheet, week_spending, value):
    print("Current Week:")
    goal_names = budget_sheet["goal_names"]
    goal_values = budget_sheet["goal_values"]
    print(value)


def load_csv(file_name):
    print("Loading CSV...")
    data = list(csv.reader(open(file_name)))
    data = np.array(data)
    return data

def process_weeks(data, budget_sheet):
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

def process_goals(data, budget_sheet):
    row_num = data.shape[0]
    column_num = data.shape[1]

    # processing the main values from the budget app spreadsheet
    budget_sheet["goal_names"] = data[2:16, 1:2].flatten();
    budget_sheet["goal_values"] = data[2:16, 3:4].flatten();
    budget_sheet["savings"] = data[7:8, 5:6].flatten();
    budget_sheet["average_spendings"] = data[3:4, 5:6].flatten();

    return budget_sheet

def calculate_money_left(budget_sheet, week_spending, value, category):
    goal_names = budget_sheet["goal_names"]
    goal_values = budget_sheet["goal_values"]
    return goal_values[goal_names.index(category)] - values

def export_to_csv():
    print("Exporting to csv... \n")

def save_to_google_drive():
    print("Saving to Google Drive... \n")

def  print_categories_and_goals():
    print("Printing Categories and Goals... \n")

def handle_commands(budget_sheet, week_spending):
    command = ""
    while "exit" not in command.lower():
        command = input("Input commands:\nexit, add spending, print week n, print month\n")
        if ("print week" in command.lower()):
            print_current_week(budget_sheet, week_spending, command.split()[2])

def main():
    print("Budgeting Script")

    budget_sheet = {}
    data = load_csv('sheet1.csv')
    budget_sheet = process_goals(data, budget_sheet)
    week_spending = process_weeks(data, budget_sheet)
    handle_commands(budget_sheet, week_spending)

main()
