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
    def from_csv(cls, csv_line: dict) -> List[User]:
        users = list()

        for line in csv_line:
            user = User(**line)
            users.append(user)

        return users
