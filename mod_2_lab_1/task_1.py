import doctest
# TODO Написать 3 класса с документацией и аннотацией типов
class Cat:
    """
    Class representing a cat.

    Attributes:
    color (str): Цвет шерсти кота (например, черный, рыжий).
    age (int): Возраст животного.

    Methods:
    say_purr(self) -> str:
    Животное говорит "Мурр".

    catch_the_mouse(self) -> str:
    Животное охотится.

    feed_cat(self) -> str:
    Покормите животное.

    """

    def __init__(self, color: str, age: int) -> None:
        """
        Инициализируйте животное, указав цвет шерсти и возраст.
        Например:
        >>> cat = Cat("white", 3)

        Args:
        color (str): Цвет шерсти кота.
        age (int): Возраст животного.

        Raises:
        ValueError: Если возраст не является положительным целым числом.

        """

        self.color = color
        self.age = age
        ...
        # Initialization of attributes


class Products:
    """
    Class representing products.

    Attributes:
    type (str): Тип товара (например, фрукты, овощи, молочные изделия).
    price (int): Цена единицы товара.
    quantity (int): Количество товара в корзине.

    Methods:
    add_product(self, quantity: int) -> int:
    Добавить товар в корзину.

    delete_product(self, quantity: int) -> int:
    Удалить товар из корзины.

    product_review(self, feedback: str) -> str:
    Оставить отзыв на товар.

    """

    def __init__(self, type: str, price: int, quantity: int) -> None:
        """
        Инициализируйте клавиатуру с помощью раскладки и количества клавиш.
        Например:
        >>> product = Products("milk", 70, 2)

        Args:
        type (str): Тип товара.
        price (int): Цена единицы товара.
        quantity (int): Количество товара в корзине.

        Raises:
        ValueError: Если количество товара в корзине не является положительным целым числом.
        """

        self.type = type
        self.price = price
        self.quantity = quantity
        ...
        # Initialization of attributes


class Door:
    """
    Class representing a door.

    Attributes:
    material (str): Материал двери (например, дерево, металл).
    height (float): Высота двери в метрах.

    Methods:
    open(self) -> str:
    Открыть дверь.

    close(self) -> str:
    Закрыть дверь.

    lock(self) -> str:
    Запереть дверь.

    """

    def __init__(self, material: str, height: float) -> None:
        """
        Initialize a Door with material and height.
        Например:
        >>> door = Door("wood", 2.7)

        Args:
        material (str): Материал двери.
        height (float): Высота двери в метрах.

        Raises:
        ValueError: Если высота не является положительным числом.

        """

        self.material = material
        self.height = height
        ...
        # Initialization of attributes


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
