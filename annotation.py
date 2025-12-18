import os
import csv


def create_annotation_csv(root_dir, output_csv, base_dir=None):
    """
    Создаёт CSV с абсолютными и относительными путями к файлам.
    
    root_dir: папка, в которой ищем файлы
    output_csv: путь к выходному CSV-файлу
    base_dir: базовая директория для относительного пути (если None — берётся root_dir)
    """
    if base_dir is None:
        base_dir = root_dir

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['absolute_path', 'relative_path'])

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                absolute_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(absolute_path, base_dir)
                writer.writerow([absolute_path, relative_path])
