# Задание 1
import re

isu = 373753
print(isu)
eyes = [":", ";", "X", "8", "="]
noses = ["-", "<", "-{", "<{"]
mouths = ["(", ")", "O", "|", "\\", "/", "P"]

smile = fr"{eyes[isu%5]}{noses[isu%4]}{mouths[isu%7]}"

print(f"Смайлик {isu%5}{isu%4}{isu%7} - {smile}")

print("Способ 1")


# Способ 1
def number_of_occurrences(text, smile_s=smile):
    print(f"Количество вхождений смайлика - {text.count(smile_s)} в сообщении:", text)


# Проверочных 5 тестов
number_of_occurrences(f"Это мои смайлики - {smile} {smile} {smile}")
number_of_occurrences(f"{smile} и  это мой - {smile}")
number_of_occurrences(f":-) или =-<)")
number_of_occurrences(f"{smile} {smile} {smile} {smile}")
number_of_occurrences(f"{smile} :-/ Hello this is my {smile}")

print("Способ 2")


# Способ 2
def number_of_occurrences_1(text, smile_s=smile):
    count = 0
    text1 = text.split(" ")
    for i in range(0, len(text1)):
        if text1[i] == smile_s:
            count += 1
        else:
            continue
    print(f"Количество вхождений смайлика -{count} в сообщении:", text)


# Проверочных 5 тестов
number_of_occurrences_1(f"Это мои смайлики - {smile} {smile} {smile}")
number_of_occurrences_1(f"{smile} и  это мой - {smile}")
number_of_occurrences_1(f":-) или =-<)")
number_of_occurrences_1(f"{smile} {smile} {smile} {smile}")
number_of_occurrences_1(f"{smile} :-/ Hello this is my {smile}")

print("Способ 3")


def regular_smile(text):
    num_smile = re.findall(r"\d\<\d", text)
    print(len(num_smile))


regular_smile("Это мои смайлики - 8<0 8<0 8<0 8<0")