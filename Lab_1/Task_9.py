ip = input("Введите IP-адрес: ")

parts = ip.split(".")
if len(parts) != 4:
    print("Некорректный IP-адрес")
else:
    correct = True
    for p in parts:
        if not p.isdigit():
            correct = False
            break
        num = int(p)
        if num < 0 or num > 255:
            correct = False
            break
    if correct:
        print("Корректный IP-адрес")
    else:
        print("Некорректный IP-адрес")
