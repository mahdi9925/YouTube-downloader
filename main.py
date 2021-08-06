import sys
import pafy
import time

from YouTube_dl import Ui_MainWindow
from EnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal

title = ''
mutex = QMutex()


class AccountManager(QObject):
    finished = pyqtSignal()
    updatedBalance = pyqtSignal()

    def withdraw(self, URL):
        # self.ui = Ui_Dialog()

        global title
        print('i am here3')
        mutex.lock()

        video = pafy.new(URL)
        # print(video.title())
        title = video.title()

        # self.ui.video_title.setText(f"title = {title}")

        self.updatedBalance.emit()
        mutex.unlock()
        self.finished.emit()


class Persenolize(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Persenolize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.show()

        self.add.clicked.connect(self.add_url)

    def add_url(self):
        self.enter = Enter_url_window()
        self.enter.show()


class Enter_url_window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(590, 247)

        self.threads = []

        self.ui.ok.clicked.connect(self.change_window_size)
        self.ui.ok.clicked.connect(self.startThreads)

    def updateBalance(self):
        global title
        self.ui.video_title.setText(f"title = {title}")
        self.ui.video_title.adjustSize()

    def createThread(self, URL):
        print('i am here1')
        thread = QThread()
        worker = AccountManager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.withdraw(URL))

        worker.updatedBalance.connect(self.updateBalance)

        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def startThreads(self):
        print('i am here2')
        self.threads.clear()
        URL = self.ui.lineEdit.text()
        self.threads = [
            self.createThread(URL)
        ]

        for thread in self.threads:
            thread.start()

    def change_window_size(self):
        self.setFixedWidth(590)
        self.setFixedHeight(500)


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())
