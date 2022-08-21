import datetime


class Human:
    population = 0

    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.__class__.count_population()

    @classmethod
    def count_population(cls, input_value=None):
        if input_value is None:
            cls.population += 1
            message = 'New human was born'
        else:
            cls.population += input_value
            message = 'New human was born'

        return message

    def enter_birth_date(self, birth_date=None):
        if birth_date is None:
            message = 'Nothing changed!'
        else:
            today = datetime.date.today()
            output_age = (today - birth_date).days // 365
            self.age = output_age
            message = f'Age was changed to: {self.age}.'

        return message

    def eat(self, food):
        message = f'{self.name} is eating {food}.'

        return message

    def sleep(self):
        message = f'{self.name} is sleeping  on the bed.'

        return message

    def speak(self, sentence):
        message = f'{self.name} says {sentence}'

        return message

    def walk(self, where=None):
        if where is None:
            message = f'{self.name} is walking anywhere!'
        else:
            message = f'{self.name} walks to {where}'

        return message

    def stay(self):
        message = f'{self.name} is staying.'

        return message

    def lie(self):
        message = f'{self.name} lies.'

        return message

    def __del__(self):
        self.__class__.population = 0
        pass
