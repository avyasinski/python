from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.setWindowTitle('Simple PROG')
		self.setGeometry(300, 200, 800, 600)

		self.main_text = QtWidgets.QLabel(self)
		self.main_text.setText('Надпись')
		self.main_text.move(100, 100)
		self.main_text.adjustSize()

		self.btn = QtWidgets.QPushButton(self)
		self.btn.move(70, 150)
		self.btn.setText('ЖМИ')
		self.btn.setFixedWidth(200)
		self.btn.clicked.connect(self.add_label)


	def add_label(self):
		print('add')


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
