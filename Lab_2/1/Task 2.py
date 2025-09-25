
input_numbers = input("Введите числа через пробел: ")
split_numbers = input_numbers.split()

number_list = []
for number_string in split_numbers:
    if '.' in number_string:
        number_list.append(float(number_string))
    else:
        number_list.append(int(number_string))


un_numbers = []
for number in number_list:
    if number_list.count(number) == 1:
        un_numbers.append(number)
print("Уникальные числа:", un_numbers)

rep_numbers = []
for number in number_list:
    if number_list.count(number) > 1 and number not in rep_numbers:
        rep_numbers.append(number)
print("Повторяющиеся числа:", rep_numbers)


chet_numbers = []
for number in number_list:
    if isinstance(number, int):
        if number % 2 == 0:
            chet_numbers.append(number)
print("Четные числа:", chet_numbers)


ne_chet_numbers = []
for number in number_list:
    if isinstance(number, int):
        if number % 2 != 0:
            ne_chet_numbers.append(number)
print("Нечетные числа:", ne_chet_numbers)


negative_numbers = []
for number in number_list:
    if number < 0:
        negative_numbers.append(number)
print("Отрицательные числа:", negative_numbers)


float_numbers = []
for number in number_list:
    if isinstance(number, float):
        float_numbers.append(number)
print("Числа с плавающей точкой:", float_numbers)


sum_of_five = 0
for number in number_list:
    if isinstance(number, int):
        if number % 5 == 0:
            sum_of_five += number
print("Сумма чисел, кратных 5:", sum_of_five)


max_number = number_list[0]
for number in number_list:
    if number > max_number:
        maximum_number = number
print("Самое большое число:", max_number)


min_number = num_list[0]
for number in number_list:
    if number < minimum_number:
        minimum_number = number
print("Самое маленькое число:", min_number)
