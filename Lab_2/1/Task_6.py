
list = input("Введите элементы списка через пробел: ")
sp_list = list.split()


unique_list = []


for element in sp_list:

    if element not in unique_list:
        unique_list.append(element)


print("Список без дубликатов:", unique_list)
