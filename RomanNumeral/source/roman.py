def convert(number: str) -> int:
    """Convert a Roman numeral to an integer."""

    if not isinstance(number, str):
        raise TypeError("Input must be a string")

    number = number.upper().strip()

    if not number:
        raise ValueError("Input cannot be empty")

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Check for invalid characters
    for character in number:
        if character not in roman:
            raise ValueError(f"Invalid Roman numeral: {character}")

    # Convert Roman numeral to integer
    total = 0

    for i in range(len(number)):
        if i + 1 < len(number) and roman[number[i]] < roman[number[i + 1]]:
            total -= roman[number[i]]
        else:
            total += roman[number[i]]

    # Check if the Roman numeral is written correctly
    if to_roman(total) != number:
        raise ValueError(f"Invalid Roman numeral: {number} . Please write Valid Roman Numeral.")

    return total


def to_roman(number: int) -> str:
    """Convert an integer to a Roman numeral for validation."""

    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = []

    for value, symbol in values:
        while number >= value:
            result.append(symbol)
            number -= value

    return "".join(result)


if __name__ == "__main__":

    while True:
        print("\n--- Roman Numeral Converter ---")
        print("1. Convert Roman Numeral")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Thank you for using the Roman Numeral Converter! See you next time.")
            break

        if choice == "1":
            try:
                user_input = input("Enter a Roman Numeral: ")
                result = convert(user_input)
                print(f"{user_input.upper().strip()} = {result}")

            except (ValueError, TypeError) as error:
                print(f"Error: {error}")

        else:
            print("Invalid choice. Please select 1 or 2.")