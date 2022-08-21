from Machine import Client
from Machine import CoffeeMachine
from Machine import CoffeeType, CoffeeAdditives, CupSize

if __name__ == '__main__':
    coffee_client = Client('Yehor', 'Romanov')
    coffee_automat = CoffeeMachine()

    coffee_automat.get_payment(50)
    coffee_automat.take_order(coffee_client,
                              CupSize.SMALL_CUP,
                              CoffeeType.ROBUSTA,
                              CoffeeAdditives.WITHOUT_ADDITIVES
                              )

    print(f'Your personal card is now {coffee_client.personal_card}')

    print('=========================================================')

    coffee_automat.get_payment(90)
    coffee_automat.take_order(coffee_client,
                              CupSize.SMALL_CUP,
                              CoffeeType.ROBUSTA,
                              CoffeeAdditives.MILK
                              )

    print(f'Your personal card is now {coffee_client.personal_card}')

    print('=========================================================')

    coffee_automat.get_payment(105)
    coffee_automat.take_order(coffee_client,
                              CupSize.SMALL_CUP,
                              CoffeeType.ARABICA,
                              CoffeeAdditives.WITHOUT_ADDITIVES
                              )

    print(f'Your personal card is now {coffee_client.personal_card}')

    print('=========================================================')

    coffee_automat.get_payment(280)
    coffee_automat.take_order(coffee_client,
                              CupSize.MEDIUM_CUP,
                              CoffeeType.ARABICA,
                              CoffeeAdditives.COLLAGEN
                              )

    print(f'Your personal card is now {coffee_client.personal_card}')

    print('=========================================================')

    coffee_automat.get_payment(350)
    coffee_automat.take_order(coffee_client,
                              CupSize.MEDIUM_CUP,
                              CoffeeType.ARABICA,
                              CoffeeAdditives.CACAO
                              )

    print(f'Your personal card is now {coffee_client.personal_card}')