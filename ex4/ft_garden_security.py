class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        if height < 0:
            print("Error, height can't be negative")
            return None
        if age < 0:
            print("Error, height can't be negative")
            return None
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                "Error, height can't be negative\n"
                "Height update rejected"
            )
            return None
        self._height = height
    
    def set_age(self, age: int) -> None:
        if age < 0:
            print(
                "Error, age can't be negative\n"
                "Age update rejected"
            )
            return None
        self._age = age

    def get_height(self) -> float:
        return self._height
    
    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(
            f"{self._name}: {self._height}cm, {self._age} days old"
        )


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    
    rose.set_height(25)
    print(f"\nHeight updated: {rose._height}cm")
    rose.set_age(30)
    print(f"Age updated: {rose._age} days")

    print(f"\nRose: ", end="")
    rose.set_height(-2.0)
    print(f"Rose: ", end="")
    rose.set_age(-6)

    print("\nCurrent states: ", end="")
    rose.show()

if __name__ == "__main__":
    main()