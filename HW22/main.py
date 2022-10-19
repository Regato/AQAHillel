import os

from file_read import csv_to_dict
from file_read import user_to_bytes


if __name__ == '__main__':
    csv_users = csv_to_dict(f'{os.getcwd()}/csv_text.csv')
    user_to_bytes(f'{os.getcwd()}/bytes.txt', csv_users)