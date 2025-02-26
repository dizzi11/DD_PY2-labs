from typing import Any


class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация животного.
        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self._name = name  # _name сделан непубличным, так как изменять имя напрямую нежелательно
        self.age = age

    def __str__(self) -> str:
        return f"Животное: {self._name}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self._name!r}, age={self.age!r})"

    def make_sound(self) -> str:
        """
        Метод, который будет переопределяться в дочерних классах.
        """
        return "Какой-то звук"


class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        return f"Собака: {self._name}, порода: {self.breed}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Dog(name={self._name!r}, age={self.age!r}, breed={self.breed!r})"

    def make_sound(self) -> str:
        """
        Перегруженный метод make_sound, так как собака лает.
        """
        return "Гав-гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, уникальный для собак – приносит предмет.
        :param item: Предмет, который собака должна принести.
        :return: Строка с действием.
        """
        return f"{self._name} принес(ла) {item}!"
