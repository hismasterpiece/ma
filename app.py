def pyramid(height: int) -> None:
    if not isinstance(height, int) or isinstance(height, bool) or height < 0:
        raise ValueError("height must be a non-negative integer")

    for row in range(1, height + 1):
        print(" " * (height - row) + "#" * (2 * row - 1))


if __name__ == "__main__":
    pyramid(int(input("Height: ")))