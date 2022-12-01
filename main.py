# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import math
import doctest


class Parallelogram:
    def __init__(self, line_one: Union[int, float], line_two: Union[int, float],
                 angle: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Параллелограмм"
        :param line_one: Сторона один
        :param line_two: Сторона два
        :param angle: Угол между сторонами один и два, в градусах
        :param square: Площадь параллелограмма
        :param perimeter: Периметр Параллелограмма

        Примеры:
        >>> parallelogram = Parallelogram(1,2,3)
        """
        self.line_one = None
        self.line_two = None
        self.square = None
        self.perimeter = None
        self.__init_line_one(line_one)
        self.__init_line_two(line_two)
        self.angle = None
        self.__init_angle(angle)

    def __init_angle(self, angle: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение угла
        :param angle: Угол
        :return: Нет
        :raise TypeError: угол выражается числом
        Пример:
        >>> g = Parallelogram(1, 2, 90)
        >>> g.angle
        1.5707963267948966
        """
        if not isinstance(angle, (int, float)):
            raise TypeError("Выразите угол числом")
        self.angle = angle/180 * math.pi

    def __init_line_one(self, line_one: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение первого отрезка
        :param line_one: Длина первого отрезка
        :return: Нет
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля
        Пример:
        >>> g = Parallelogram(1, 2, 90)
        >>> g.line_one
        1
        """
        if not isinstance(line_one, (int, float)):
            raise TypeError("Длина отрезка должна быть выражена числом")
        if line_one <= 0:
            raise ValueError("Длина отрезка должна быть больше нуля")
        self.line_one = line_one

    def __init_line_two(self, line_two: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение второго отрезка
        :param line_two:
        :return: Net
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля
        Пример:
        >>> g = Parallelogram(1, 2, 90)
        >>> g.line_two
        2

        """
        if not isinstance(line_two, (int, float)):
            raise TypeError("Длина отрезка должна быть выражена числом")
        if line_two <= 0:
            raise ValueError("Длина отрезка должна быть больше нуля")
        self.line_two = line_two

    def square(self) -> Union[int, float]:
        """
        Вычисляет площадь
        :return: Число-площадь
        Примеры:
        >>> g = Parallelogram(1, 2, 90)
        >>> g.square()
        2.0

        """
        return self.line_one * self.line_two * math.sin(self.angle)

    def perimeter(self) -> Union[int, float]:
        """
        Вычисляет периметр
        :return: Число - периметр
        Пример:
        >>> g = Parallelogram(1, 2, 90)
        >>> g.perimeter()
        6
        """
        return 2*(self.line_one + self.line_two)

    def __str__(self) -> str:
        """
        Переводит в строку, в которой перечислены атрибуты
        :return: Строка
        Пример:
        >>> g = Parallelogram(1, 2, 90)
        >>> print(g)
        Сторона один: 1, сторона два: 2, угол между ними: 90.0 градусов
        """
        return f"Сторона один: {self.line_one}, " \
               f"сторона два: {self.line_two}, " \
               f"угол между ними: {self.angle / math.pi * 180} градусов"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod() #тестирование примеров, которые находятся в документации