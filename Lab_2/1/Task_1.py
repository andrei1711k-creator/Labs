text = input("Введите строку: ")

words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = words.count(word)

for word, count in word_counts.items():
    if count == 1:
        print(f"Слово '{word}' уникальное")
    else:
        print(f"Слово '{word}' встречается {count} раз")



