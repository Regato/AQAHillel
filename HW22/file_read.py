import os
import pickle
from io import BytesIO
from typing import List

from user import User


def csv_to_dict(path):
    """Returns User class objects list"""

    # Check is file existing
    if os.path.exists(path) is not True:
        print('[CSV_TO_DICT]: CSV file is not existing!')

        return False
    else:
        # If existing - open it
        with open(path, 'r') as file:
            # Read file by lines formatting
            csv_lines = file.readlines()

            # Cut first line with headers information
            first_line = csv_lines.pop(0)

            # Making a dict from extracted data
            user_data = dict()
            user_data['headers'] = first_line
            user_data['data'] = csv_lines

            # Using from_csv method from User class
            # to make a CSV file from data
            users: List[User] = User.from_csv(user_data)

            return users


def user_to_bytes(path, function_obj):
    """Returns True and writing bytes data from CSV to a bytes file."""

    # Open file by a path
    with open(path, 'wb') as file:
        # Making headers in bytes format
        header_str = f'first_name last_name email gender'
        header_bytes = pickle.dumps(header_str)
        # Putting bytes headers into BytesIO container (buffer)
        # to easily write it into a file
        # (python does not provide this function)
        head_buffer = BytesIO(header_bytes)
        # Writing buffer data to a file
        file.writelines(head_buffer)

        # Getting User class objects (users) from a list of users
        for obj in function_obj:
            # Making data from class object (user) in bytes format
            data_str = f'{obj.firstAttribute} ' \
                       f'{obj.secondAttribute} ' \
                       f'{obj.thirdAttribute} ' \
                       f'{obj.fourthAttribute}'
            data_bytes = pickle.dumps(data_str)
            # Putting bytes data into BytesIO container (buffer)
            # to easily write it into a file
            # (python does not provide this function)
            data_buffer = BytesIO(data_bytes)
            # Writing buffer data to a file
            file.writelines(data_buffer)

        print('[USER_TO_BYTES]: User class object are converted to a bytes file!')

        return True
