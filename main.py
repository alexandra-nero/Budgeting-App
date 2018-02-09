import csv
import numpy as np

def check_float(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def print_current_week():
    print("Printing Current Week...")

def load_csv(file_name):
    print("Loading CSV...")
    data = list(csv.reader(open(file_name)))
    data = np.array(data)
    return data

def process_csv(data, budget_sheet):
    row_num = data.shape[0]
    column_num = data.shape[1]

    # processing the main values from the budget app
    budget_sheet["goal_names"] = data[2:16, 1:2].flatten();
    budget_sheet["goal_values"] = data[2:16, 3:4].flatten();
    budget_sheet["savings"] = data[7:8, 5:6].flatten();
    budget_sheet["average_spendings"] = data[3:4, 5:6].flatten();

    # processing the weekly values from the budgeting app
    row_start = 21
    column_labels = 1
    column_goal = 2
    column_left = 3
    week_budgets = {}
    while(row_start < row_num):
        current_week = {}
        print(data[row_start:row_start+1, column_labels:column_labels+1])
        row_start += 11

    return budget_sheet

def save_to_google_drive():
    print("Saving to Google Drive... \n")

def  print_categories_and_goals():
    print("Printing Categories and Goals... \n")

def main():
    print("Budgeting Script")

    budget_sheet = {"categories":[], "goals":[], "savings":[],
        "average_spendings":[]}
    data = load_csv('sheet1.csv')
    budget_sheet = process_csv(data, budget_sheet)

    print(budget_sheet)

main()