
sum = int(input("Введите сумму в рублях (целое число): "))


nominals = [100, 50, 10, 5, 2, 1]
result = {}

remaining = sum
for nominal in nominals:
    count = remaining // nominal
    if count > 0:
        result[nominal] = count
    remaining %= nominal

print(f"Сумма для размена: {sum} руб.")
for nominal, count in result.items():
    if nominal >= 10:
        print(f"{nominal} руб. купюр: {count}")
    else:
        print(f"{nominal} руб. монет: {count}")
