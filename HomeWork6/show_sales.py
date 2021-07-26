import pandas as pd


def display_recorded_data(start, end):
    """
    The function for reading data implements the following logic:
    - just run the script - display all records;
    - launching a script with one number - display all records from a number equal to this number to the end;
    - launching a script with two numbers - display records starting from the number equal to the first number,
      up to the number equal to the second number, inclusive.
    Handling exceptions when the user enters a non-existent record number.
    :param start: int
    :param end: int
    """
    n = (end - start + 1) if end else None
    try:
        df = pd.read_csv('bakery.csv', header=None, skiprows=range(start), nrows=n, encoding='utf-8')
        print(df)
    except Exception as e:
        print(e)
