class FileIterator:
    def __init__(self, annotation_file):
        with open(annotation_file, 'r') as csv_file:
            if annotation_file is None:
                raise ValueError
            self.data = csv_file.readlines()
            self.ind = 0
            self.length = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.ind < self.length):
            # Нужно вернуть только абсолютный путь для чтения картинки приложением
            line, trash = self.data[self.ind].split(',')
            self.ind += 2
            return line
        else:
            raise StopIteration
