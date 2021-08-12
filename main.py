import sys
from pytube import YouTube, streams
import urllib.request

from YouTube_dl import Ui_MainWindow
from EnterURL import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal


items = []
tags = []

mutex = QMutex()
download_mutex = QMutex()


class Manager(QObject):
    finished = pyqtSignal()
    UPDATE = pyqtSignal()
    Handle_Progress = pyqtSignal(float)

    global tags

    def get_data_from_URL(self, URL):
        print('I am  in get_data_from_URL')
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
            item = f'{s.mime_type}{s_resolution}{s_abr} /{file_size}'
            items.append(item)

        print(f'title = {title}')
        self.UPDATE.emit()
        mutex.unlock()
        self.finished.emit()

    def download_video_Manger(self, index):
        print('hello')
        download_mutex.lock()
        for index_tag, tag in enumerate(tags):
            if index == index_tag:
                print(f'{index} = {index_tag} and tag = {tag}')
                stream = streams.get_by_itag(tag)
                url = stream.url
                urllib.request.urlretrieve(
                    url, stream.title, self.Handle_ProgressBar)

        download_mutex.unlock()
        self.finished.emit()

    def Handle_ProgressBar(self, blocknum, blocksize, totalsize):
        read_data = blocknum * blocksize
        if totalsize > 0:
            global download_percentage
            download_percentage = read_data * 100 / totalsize
            download_percentage = round(download_percentage, 2)
            self.Handle_Progress.emit(download_percentage)


class Persenolize(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Persenolize, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setFixedSize(1146, 732)

        

        self.show()

        self.threads = []

        self.add_btn.clicked.connect(self.Enter_url)
        self.ok_btn.clicked.connect(self.startThread_get_data_Thread)
        self.download_btn.clicked.connect(
            self.startThread_get_current_index_comboBox)

    def startThread_get_data_Thread(self):
        self.threads.clear()
        URL = self.Enter_links.text()
        self.Enter_links.setEnabled(False)
        self.ok_btn.setEnabled(False)
        self.threads.append(self.get_data_Thread(URL))
        self.threads[0].start()

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

    def update_Enter_url_window(self):
        global items
        self.comboBox_data.addItems(items)

    def startThread_get_current_index_comboBox(self):
        self.download_btn.setEnabled(False)
        index = self.comboBox_data.currentIndex()
        self.threads.append(self.download_Thread(index))
        self.threads[1].start()

    def download_Thread(self, index):
        print('I am in downloadThread')
        thread = QThread()
        worker = Manager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.download_video_Manger(index))
        worker.Handle_Progress.connect(self.Update_progress)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def Update_progress(self, download_percentage):
        print(download_percentage)
        self.prog_bar.setValue(download_percentage)
        if download_percentage >= 100:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Download successfully!")
                msg.setWindowTitle("Informaition")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    def Enter_url(self):
        self.setFixedSize(1146, 856)


# class Enter_url_window(QDialog):
#     def __init__(self, parent=None):
#         QDialog.__init__(self, parent)
#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)

#         self.setFixedSize(590, 247)

#         self.threads = []
#         self.ui.ok.clicked.connect(self.startThread_get_data_Thread)
#         self.ui.download.clicked.connect(
#             self.startThread_get_current_index_comboBox)

#     def update_Enter_url_window(self):
#         global title
#         global items
#         self.ui.video_title.setText(f"title = {title}")
#         self.ui.video_duration.setText(f"duration = {duration}")
#         self.ui.video_title.adjustSize()
#         self.ui.video_duration.adjustSize()
#         self.ui.comboBox.addItems(items)
#         self.setFixedWidth(590)
#         self.setFixedHeight(500)

#     def get_data_Thread(self, URL):
#         thread = QThread()
#         worker = Manager()
#         worker.moveToThread(thread)
#         thread.started.connect(lambda: worker.get_data_from_URL(URL))
#         worker.UPDATE.connect(self.update_Enter_url_window)
#         worker.finished.connect(thread.quit)
#         worker.finished.connect(worker.deleteLater)
#         thread.finished.connect(thread.deleteLater)
#         return thread

#     def download_Thread(self, index):
#         print('I am in downloadThread')
#         thread = QThread()
#         worker = Manager()
#         worker.moveToThread(thread)
#         thread.started.connect(lambda: worker.download_video_Manger(index))
#         # worker.Handle_Progress.connect(self.Update_progress)
#         worker.finished.connect(thread.quit)
#         worker.finished.connect(worker.deleteLater)
#         thread.finished.connect(thread.deleteLater)
#         return thread

#     # def Update_progress(self, download_percentage):
#     #     print('I am here')
#     #     self.main = Persenolize()
#     #     print(download_percentage)
#     #     self.main.prog_bar.setValue(download_percentage)
#     #     Persenolize.prog(download_percentage)
#     #     print(self.YouTubeDl.prog_bar.value())

#     def startThread_get_data_Thread(self):
#         self.threads.clear()
#         URL = self.ui.lineEdit.text()
#         self.threads.append(self.get_data_Thread(URL))
#         self.threads[0].start()

#     def startThread_get_current_index_comboBox(self):
#         self.ui.download.setEnabled(False)
#         index = self.ui.comboBox.currentIndex()
#         self.threads.append(self.download_Thread(index))
#         self.threads[1].start()


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())
