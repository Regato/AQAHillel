import pytest

from Game import Game


class ConfigGame(object):
    game_obj = None


@pytest.fixture(scope="module", autouse=True)
def game_scope():
    ConfigGame.game_obj = Game()


@pytest.mark.parametrize('value1, value2, value3',
                         [(1, 1, 1), (1, 2, 1), (1, 1, 2),
                          (2, 2, 2), (2, 1, 2), (2, 1, 1),
                          (3, 3, 3), (3, 1, 3), (3, 1, 1),
                          (3, 2, 3), (3, 2, 2)])
def test_add_student(value1, value2, value3):
    result_throw = ConfigGame.game_obj.throw(value1, value2, value3)

    scores = [d for d in (value1, value2, value3)]

    if scores.count(scores[0]) == 3:
        check_result = scores[0] * 100
    elif scores.count(scores[0]) == 2:
        check_result = scores[0] * 10
    elif scores.count(scores[1]) == 2:
        check_result = scores[1] * 10

    assert result_throw == check_result
