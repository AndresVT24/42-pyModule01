class Plant:
    name: str
    height: float
    _age: int

    def show(self) -> None:
        print(
            f"{self.name}: {self.height}cm, {self._age} days old"
        )

def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose._age = 30
    rose.show()

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower._age = 45
    sunflower.show()

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus._age = 120
    cactus.show()

if __name__ == "__main__":
    main()