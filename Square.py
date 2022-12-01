from typing import Union
import doctest


class Square:
    def __init__(self, line: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Параллелограмм"
        :param line: Сторона Квадрата
        :param square_value: Площадь параллелограмма
        :param perimeter_value: Периметр Параллелограмма

        Примеры:
        >>> rectangle = Square(1)
        """
        self.line = None
        self.square_value = None
        self.perimeter_value = None
        self.__init_line(line)

    def __init_line(self, line: Union[int, float]) -> None:
        """
        Инициализирует и проверяет значение первого отрезка
        :param line: Длина стороны квадрата
        :return: Нет
        :raise TypeError: длина выражается числом
        :raise ValueError: длина больше нуля
        Пример:
        >>> g = Square(1)
        >>> g.line
        1
        """
        if not isinstance(line, (int, float)):
            raise TypeError("Длина отрезка должна быть выражена числом")
        if line <= 0:
            raise ValueError("Длина отрезка должна быть больше нуля")
        self.line = line

    def square(self) -> Union[int, float]:
        """
        Вычисляет площадь
        :return: Число-площадь
        Примеры:
        >>> g = Square(1)
        >>> g.square()
        1.0

        """
        self.square_value = float(self.line * self.line)
        return self.square_value

    def perimeter(self) -> Union[int, float]:
        """
        Вычисляет периметр
        :return: Число - периметр
        Пример:
        >>> g = Square(1)
        >>> g.perimeter()
        4.0
        """
        self.perimeter_value = float(4*self.line)
        return self.perimeter_value

    def __str__(self) -> str:
        """
        Переводит в строку, в которой перечислены атрибуты
        :return: Строка
        Пример:
        >>> g = Square(1)
        >>> print(g)
        Сторона квадрата: 1
        """
        return f"Сторона квадрата: {self.line}"


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod() #тестирование примеров, которые находятся в документации