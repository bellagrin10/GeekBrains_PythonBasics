from collections import defaultdict


def thesaurus_adv(*args):
    """
    The function takes strings in the format "First Name Last Name" as arguments and returns a dictionary,
     in which the keys are the first letters of the surnames, and the values are dictionaries,
     in which the keys are the first letters of the names, and the values are lists,
     containing full names starting with the corresponding letter.
    """

    full_names = list(map(str.split, args))
    staff = defaultdict(dict)
    for first_name, last_name in full_names:
        staff[last_name[0]].update({first_name[0]: []})

    for first_name, last_name in full_names:
        staff[last_name[0]][first_name[0]].append(f'{first_name} {last_name}')
    return staff


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

# Sorting the dictionary by foreign keys: first letters of surnames and by internal keys: first letters of names

print(
    *map(
        lambda x: {x[0]: dict(sorted(x[1].items()))},
        sorted(result.items())
        )
)
