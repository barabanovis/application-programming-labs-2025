from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import QSize
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")


        self.label = QLabel()
        self.button = QPushButton()

        self.button.clicked.connect(self.button_click)

        def button_click(self):
            

    def button_toggle(self, checked):
        self.button_cheched = checked
        print(self.button_cheched)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
