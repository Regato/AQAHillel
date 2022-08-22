from unittest import TestCase

from Dice import Dice
from Game import Game


class TestDice(TestCase):
    def setUp(self) -> None:
        self.dice_obj = Dice()
        print('Testing starts...')

        return self.dice_obj

    def tearDown(self) -> None:
        print('Testing done!')

        del self.dice_obj

    def test_scores(self):
        self.assertEqual(self.dice_obj.scores, 1)

    def test_set_scores(self):
        self.dice_obj.set_scores(3)

        self.assertEqual(self.dice_obj.scores, 3)


class TestGame(TestCase):
    def setUp(self) -> None:
        self.game_obj = Game()
        print('Testing starts...')

        return self.game_obj

    def tearDown(self) -> None:
        print('Testing done!')

        del self.game_obj

    def test_dices(self):
        dices = [d.scores for d in self.game_obj.dices]

        self.assertEqual(dices, [1, 1, 1])

    def test_throw1(self):
        throw = self.game_obj.throw(3, 3, 3)

        self.assertEqual(throw, 300)

    def test_throw2(self):
        throw = self.game_obj.throw(1, 2, 2)

        self.assertEqual(throw, 20)

    def test_throw3(self):
        throw = self.game_obj.throw(2, 2, 1)

        self.assertEqual(throw, 20)

    def test_throw4(self):
        throw = self.game_obj.throw(1, 2, 1)

        self.assertEqual(throw, 10)