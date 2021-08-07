import sys
from pytube import YouTube
import time

from YouTube_dl import Ui_MainWindow
from EnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal

title = ''
duration = ''
items = []
mutex = QMutex()


class Manager(QObject):
    finished = pyqtSignal()
    UPDATE = pyqtSignal()

    def get_data_from_URL(self, URL):
        print('I am here')
        global title
        global items
        mutex.lock()

        video = YouTube(URL)
        title = video.title

        streams = video.streams

        for s in streams:
            if s.abr == None:
                s_abr = ''
            else:
                s_abr = f'/{s.abr}'
            if s.resolution == None:
                s_resolution = ''
            else:
                s_resolution = f'/{s.resolution}'

            item = f'{s.mime_type}{s_resolution}{s_abr}/{s.filesize}'
            items.append(item)
        
        print(f'title = {title}')

        self.UPDATE.emit()
        mutex.unlock()
        self.finished.emit()


class Persenolize(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Persenolize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.show()
        self.enter = Enter_url_window()
        self.add.clicked.connect(lambda: self.enter.show())
        

class Enter_url_window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(590, 247)

        self.threads = []
        self.ui.ok.clicked.connect(self.startThreads)

    def update(self):
        global title
        global items
        self.ui.video_title.setText(f"title = {title}")
        self.ui.video_duration.setText(f"duration = {duration}")
        self.ui.video_title.adjustSize()
        self.ui.video_duration.adjustSize()

        self.ui.comboBox.addItems(items)
        self.setFixedWidth(590)
        self.setFixedHeight(500)

    def createThread(self, URL):
        thread = QThread()
        worker = Manager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.get_data_from_URL(URL))
        worker.UPDATE.connect(self.update)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def startThreads(self):
        self.threads.clear()
        URL = self.ui.lineEdit.text()
        self.threads = [
            self.createThread(URL)
        ]

        for thread in self.threads:
            thread.start()

    


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())
