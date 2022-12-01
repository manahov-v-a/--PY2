from typing import Union
import doctest


class Rectangle:
    def __init__(self, line_one: Union[int, float], line_two: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Параллелограмм"
        :param line_one: Сторона один
        :param line_two: Сторона два
        :param square_value: Площадь параллелограмма
        :param perimeter_value: Периметр Параллелограмма

        Примеры:
        >>> rectangle = Rectangle(1,2)
        """
        self.line_one = None
        self.line_two = None
        self.square_value = None
        self.perimeter_value = None
        self.__init_line_one(line_one)
        self.__init_line_two(line_two)

    def __init_line_one(self, line_one: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение первого отрезка
        :param line_one: Длина первого отрезка
        :return: Нет
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля
        Пример:
        >>> g = Rectangle(1, 2)
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
        >>> g = Rectangle(1, 2)
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
        >>> g = Rectangle(1, 2)
        >>> g.square()
        2.0

        """
        self.square_value = float(self.line_one * self.line_two)
        return self.square_value

    def perimeter(self) -> Union[int, float]:
        """
        Вычисляет периметр
        :return: Число - периметр
        Пример:
        >>> g = Rectangle(1, 2)
        >>> g.perimeter()
        6.0
        """
        self.perimeter_value = float(2*(self.line_one + self.line_two))
        return self.perimeter_value

    def __str__(self) -> str:
        """
        Переводит в строку, в которой перечислены атрибуты
        :return: Строка
        Пример:
        >>> g = Rectangle(1, 2)
        >>> print(g)
        Сторона один: 1, сторона два: 2
        """
        return f"Сторона один: {self.line_one}, " \
               f"сторона два: {self.line_two}"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod() #тестирование примеров, которые находятся в документации