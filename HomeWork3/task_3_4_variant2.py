def thesaurus_adv(*args):
    """
    The function takes strings in the format "First Name Last Name" as arguments and returns a dictionary,
     in which the keys are the first letters of the surnames, and the values are dictionaries,
     in which the keys are the first letters of the names, and the values are lists,
     containing full names starting with the corresponding letter.
    """

    usernames = {}
    full_names = list(map(str.split, args))
    list(
        map(
            lambda x: usernames.setdefault(x[1][0], {}),
            full_names
        )
    )
    print(usernames)
    list(
        map(
            lambda x: usernames[x[1][0]].update({x[0][0]: []}),
            full_names
        )
    )
    print(usernames)
    list(
        map(
            lambda x: usernames[x[1][0]][x[0][0]].append(' '.join(x)),
            full_names
        )
    )
    return usernames


result = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(result)

# Sorting the dictionary by foreign keys: first letters of surnames and by internal keys: first letters of names
print(sorted(result.items()))
print(
    *map(
        lambda x: {x[0]: dict(sorted(x[1].items()))},
        sorted(result.items())
        )
)
