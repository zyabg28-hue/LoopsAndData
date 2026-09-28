def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s.isalnum():
        return False

    first_digit_index = None
    for i, ch in enumerate(s):
        if ch.isdigit():
            first_digit_index = i
            break

    if first_digit_index is not None:
        if first_digit_index == 0 or s[first_digit_index] == "0":
            return False
        if any(ch.isalpha() for ch in s[first_digit_index + 1:]):
            return False

    return True


main()
