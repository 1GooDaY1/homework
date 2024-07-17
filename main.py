number_dict = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_index = 0

while number_index < len(number_dict):
    number = number_dict[number_index]
    if number > 0:
        print(number)
    number_index += 1
