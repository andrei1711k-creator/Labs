
numbers1 = input("Введите первый набор чисел через пробел: ")
sp_numbers1 = numbers1.split()
numbers2 = input("Введите второй набор чисел через пробел: ")
sp_numbers2 = numbers2.split()


number_list1 = []
for number_str in sp_numbers1:
    if '.' in number_str:
        number_list1.append(float(number_str))
    else:
        number_list1.append(int(number_str))




number_list2 = []
for number_str in sp_numbers2:
    if '.' in number_str:
        number_list2.append(float(number_str))
    else:
        number_list2.append(int(number_str))


sovp_numbers = []
for number1 in number_list1:
    for number2 in number_list2:
        if number1 == number2 and number1 not in sovp_numbers:
            sovp_numbers.append(number1)
print("Числа, присутствующие в обоих наборах:", sovp_numbers)


uni_to_first = []
for number in number_list1:
    if number not in number_list2 and number not in uni_to_first:
        uni_to_first.append(number)
print("Числа, которые есть только в первом наборе:", uni_to_first)


uni_to_second = []
for number in number_list2:
    if number not in number_list1 and number not in uni_to_second:
        uni_to_second.append(number)
print("Числа, которые есть только во втором наборе:", uni_to_second)


combined_numbers= []
for number in number_list1:
    if number not in sovp_numbers and number not in combined_numbers:
        combined_numbers.append(number)
for number in number_list2:
    if number not in sovp_numbers and number not in combined_numbers:
        combined_numbers.append(number)
print("Числа из обоих наборов без общих чисел:", combined_numbers)
