import os
import csv


class FileIterator:
    def __iter__(self):
        return self

    def __next__(self):


def create_annotation_csv(root_dir, output_csv):
    """
    Создаёт CSV с абсолютными и относительными путями к файлам.

    root_dir: папка, в которой ищем файлы
    output_csv: путь к выходному CSV-файлу
    """
    if base_dir is None:
        base_dir = root_dir

    with open(output_csv, 'w+', encoding='utf-8') as file:
        writer = csv.writer(file)
