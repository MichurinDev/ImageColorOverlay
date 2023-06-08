# Имортируем библиотеки
from PIL import Image
from random import randint
import os

#  Шаблон апельсина
path = "orange_bw.png"
non_change_colors = [(0, 0, 0)]  # Цвета, которые не изменяем
orange_count = 10  # Количество генерируемых апельсинов

for count in range(orange_count):
    # Открываем исхоодную картинку
    with Image.open(path) as img:
        obj = img.load()

    # Генерируем цвет нового апельсина
    new_orange_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    # Перебираем пиксели
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # Ели цвет пикселя отсутствует в списке неизменяемых цветов
            if obj[i, j] not in non_change_colors:
                # Смешиваем, убирая белый
                obj[i, j] = (obj[i, j][0] + new_orange_color[0] - 255,
                             obj[i, j][1] + new_orange_color[1] - 255,
                             obj[i, j][2] + new_orange_color[2] - 255)

    # Если нет папки GenerateResult — создаём
    if not os.path.exists("GenerateResult"):
        os.makedirs("GenerateResult")

    # Сохраняем в папке
    img.save(f"GenerateResult/{count + 1}.jpg")

    # Логгирование прогресса
    print(f"{count + 1}\t|\t{orange_count}")
