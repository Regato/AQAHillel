from enum import Enum
from enum import auto
from enum import unique


@unique
class Gender(Enum):
    MALE = auto()
    FEMALE = auto()
