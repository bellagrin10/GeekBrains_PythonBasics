"""
Implement a simple data storage system for bakery sales. There should be two scripts with a command line interface:
one for writing data and one for displaying the recorded data.
When writing, send the value of the sales amount from the command line.
To read data, implement the following logic on the command line:
- just run the script - display all records;
- launching a script with one parameter - a number - display all records from a number equal to this number to the end;
- launching a script with two numbers - display records starting from the number equal to the first number,
  up to the number equal to the second number, inclusive.
Think about how to avoid reading the entire file when implementing the second and third cases.
Store data in the bakery.csv file in utf-8 encoding. Records are numbered starting from 1.
* Add the ability to edit data using a separate script:
- we pass it the record number and the new value.
In this case, the file should not be read in its entirety - a mandatory requirement.
Provide for a situation where the user enters a record number that does not exist.
"""

from add_sale import write_data
from show_sales import display_recorded_data
from edit_data import edit_sales_value
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, default=None)
parser.add_argument('--sales_value', type=float, default=None)
parser.add_argument('--start', type=int, default=0)
parser.add_argument('--end', type=int, default=0)
parser.add_argument('--index', type=int, default=None)
parser.add_argument('--new_value', type=float, default=None)
args = parser.parse_args()
if args.file_name == 'add_sale.py':
    write_data(args.sales_value)
elif args.file_name == 'show_sales.py':
    display_recorded_data(args.start, args.end)
elif args.file_name == 'edit_data.py':
    edit_sales_value(args.index, args.new_value)
