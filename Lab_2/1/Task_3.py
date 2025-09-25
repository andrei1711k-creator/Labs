
input_numbers = input("Введите числа через пробел: ")
split_numbers = input_numbers.split()


number_list = []
for number_string in split_numbers:
    if '.' in number_string:
        number_list.append(float(number_string))
    else:
        number_list.append(int(number_string))


uni_numbers = []
for number in number_list:
    if number not in uni_numbers:
        uni_numbers.append(number)

max_number = uni_numbers[0]
for number in uni_numbers:
    if number > max_number:
        max_number = number


uni_numbers.remove(max_number)


second_max_number = uni_numbers[0]
for number in uni_numbers:
    if number > second_max_number:
        second_max_numer = number

print("Второе по величине число:", second_max_number)
