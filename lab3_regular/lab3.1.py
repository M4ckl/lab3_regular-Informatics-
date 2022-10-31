import re

isu = 373753
print(f"Вариант: {isu%6}")


def repeat(text):
    new_text = re.findall(r'(\w+)\s\1', text)
    for i in new_text:
        text = text.replace(i+' ', "", 1)
    print(text)


#5 тестов
repeat("1.Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова.Смешно, не не правда ли?Не нужно портить хор хоровод.")
repeat("2.ITMO is is more than than a university")
repeat("3.Раз Два Три Три")
repeat("4.Маша Даша Саша Саша Никита")
repeat("5.Программная инженерия и компьютерные технологии технологии")