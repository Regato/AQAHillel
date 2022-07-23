def input_argument(value):
    """One argument function

    Args:
        value(int): any integer argument

    Returns:
        output_value(int): multiple value by 100
    """
    output_value = (value * 100)

    return output_value


def output_collection(collect_list, func):
    """Makes a list from function and collection

    Args:
        collect_list(list): list on numbers (collection)
        func(function): function with one argument

    Returns:
        result_list(list): list of numbers
    """

    result_list = [func(item) for item in collect_list]

    return result_list


collect_list = [22, 4, 556, 634, 6, 3]
result = output_collection(collect_list, input_argument)

print(result)
