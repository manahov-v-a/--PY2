import math
from typing import Union


class Parallelogram:
    def __init__(self, line_one: Union[int, float], line_two: Union[int, float], angle: Union[int, float] = 90):
        """ Доступ к длинам и углу закрыт, чтобы после определения нельзя
        было поменять всё

        Создание и подготовка к работе объекта "Параллелограмм"
        :param line_one: Сторона один
        :param line_two: Сторона два
        :param angle: Угол между сторонами один и два, в градусах
        :param square_value: Площадь параллелограмма
        :param perimeter_value: Периметр Параллелограмма
        """

        self._line_one = None
        self._line_two = None
        self._angle = None
        self.square_value = None
        self.perimeter_value = None
        self.__init_line_one(line_one)
        self.__init_line_two(line_two)
        self.__init_angle(angle)

    def __init_line_one(self, line_one: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение первого отрезка
        :param line_one: Длина первого отрезка
        :return: Нет
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля

        """
        if not isinstance(line_one, (int, float)):
            raise TypeError("Длина отрезка должна быть выражена числом")
        if line_one <= 0:
            raise ValueError("Длина отрезка должна быть больше нуля")
        self._line_one = line_one

    def __init_line_two(self, line_two: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение второго отрезка
        :param line_two:
        :return: Net
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля

        """
        if not isinstance(line_two, (int, float)):
            raise TypeError("Длина отрезка должна быть выражена числом")
        if line_two <= 0:
            raise ValueError("Длина отрезка должна быть больше нуля")
        self._line_two = line_two

    def __init_angle(self, angle: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение угла
        :param angle: Угол
        :return: Нет
        :raise TypeError: угол выражается числом

        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Выразите угол числом")
        self._angle = angle / 180 * math.pi

    def get_perimeter(self) -> float:
        """
        Вычисляет периметр
        :return: Число - периметр
        """
        self.perimeter_value = 2 * (self._line_one + self._line_two)
        return self.perimeter_value

    def get_square(self) -> float:
        """
        Вычисляет площадь
        :return: Число-площадь
        """
        self.square_value = self._line_one * self._line_two * math.sin(self._angle)
        return self.square_value

    def __str__(self) -> str:
        """
        Переводит в строку, в которой перечислены атрибуты
        :return: Строка
        """
        return f"Сторона один: {self._line_one}, " \
               f"сторона два: {self._line_two}, " \
               f"угол между ними: {self._angle / math.pi * 180} градусов"

    def __repr__(self) -> str:
        """
        Переводит в формальное строковое представление.
        :return: строка
        """
        return f"{self.__class__.__name__}(line_one={self._line_one}, " \
               f"line_two={self._line_two}, angle={self._angle / math.pi * 180})"


class Rectangle(Parallelogram):

    def __init__(self, line_one: Union[int, float], line_two: Union[int, float]):
        """
        Заполняет объект Прямоугольник. Методы наследуются
        :param line_one: Сторона 1
        :param line_two: Сторона 2
        """
        super().__init__(line_one, line_two)

    def get_square(self) -> float:
        """ Перегружен, т.к. иная формула вычисления площади """
        """
        Вычисляет площадь
        :return: Число-площадь
        """
        self.square_value = self._line_one * self._line_two
        return self.square_value

    def __str__(self) -> str:
        """
        Переводит в строку, в которой перечислены атрибуты
        :return: Строка
        """
        return f"Сторона один: {self._line_one}, " \
               f"сторона два: {self._line_two}"

    def __repr__(self) -> str:
        """
        Переводит в формальное строковое представление.
        :return: строка
        """
        return f"{self.__class__.__name__}(line_one={self._line_one}, " \
               f"line_two={self._line_two})"


if __name__ == "__main__":
    pf = Parallelogram(1, 1.5, 90)
    print(pf.get_square())
    pass
