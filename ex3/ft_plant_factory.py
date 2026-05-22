class Plant:
    name: str
    height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def grow(self) -> None:
        self.height += 0.8
        self.height = round(self.height, 1)

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Plant Factory Output ===")

    rose = Plant("Rose", 25.0, 30)
    print("Created: ", end="")
    rose.show()

    oak = Plant("Oak", 200.0, 365)
    print("Created: ", end="")
    oak.show()

    cactus = Plant("Cactus", 5.0, 90)
    print("Created: ", end="")
    cactus.show()

    sunflower = Plant("Sunflower", 80.0, 45)
    print("Created: ", end="")
    sunflower.show()

    fern = Plant("Fern", 15.0, 120)
    print("Created: ", end="")
    fern.show()


if __name__ == "__main__":
    main()