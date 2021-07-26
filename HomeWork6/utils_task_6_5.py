"""
**There are two files: one contains the names of site users, and the other contains data about their hobbies.
It is known that when storing data, the principle is used: one line - one user, the separator between values is a comma.

If the hobby file contains fewer entries than the full name file,
set to None in the merged data in the format <full name>: None.
If on the contrary, we exit the script with the code "1".

Solve problem for a situation when the amount of data in the files exceeds the amount of RAM.
You need to save the merged data to a new file (users_hobby.txt).
We write the hobby separated by a colon and a space after the full name:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи

Also, implement data parsing from files -
get separately the last name, first name and patronymic for users and the name of each hobby.
"""

import csv
import sys
from itertools import zip_longest


def save_the_combined_data_from_both_files_to_a_new_file(user_file_name, hobby_file_name, users_hobby_file_name):
    """
    The function saves the merged data from users.csv and hobby.csv files to a new users_hobby.csv file.
    :param user_file_name: users.csv - contains the full names of site users
    :param hobby_file_name: hobby.csv - contains data about their hobbies
    :param users_hobby_file_name: users_hobby.csv - contains merged data in the format <full name>: <hobbies>;
           the separator between values is a comma.
    """
    with open(user_file_name, newline='', encoding='utf-8') as csv_f1, \
            open(hobby_file_name, newline='', encoding='utf-8') as csv_f2, \
            open(users_hobby_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        full_name = csv.reader(csv_f1)
        hobbies = csv.reader(csv_f2)
        data_writer = csv.writer(csv_file, delimiter=':')
        for (name, hobby) in zip_longest(full_name, hobbies):
            try:
                if not name:
                    raise Exception('csv.Error')
                else:
                    if not hobby:
                        hobby = ['None']
                    user_hobbies_data = (','.join(name)+',', ' '+','.join(hobby))
                    data_writer.writerow(user_hobbies_data)
            except csv.Error:
                sys.exit()

    # data parsing from files -
    # get separately the last name, first name and patronymic for users and
    # the name of each hobby by the principle of main hobby: name, other hobbies: list of hobbies.
    with open(users_hobby_file_name, newline='', encoding='utf-8') as csv_f1:
        reader = csv.DictReader(csv_f1, delimiter=',', restkey='ДРУГИЕ ХОББИ')
        print(*reader, sep='\n')

    # data parsing from files -
    # get full name of users and the name of each hobby : list of hobbies.
    with open(users_hobby_file_name, newline='', encoding='utf-8') as csv_f1:
        reader = csv.DictReader(csv_f1, delimiter=':')
        print(*reader, sep='\n')
