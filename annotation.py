import os
import csv


def create_annotation_csv(root_dir, output_csv, base_dir=None):
    """
    Создаёт CSV с абсолютными и относительными путями к файлам.
    """
    if base_dir is None:
        base_dir = root_dir

    with open(output_csv, 'w+', encoding='utf-8') as file:
        writer = csv.writer(file)

        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                absolute_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(absolute_path, base_dir)
                writer.writerow([absolute_path, relative_path])
