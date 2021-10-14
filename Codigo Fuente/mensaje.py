
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'MENSAJE !!!!'
        self.left = 500
        self.top = 300
        self.width = 320
        self.height = 200
        # self.initUI()

    def initUI(self, mensaje):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        buttonReply = QMessageBox.warning(self, "Mensaje : ",mensaje, QMessageBox.Ok , QMessageBox.Ok)
        if buttonReply == QMessageBox.Ok:
            print('Haz Clickeado Ok.')
        else:
            print('Haz Clickeado No.') 
# app = QApplication(sys.argv)
# ex = App()
# ex.initUI("hola")
# sys.exit(app.exec_())