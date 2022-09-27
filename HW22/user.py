from __future__ import annotations
from typing import List

import numpy as np

from gender import Gender


class User:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            email: str,
            gender: Gender
    ) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender

    @classmethod
    def from_csv(cls, csv_data: dict) -> List[User]:
        # Getting headers and data from a dict
        headers = csv_data['headers']
        data = csv_data['data']
        # Making lists from strings
        headers_split = headers.split(' ')
        pre_len = len(data)
        data_split = [data[index].split(' ') for index in range(pre_len)]
        # Taking length of lists
        header_len = len(headers_split)
        data_len = len(data_split)

        # Making empty list to return it
        user_list = list()

        # Check are headers providing usable data
        # Check is headers length equal data length
        if data_len == 1 and header_len == 4:
            # Making a new user from collected data
            new_user = User(
                first_name=data_split[0][0],
                last_name=data_split[0][1],
                email=data_split[0][2],
                gender=data_split[0][3]
            )

            # Appending User class object (user) to a list of users
            user_list.append(new_user)

            print('[FROM_CSV]: User is created successfully!')
        elif data_len > 1 and header_len == 4:
            # Getting index of current list and make an operation
            for index_list in range(data_len):
                # Getting current list
                current_list = data_split[index_list]
                # Making a new user from collected data
                new_user = User(
                    first_name=current_list[0],
                    last_name=current_list[1],
                    email=current_list[2],
                    gender=current_list[3]
                )

                # Appending User class object (user) to a list of users
                user_list.append(new_user)

            print('[FROM_CSV]: Users are created successfully!')
        else:
            print('[FROM_CSV]: Error, data from the CSV file are incorrect!')

        return user_list

    @property
    def firstAttribute(self):
        return self.__first_name

    @property
    def secondAttribute(self):
        return self.__last_name

    @property
    def thirdAttribute(self):
        return self.__email

    @property
    def fourthAttribute(self):
        return self.__gender
