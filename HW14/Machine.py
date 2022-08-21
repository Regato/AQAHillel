from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import ClassVar


class DiscountEnum(Enum):
    FIRST_DISCOUNT = 0.5
    SECOND_DISCOUNT = 1.5
    THIRD_DISCOUNT = 2
    FOURTH_DISCOUNT = 3


@dataclass
class Human(ABC):
    """Takes first_name and last_name attributes"""
    first_name: str
    last_name: str

    @abstractmethod
    def calc_plus_discount(self, value):
        pass


@dataclass
class Client(Human):
    """Takes discount attribute (ENUM field)"""
    personal_card: ClassVar[float] = 0.0

    def calc_plus_discount(self, discount: DiscountEnum):
        # Sum of discount value + personal card
        discount_value = discount.value
        self.__class__.personal_card += discount_value
        print(f'You got {discount_value} points to your personal card, may be next time? :)')


class CupSize(Enum):
    SMALL_CUP = ('Small', 25)
    MEDIUM_CUP = ('Medium', 50)
    LARGE_CUP = ('Large', 100)


class CoffeeType(Enum):
    ARABICA = ('Arabica', 80)
    ROBUSTA = ('Robusta', 20)


class CoffeeAdditives(Enum):
    WITHOUT_ADDITIVES = ('Without Additives', 0)
    MILK = ('Milk', 5)
    CHOCOLATE = ('Chocolate', 50)
    COLLAGEN = ('Collagen', 130)
    CINNAMON = ('Cinnamon', 200)
    BUTTER = ('Butter', 100)
    ADAPTOGENS = ('Adaptogens', 130)
    CACAO = ('Cacao', 200)
    TURMERIC = ('Turmeric', 50)
    CARMADON = ('Carmadon', 50)
    RAW = ('Raw', 100)
    HONEY = ('Honey', 100)


class NotEnoughMoneyError(Exception):
    pass


@dataclass
class CoffeeMachine(object):
    """Takes nothing"""
    box_office: ClassVar[float] = 10000
    payment: ClassVar[float] = 0.0

    def get_payment(self, value):
        # Get payment from user
        self.__class__.payment += value

    def take_order(self, client_object,
                   cup_size: CupSize,
                   coffee_type: CoffeeType,
                   coffee_additives: CoffeeAdditives):
        # Get an order from user
        order_sum = cup_size.value[1] + coffee_type.value[1] + coffee_additives.value[1]

        # Check is order sum degree payment
        if order_sum == self.__class__.payment:
            # Take money from user to box office
            self.__class__.box_office += order_sum

            # Give points to user
            if order_sum >= 300:
                client_object.calc_plus_discount(DiscountEnum.FOURTH_DISCOUNT)
            elif order_sum >= 250:
                client_object.calc_plus_discount(DiscountEnum.THIRD_DISCOUNT)
            elif order_sum >= 100:
                client_object.calc_plus_discount(DiscountEnum.SECOND_DISCOUNT)
            elif order_sum >= 50:
                client_object.calc_plus_discount(DiscountEnum.FIRST_DISCOUNT)
            else:
                print('You got 0 points to your personal card, may be next time? :)')

            # Make payment 0 and print it
            self.__class__.payment = 0.0

        # Check is order sum smaller than payment
        elif order_sum < self.__class__.payment:
            # Make change for user and take it from box office
            # Take money from user to box office
            change = self.__class__.payment - order_sum
            self.__class__.box_office -= change
            self.__class__.box_office += order_sum

            # Give points to user
            if order_sum >= 300:
                client_object.calc_plus_discount(DiscountEnum.FOURTH_DISCOUNT)
            elif order_sum >= 250:
                client_object.calc_plus_discount(DiscountEnum.THIRD_DISCOUNT)
            elif order_sum >= 100:
                client_object.calc_plus_discount(DiscountEnum.SECOND_DISCOUNT)
            elif order_sum >= 50:
                client_object.calc_plus_discount(DiscountEnum.FIRST_DISCOUNT)
            else:
                print('You got 0 points to your personal card, may be next time? :)')

            # Make payment 0 and print it
            self.__class__.payment = 0.0
            print(f'Your change is {change}')

        else:
            raise NotEnoughMoneyError('Your payment is not enough for your coffee order')
