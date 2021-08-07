import sys
from pytube import YouTube, streams
import time

from YouTube_dl import Ui_MainWindow
from EnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal

title = ''
duration = ''
items = []
tags = []
mutex = QMutex()
download_mutex = QMutex()


class Manager(QObject):
    finished = pyqtSignal()
    UPDATE = pyqtSignal()

    global tags

    def get_data_from_URL(self, URL):
        print('I am  in get_data_from_URL')
        global title
        global items
        global streams
        mutex.lock()

        video = YouTube(URL)
        title = video.title
        streams = video.streams

        for s in streams.order_by('itag'):
            tags.append(s.itag)

            if s.abr == None:
                s_abr = ''
            else:
                s_abr = f' /{s.abr}'

            if s.resolution == None:
                s_resolution = ''
            else:
                s_resolution = f' /{s.resolution}'

            file_size = f'{round(s.filesize * 1e-6 ,1)} MB'
            print(s.filesize, file_size)
            item = f'{s.mime_type}{s_resolution}{s_abr} /{file_size}'
            items.append(item)

        print(f'title = {title}')
        self.UPDATE.emit()
        mutex.unlock()
        self.finished.emit()

    def download_video_Manger(self, index):
        download_mutex.lock()
        for index_tag, tag in enumerate(tags):
            if index == index_tag:
                stream = streams.get_by_itag(tag)
                print(stream)
        download_mutex.unlock()
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
        self.ui.ok.clicked.connect(self.startThread_get_data_Thread)
        self.ui.download.clicked.connect(
            self.startThread_get_current_index_comboBox)

    def update_Enter_url_window(self):
        global title
        global items
        self.ui.video_title.setText(f"title = {title}")
        self.ui.video_duration.setText(f"duration = {duration}")
        self.ui.video_title.adjustSize()
        self.ui.video_duration.adjustSize()
        self.ui.comboBox.addItems(items)
        self.setFixedWidth(590)
        self.setFixedHeight(500)

    def get_data_Thread(self, URL):
        thread = QThread()
        worker = Manager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.get_data_from_URL(URL))
        worker.UPDATE.connect(self.update_Enter_url_window)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def download_Thread(self, index):
        print('I am in downloadThread')
        thread = QThread()
        worker = Manager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.download_video_Manger(index))
        # worker.UPDATE.connect(self.update)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def startThread_get_data_Thread(self):
        self.threads.clear()
        URL = self.ui.lineEdit.text()
        self.threads.append(self.get_data_Thread(URL))
        self.threads[0].start()

    def startThread_get_current_index_comboBox(self):
        index = self.ui.comboBox.currentIndex()
        self.threads.append(self.download_Thread(index))
        self.threads[1].start()


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())
