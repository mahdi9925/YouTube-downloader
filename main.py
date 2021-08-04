
from YouTube_dl import Ui_MainWindow
from DialogEnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class Persenolize(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Persenolize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.show()

        self.add.clicked.connect(self.add_url)
    
    def add_url(self):
        self.enter= Enter_url_window()
        self.enter.show()


class Enter_url_window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())