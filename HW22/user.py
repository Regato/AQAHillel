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
        headers = csv_data['headers']
        data = csv_data['data']
        headers_split = headers.split(' ')
        data_split = data[0].split(' ')
        header_len = len(headers_split)
        data_len = len(data_split)
        data_count = data_len // header_len

        user_list = list()

        if header_len == 4 and header_len == data_len:
            new_user = User(
                first_name=data_split[0],
                last_name=data_split[1],
                email=data_split[2],
                gender=data_split[3]
            )

            user_list.append(new_user)
        else:
            data_arr = np.array(data_split)
            data_split = np.array_split(data_arr, data_count)
            np.array_split()

            for index_arr in range(data_count):
                current_arr = data_split[index_arr]
                new_user = User(
                    first_name=current_arr[0],
                    last_name=current_arr[1],
                    email=current_arr[2],
                    gender=current_arr[3]
                )

                user_list.append(new_user)

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
