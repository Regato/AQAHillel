import os
import pickle
from io import BytesIO
from typing import List

from user import User


def csv_to_dict(path):
    if os.path.exists(path) is not True:
        print('CSV file is not existing!')

        return False
    else:
        with open(path, 'r') as file:
            csv_lines = file.readlines()

            first_line = csv_lines.pop(0)

            user_data = dict()
            user_data['headers'] = first_line
            user_data['data'] = csv_lines

            users: List[User] = User.from_csv(user_data)

            return users


def user_to_bytes(path, function_obj):
    with open(path, 'wb') as file:
        header_str = f'first_name last_name email gender'
        header_bytes = pickle.dumps(header_str)
        file.write(header_bytes)

        for obj in function_obj:
            data_str = f'{obj.firstAttribute} ' \
                       f'{obj.secondAttribute} ' \
                       f'{obj.thirdAttribute} ' \
                       f'{obj.fourthAttribute}'
            data_bytes = pickle.dumps(data_str)
            data_buffer = BytesIO(data_bytes)
            file.writelines(data_buffer)

        return True
