import numpy as np
from first_function import input_argument


def output_collection(collect_list: list, value: object) -> int:
    """Makes a collection from argument and array

    Args:
        value(int): integer argument from function
        collect_list(list): input array (collection)

    Returns:
        result_list(list): every element in array was changed by value
    """

    result_list = np.multiply(collect_list, value)

    return result_list
