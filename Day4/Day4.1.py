def validate_password(password):
    return there_are_2_adjacent_digits(password) and is_digits_increase_from_left_to_right(password)


def there_are_2_adjacent_digits(password):
    for i in range(len(password) - 1 ):
        if password[i] == password[i +1]:
            return True
    return False


def is_digits_increase_from_left_to_right(password):
    for i in range(len(password) - 1 ):
        if password[i] > password[i +1]:
            return False
    return True


with open("inputDay4.txt") as f:
    (start, stop) = f.readline().split("-")
    count = 0
    for i in range(int(start), int(stop)):
        password = str(i)
        if validate_password(password):
            count += 1
    print(f"Valid passwords in the range are : {count}")