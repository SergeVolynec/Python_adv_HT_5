"""Напишите функцию, которая принимает на вход строку
- абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов:
путь, имя файла, расширение файла."""

from os import path

link = "E:\Документы\Сдача квартиры\ДОГОВОР.docx"

def file_info(link):
    file_name = path.basename(link)
    name, extension = file_name.split('.')
    file_path = path.split(link)[0]
    return file_path, name, extension


if __name__ == '__main__':
    print(file_info(link))
