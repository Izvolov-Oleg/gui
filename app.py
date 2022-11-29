import sys
import time

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication


# noinspection PyUnresolvedReferences
class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Simple app")
        self.setGeometry(300, 250, 350, 200)

        self.main_text = QLabel(self)
        self.main_text.setText('Base')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('Push me')
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

        self.new_text = QLabel(self)
        self.new_text2 = QLabel(self)

    def add_label(self):
        self.new_text.setText("Second label")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()