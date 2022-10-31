import re

isu = 373753
print(f"Вариант: {isu%4}")


def words_with_vowels(text):
    matches = re.findall(r"[а-яА-ЯёЁ]+", text)
    res = []
    for i in matches:
        letters = re.findall(r"[уеыаоэяию]+", i)
        flag = False
        if len(letters):
            for letter in range(0, len(letters)):
                if letters[letter] != letters[letter - 1]:
                   flag = True
                   break
        if not flag:
            res.append(i)
        else:
            flag = True

    res.sort(key=len)
    text_1 = (' '.join(res))
    text_1 = text_1.split(" ")

    for word in range(len(text_1)):
        print(text_1[word])


words_with_vowels("Классное слово – обороноспособность,которое должно идти после слов: трава и молоко.")
#words_with_vowels("Добро пожаловать в наш уютный дом на поборежье моря")
#words_with_vowels("Погода дождливая и ветер сильный")