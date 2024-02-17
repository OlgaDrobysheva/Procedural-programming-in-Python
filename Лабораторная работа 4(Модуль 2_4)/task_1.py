class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} - {self.age} years old"

    def __repr__(self) -> str:
        return f"Animal(name='{self.name}', age={self.age})"


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def voice(self) -> str:
        return "Meow Meow!"

    def hunting(self, victim: str) -> str:
        return f"{self.name} caught a new victim: {victim}"


if __name__ == "__main__":
    first_cat = Cat(name="Barsik", age=2, color="White")
    print(first_cat)
    print(first_cat.voice())
    print(first_cat.hunting("Mouse"))
