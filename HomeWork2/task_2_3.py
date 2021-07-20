"""
It is necessary to process the list - separate each integer with quotes
and padded with zero to two integer digits.
Form a string from the processed list,
without creating a new list (as they say, in place).
"""

string_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, string in enumerate(string_list):
    if string.isalnum():
        if string.isdigit():
            string_list[i] = f'{string.zfill(2):"^4}'
    else:
        string_list[i] = f'{"+"+string[1:].zfill(2):"^5}'
string = ' '.join(string_list)
print(string)
