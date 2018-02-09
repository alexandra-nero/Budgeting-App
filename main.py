import csv
import numpy as np

def check_float(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def print_status():
    print "Printing Status..."


def load_csv(file_name):
    print "Loading CSV..."
    data = list(csv.reader(open(file_name)))
    data = np.array(data)
    return data

def process_csv(data):
    print data

def save_to_google_drive():
    print "Saving to Google Drive... \n"

def  print_categories_and_goals():
    print "Printing Categories and Goals... \n"

def main():
    print("Hello, World!")
    CATEGORY_START = (2, 3)
    WEEK_START = (2, 22)

    categories_dict = {}
    current_week = {}

    data = load_csv('sheet1.csv')
    process_csv(data)


main()
