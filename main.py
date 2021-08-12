import sys
from pytube import YouTube, streams
import urllib.request
import os

from YouTube_dl import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QMutex, QObject, QThread, pyqtSignal


items = []
tags = []
Path = '/home/user/Downloads'

mutex = QMutex()
download_mutex = QMutex()


class Manager(QObject):
    finished = pyqtSignal()
    UPDATE = pyqtSignal(str)
    Handle_Progress = pyqtSignal(float)

    global tags

    def get_data_from_URL(self, URL):
        print('I am  in get_data_from_URL')
        global items
        global streams
        global title
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
        self.UPDATE.emit(title)
        mutex.unlock()
        self.finished.emit()

    def download_video_Manger(self, index, FileName_andPath):
        download_mutex.lock()

        for index_tag, tag in enumerate(tags):
            if index == index_tag:
                print(f'{index} = {index_tag} and tag = {tag}')
                print(f'FileName and path = {FileName_andPath}')
                stream = streams.get_by_itag(tag)
                url = stream.url
                urllib.request.urlretrieve(
                    url, FileName_andPath, self.Handle_ProgressBar)
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
        self.setFixedSize(1150, 650)

        self.prog_bar.hide()

        self.comboBox_data.setEnabled(False)
        self.saveTo_name.setEnabled(False)
        self.save_file.setEnabled(False)
        self.download_btn.setEnabled(False)
        self.ok_btn.setEnabled(False)

        self.show()
        self.threads = []

        
        self.save_file.clicked.connect(self.get_path_save)
        self.Enter_links.textChanged.connect(self.enable_disable_btn)
        self.add_btn.clicked.connect(self.Enter_url)
        self.ok_btn.clicked.connect(self.startThread_get_data_Thread)
        self.download_btn.clicked.connect(
            self.startThread_get_current_index_comboBox)

    def enable_disable_btn(self):
        if len(self.Enter_links.text()) > 0:
            self.ok_btn.setEnabled(True)
        else:
            self.ok_btn.setEnabled(False)

    def get_path_save(self):
        save = os.path.join('/home/user/', title)
        Path = QFileDialog.getSaveFileName(
            self, 'Save to', save, options=QFileDialog.DontUseNativeDialog)
        self.saveTo_name.setText(Path[0])

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

    def update_Enter_url_window(self, title):
        global items
        global Path

        self.comboBox_data.addItems(items)
        self.comboBox_data.setEnabled(True)
        self.save_file.setEnabled(True)
        self.saveTo_name.setEnabled(True)
        self.download_btn.setEnabled(True)

        Name_Path = os.path.join(Path, title)
        self.saveTo_name.setText(Name_Path)
        self.setFixedSize(1150,820)

    def startThread_get_current_index_comboBox(self):
        self.download_btn.setEnabled(False)
        self.prog_bar.show()
        index = self.comboBox_data.currentIndex()
        FileName_andPath = self.saveTo_name.text()
        self.threads.append(self.download_Thread(index, FileName_andPath))
        self.threads[1].start()

    def download_Thread(self, index, FileName_andPath):
        print('I am in downloadThread')
        thread = QThread()
        worker = Manager()
        worker.moveToThread(thread)
        thread.started.connect(
            lambda: worker.download_video_Manger(index, FileName_andPath))
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
            self.download_btn.setEnabled(True)
            self.ok_btn.setEnabled(True)
            self.Enter_links.setEnabled(True)
            print(self.threads)

    def Enter_url(self):
        self.setFixedSize(1150, 750)
        self.Enter_links.setFocus()


app = QApplication(sys.argv)
main = Persenolize()
sys.exit(app.exec())
