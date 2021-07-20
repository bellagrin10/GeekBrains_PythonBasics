from itertools import zip_longest

'''
There are two lists: tutors and classes.
It is necessary to implement a generator that returns tuples of the form (<tutor>, <class>).
The number of generated tuples must not exceed the length of the tutors list.
If there are fewer elements in the classes list than in the tutors list,
you need to output the last tuples in the form: (<tutor>, None).
Prove that you have created a generator. Check his work to the point of against the stop.
'''


def distribution_of_tutors_by_class(tutors, classes):
    if len(tutors) <= len(classes):
        return zip(tutors, classes)
    return zip_longest(tutors, classes, fillvalue=None)


result_1 = distribution_of_tutors_by_class(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'],
                                           ['9А', '7В', '9Б', '9В', '8Б'])
result_2 = distribution_of_tutors_by_class(['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'],
                                           ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '8A'])
print(f'{" result 1 ":*^20}')
print(*result_1, sep='\n')
print(f'{" result 2 ":*^20}')
while True:
    print(next(result_2))
