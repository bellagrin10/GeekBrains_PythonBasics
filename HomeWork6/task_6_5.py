"""
** Solve problem 4 and implement the command line interface,
so that you can specify the name of both source files and the name of the output file. Test the script.
"""

import utils_task_6_5
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--user_file_name', type=str, default=None)
parser.add_argument('--hobby_file_name', type=str, default=None)
parser.add_argument('--users_hobby_file_name', type=str, default=None)
args = parser.parse_args()
if not args.user_file_name or not args.hobby_file_name or not args.users_hobby_file_name:
    utils_task_6_5.save_the_combined_data_from_both_files_to_a_new_file('users.csv', 'hobby.csv', 'users_hobby.csv')
else:
    utils_task_6_5.save_the_combined_data_from_both_files_to_a_new_file(args.user_file_name,
                                                                        args.hobby_file_name,
                                                                        args.users_hobby_file_name)
