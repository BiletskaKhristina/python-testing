class Figure:
    def __init__(self, figure_type, length):
        allowed = ["квадрат", "прямокутник", "трикутник"]

        if figure_type not in allowed:
            raise ValueError("Невідомий тип фігури")

        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль")

        self.figure_type = figure_type
        self.length = length

    def get_figure_type(self):
        return self.figure_type

    def get_figure_length(self):
        if self.figure_type == "квадрат":
            return self.length * 4
        if self.figure_type == "прямокутник":
            return self.length * 2
        return self.length * 3

    def get_angles(self):
        if self.figure_type == "квадрат":
            return [90, 90, 90, 90]
        if self.figure_type == "прямокутник":
            return [90, 90, 90, 90]
        return [60, 60, 60]


def count_vowels(text):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯaeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def get_number():
    number = int(input("Введіть число: "))
    if number <= 0:
        raise ValueError("Число має бути більшим за нуль")
    return number
