class Plant:
    name: str
    height: float
    _age: int

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
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    tmp = rose.height
    rose._age = 30
    rose.show()

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()

    print(f"Growth this week: {round(rose.height - tmp, 2)}cm")

if __name__ == "__main__":
    main()