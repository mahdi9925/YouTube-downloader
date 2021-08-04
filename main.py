from YouTube_dl import Ui_MainWindow
from DialogEnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys



class Persenolize(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # super().__init__()
        super(Persenolize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.add.clicked.connect(self.enter)
        self.show()


    def enter(self):
        Enter_url()
class Enter_url(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.show()

app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())