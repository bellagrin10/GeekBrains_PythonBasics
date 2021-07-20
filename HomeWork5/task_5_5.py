def identify_non_repetitive_elements(src):
    """
    A list of numbers is presented.
    Determine list items that do not have repetitions.
    Form a list of these elements while maintaining their order in the original list.
    :return: list
    """

    identification_index_or_mark = {}
    for index, key in enumerate(src):
        if identification_index_or_mark.get(key):
            identification_index_or_mark.update({key: "non-unique"})
        else:
            identification_index_or_mark.update({key: index})
    return identification_index_or_mark


unique_items_and_marking_non_unique = identify_non_repetitive_elements([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])
print(unique_items_and_marking_non_unique)

# insertion order is guaranteed for Python 3.7 and up!
# (порядок вставки гарантирован для Python 3.7 и выше!)

result = [key for key, value in unique_items_and_marking_non_unique.items() if value != "non-unique"]
print(result)

# for Python below 3.7 can be sorted by unique element occurrence indices.
# (для Python ниже 3.7 можно отсортировать по индексам появления уникальных элементов.)

temp = sorted(unique_items_and_marking_non_unique.items(), key=lambda item: item[1] if item[1] != "non-unique" else 0)
result = [key for key, value in temp if value != "non-unique"]
print(result)
