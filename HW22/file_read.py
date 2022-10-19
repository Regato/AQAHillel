import csv
import pickle
from io import BytesIO
from typing import List

from user import User


def csv_to_dict(path):
    """Returns User class objects list"""

    with open(path, 'r') as file:
        csv_data = csv.DictReader(file)
        csv_extract = [extract_data for extract_data in csv_data]

        user: List[User] = User.from_csv(csv_extract)

        print(user)
        return user


def user_to_bytes(path, function):
    """Returns True and writing bytes data from CSV to a bytes file."""
    users = [user.__dict__ for user in function]
    write_users = [list(user.values()) for user in users]

    header_bytes = pickle.dumps(write_users)
    head_buffer = BytesIO(header_bytes)
    with open(path, 'wb') as file:
        file.writelines(head_buffer)
