# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTube_dl.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 650)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-radius: 20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius:5px;\n"
"    background-color: rgb(59, 61, 62);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(9, 9, 1110, 40))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setStyleSheet("background-color: rgb(26, 32, 37);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 3, 561, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: #51a8d6;\n"
"    border-radius: 3px;\n"
"    font-size:16px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #20a0e6;\n"
"    border-bottom: 2px solid #fff;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #156de8;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: #f2883d;\n"
"    border-radius: 3px;\n"
"    font-size:16px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #f07c29;\n"
"    border-bottom: 2px solid #fff;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #e3670e;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: #b463f2;\n"
"    border-radius: 3px;\n"
"    font-size:16px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #a646f0;\n"
"    border-bottom: 2px solid #fff;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #9826f0;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(9, 55, 1101, 521))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(128, 140, 140);\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 580, 61, 51))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.add_btn = QtWidgets.QPushButton(self.frame_3)
        self.add_btn.setGeometry(QtCore.QRect(0, 0, 54, 50))
        self.add_btn.setMaximumSize(QtCore.QSize(100, 100))
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"")
        self.add_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-add-96 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setIconSize(QtCore.QSize(50, 50))
        self.add_btn.setObjectName("add_btn")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 690, 1121, 33))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enter_links = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Enter_links.setFont(font)
        self.Enter_links.setStyleSheet("QLineEdit{\n"
"    border: 0.5px solid #000;\n"
"    selection-color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(0, 220, 106);\n"
"    color:#000;\n"
"    background-color: #e1e1e1;\n"
"    border-radius: 2px;\n"
"    margin-left: 5px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.Enter_links.setText("")
        self.Enter_links.setDragEnabled(True)
        self.Enter_links.setObjectName("Enter_links")
        self.horizontalLayout.addWidget(self.Enter_links)
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancel_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.cancel_btn.setMaximumSize(QtCore.QSize(100, 25))
        self.cancel_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    border: 2px solid #4580ff;\n"
"    background-color: #e1e1e1;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #9c9c9c;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #707070;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.ok_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_btn.setMaximumSize(QtCore.QSize(200, 25))
        self.ok_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ok_btn.setStyleSheet("QPushButton{\n"
"    border-radius: 3px;\n"
"    border: 2px solid #4580ff;\n"
"    background-color: #e1e1e1;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #9c9c9c;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #707070;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(13, 750, 991, 33))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_data = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_data.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_data.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox_data.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_data.setStyleSheet("QComboBox QAbstractItemView {\n"
"    border: 1px solid grey;\n"
"    background: #8e97d1;\n"
"    font-size: 18px;\n"
"    selection-background-color: rgb(66, 204, 123);\n"
"}\n"
"\n"
"QComboBox:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.comboBox_data.setObjectName("comboBox_data")
        self.horizontalLayout_2.addWidget(self.comboBox_data)
        self.saveTo_name = QtWidgets.QLineEdit(self.layoutWidget2)
        self.saveTo_name.setEnabled(True)
        self.saveTo_name.setMinimumSize(QtCore.QSize(700, 0))
        self.saveTo_name.setMaximumSize(QtCore.QSize(500, 25))
        self.saveTo_name.setStyleSheet("QLineEdit{\n"
"    selection-color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(0, 220, 106);\n"
"    color:#000;\n"
"    background-color: #e1e1e1;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.saveTo_name.setText("")
        self.saveTo_name.setObjectName("saveTo_name")
        self.horizontalLayout_2.addWidget(self.saveTo_name)
        self.save_file = QtWidgets.QToolButton(self.layoutWidget2)
        self.save_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_file.setStyleSheet("QToolButton:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.save_file.setObjectName("save_file")
        self.horizontalLayout_2.addWidget(self.save_file)
        self.prog_bar = QtWidgets.QProgressBar(self.frame)
        self.prog_bar.setGeometry(QtCore.QRect(80, 640, 1019, 20))
        self.prog_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.prog_bar.setStyleSheet("QProgressBar {\n"
"    color :#e1e1e1;\n"
"    font-size : 17px;\n"
"    border-style : none;\n"
"    border-radius: 10px;\n"
"    background-color : #325099;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius : 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.193, y1:0.346591, x2:0.79, y2:0.71, stop:0 rgba(77, 83,         198, 255), stop:1 rgba(23, 197, 23, 255));\n"
"}")
        self.prog_bar.setProperty("value", 0)
        self.prog_bar.setObjectName("prog_bar")
        self.download_btn = QtWidgets.QPushButton(self.frame)
        self.download_btn.setGeometry(QtCore.QRect(1020, 750, 100, 30))
        self.download_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.download_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.download_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(215, 134, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(106, 255, 123);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: #9c9a9b;\n"
"}")
        self.download_btn.setObjectName("download_btn")
        self.animation = QtWidgets.QLabel(self.frame)
        self.animation.setGeometry(QtCore.QRect(90, 590, 50, 50))
        self.animation.setText("")
        self.animation.setObjectName("animation")
        self.loading_text = QtWidgets.QLabel(self.frame)
        self.loading_text.setGeometry(QtCore.QRect(160, 587, 151, 41))
        self.loading_text.setText("")
        self.loading_text.setObjectName("loading_text")
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.pushButton.setText(_translate("MainWindow", "Downloader"))
        self.pushButton_2.setText(_translate("MainWindow", "YouTube"))
        self.pushButton_3.setText(_translate("MainWindow", "Instagram"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.add_btn.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Enter_links.setPlaceholderText(_translate("MainWindow", "Enter YouTube URL..."))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))
        self.cancel_btn.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.ok_btn.setText(_translate("MainWindow", "OK"))
        self.ok_btn.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveTo_name.setPlaceholderText(_translate("MainWindow", "Save to..."))
        self.save_file.setText(_translate("MainWindow", "..."))
        self.download_btn.setText(_translate("MainWindow", "Download"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
