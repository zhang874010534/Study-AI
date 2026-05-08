from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """接收两个数字并返回它们的和。"""
    return a + b


if __name__ == "__main__":
    print(add(1, 2))
