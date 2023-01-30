class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. "

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"
        
    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def set_name(self, name):
        self._name = name

    def set_author(self, author):
        self._author = author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages >= 0:
                self._pages = pages
            else:
                raise ValueError
        else:
            raise TypeError
            
    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, " \
               f"author={self._author!r}, " \
               f"pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, int):
            if duration >= 0:
                self.duration = duration
            else:
                raise ValueError
        else:
            raise TypeError

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}," \
               f" author={self._author!r}, " \
               f" duration={self.duration})"

