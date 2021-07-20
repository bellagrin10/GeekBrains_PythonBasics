"""
The list needs to be processed - separate each integer with quotes
and zero-padded to two integer digits, creating a new list.
Form a string from the processed list.
"""
string_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_string_list = []
temp = []
for string in string_list:
    if string.isalnum():
        if string.isdigit():
            digits_zero_fill = string.zfill(2)
            new_string_list.extend(['"', digits_zero_fill, '"'])
            temp.append(digits_zero_fill)
        else:
            new_string_list.append(string)
    else:
        plus_digits_zero_fill = f'+{string[1:].zfill(2)}'
        new_string_list.extend(['"', plus_digits_zero_fill, '"'])
        temp.append(plus_digits_zero_fill)
formed_string = ' '.join(new_string_list)
for i in temp:
    j = f' {i} '
    formed_string = i.join(formed_string.split(j))
print(formed_string)
