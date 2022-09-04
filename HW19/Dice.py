class Dice(object):
    def __init__(self):
        self.__scores = 1

    @property
    def scores(self):
        return self.__scores

    def set_scores(self, num):
        self.__scores = num
