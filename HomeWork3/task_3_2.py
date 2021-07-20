def num_translate_adv(number, dict_num):
    """
    Translation of numbers from 0 to 10 from English into Russian.
    Implement correct work with numbers starting with a capital letter - the result must also be capitalized.
    """
    if number.istitle():
        number = number.lower()
        translate = dict_num.get(number).title()
    else:
        translate = dict_num.get(number)
    return translate


dict_of_numbers = dict(one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
                       eight='восемь', nine='девять', ten='десять')
print(num_translate_adv('one', dict_of_numbers))
print(num_translate_adv('One', dict_of_numbers))
print(num_translate_adv('on', dict_of_numbers))
