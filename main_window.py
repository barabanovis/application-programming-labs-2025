from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from iterator import FileIterator


class MainWindow(QWidget):
    def __init__(self):
        self.iter = FileIterator('results.csv')

        super().__init__()

        self.setWindowTitle("My Application")
        self.resize(400, 300)

        layout = QVBoxLayout()
        self.image_label = QLabel()
        layout.addWidget(self.image_label, 1)
        self.button = QPushButton("Next Image")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button, 0)

        self.setLayout(layout)

    def on_button_click(self):
        try:
            path = self.iter.__next__()
        except StopIteration:
            self.image_label.setText("You listed all images")

        pixmap = QPixmap(path)

        if pixmap.isNull():
            self.image_label.setText("Image not found!")
        else:
            self.image_label.setPixmap(pixmap)
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
