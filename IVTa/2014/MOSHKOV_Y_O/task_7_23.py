# Задача 7. Вариант 23
# Создайте игру, в которой компьютер загадывает название одного 
# из семи дней недели, а игрок должен его угадать.

# Moshkov Y. O.
# 31.03.2016

import random
week = ["Понедельник", "Вторник", "Среда", 
"Четверг", "Пятница", "Суббота", "Воскресенье"]
number = random.randint(0, 6)
day = week[number].lower()

inputDay = input("Угадайте один из семи дней недели: ")
score = 6
while inputDay != day:
        inputDay = input("Вы не угадали, попробуйте ещё раз: ")
        if (score > 0):
                score -= 1
out = "Вы угадали! Ваш счёт " + str(score) + ". Нажмите Enter для выхода."
input(out)