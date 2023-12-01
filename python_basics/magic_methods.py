"""Magic Methods in python."""


from typing import Any


class MyClass:
    def __my_magic__(self, skil_level):
        return skil_level * 10


my_instance = MyClass()
skills_boost = my_instance.__my_magic__(1)
print(f"You're a {skills_boost}X developer!")


class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # def __repr__(self) -> str:
    #     return f"Vecot2D(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return 2

    def __add__(self, other: object) -> object:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: object) -> object:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        # Scalar multiplication
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        # Dot multiplication
        elif isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("Unsupported operand for type *")

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Index out of range.")

    def __call__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __getattr__(self, name: str):
        if name == "magnitude":
            return (self.x**2 + self.y**2) ** 0.5
        else:
            raise AttributeError(f"Vector2D object has not attribute {name}.")


v1 = Vector2D(3, 5)
print(v1)
v2 = Vector2D(3, 5)
print(v1 == v2)
print(len(v1))
result = v1 + v2
print(result)
result = v1 - v2
print(result)
result = v1 * v2
print(result)
result = v1 * 2
print(result)
print(v1[0])
print(v1[1])
# print(v1[2])
result = v1(3)
print(result)
print(v1.magnitude)
print(v1.latitude)
