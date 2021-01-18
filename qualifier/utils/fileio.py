# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csv_path, qualifying_loans):
    """Saves the qualifying loans in CSV format 

    Args:
        csv_path: the user provided path for the created file
        qualifying_loans: the loans that the user qualifies for based on inputed information

    Returns:
        Creates new User desinated CSV name and path
    """

    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    csvpath = Path(csv_path)
    with open(csvpath, "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for item in qualifying_loans:
            csvwriter.writerow(item)

