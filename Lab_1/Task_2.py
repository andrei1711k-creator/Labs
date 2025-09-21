

text = input("Введите строку: ")

vowels = "aeiouAEIOU"
res = ""

for i in text:
    if i not in vowels:
        res +=i




print("Исходная строка:", text)
print("Строка без гласных:", res)
