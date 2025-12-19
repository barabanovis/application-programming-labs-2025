class FileIterator:
    def __init__(self, annotation_file):
        with open(annotation_file, 'r') as csv_file:
            self.data = csv_file.readlines()
            self.ind = 0
            self.length = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.ind < self.length):
            line = self.data[self.ind]
            if line[-1] == '\n':
                line = line[:-1]
            self.ind += 1
            return line
        else:
            raise StopIteration
