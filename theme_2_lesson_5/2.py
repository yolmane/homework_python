word = input("Введите слово: ")

vowels = "aeiou"
vowels_count = 0
consonants_count = 0

for letter in word:
    if letter.isalpha():
        if letter.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    else:
        print(False)
        break
print(f"Кол-во гласных букв: {vowels_count}")
print(f"Кол-во согласных букв: {consonants_count}")