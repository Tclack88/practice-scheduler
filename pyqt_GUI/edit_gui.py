# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


import datetime as dt
import hashlib
import os
import pandas as pd
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from practice_sched import Schedule
import time

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
        self.setScaledContents(True)

    def setPixmap(self, image):
        super().setPixmap(image)


class DragNDropBox(QWidget):
    def __init__(self):
        super().__init__()
        #self.resize(400, 400)
        self.setAcceptDrops(True)
        mainLayout = QVBoxLayout()
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        self.setLayout(mainLayout)
        self.current_image = None
        self.current_image_address = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
        self.resize(self.photoViewer.sizeHint())
        self.current_image_address = file_path # set file path for saving
        self.current_image = self.photoViewer.pixmap()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(672, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topButtonFrame = QtWidgets.QFrame(self.centralwidget)
        self.topButtonFrame.setObjectName("topButtonFrame")
        self.formLayout = QtWidgets.QFormLayout(self.topButtonFrame)
        self.formLayout.setObjectName("formLayout")
        self.addButton = QtWidgets.QPushButton(self.topButtonFrame)
        self.addButton.setObjectName("addButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.addButton)
        self.practiceButton = QtWidgets.QPushButton(self.topButtonFrame)
        self.practiceButton.setObjectName("practiceButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.practiceButton)
        self.verticalLayout.addWidget(self.topButtonFrame, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.itemBox = QtWidgets.QTextEdit(self.frame)
        self.itemBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.itemBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.itemBox.setObjectName("itemBox")
        self.gridLayout.addWidget(self.itemBox, 1, 1, 1, 3)
        self.cancelImageButton = QtWidgets.QPushButton(self.frame)
        self.cancelImageButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.cancelImageButton.setObjectName("cancelImageButton")
        self.gridLayout.addWidget(self.cancelImageButton, 4, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.notesBox = QtWidgets.QTextEdit(self.frame)
        sizePolicy.setHorizontalStretch(20)
        self.notesBox.setSizePolicy(sizePolicy)
        self.notesBox.setMaximumSize(QtCore.QSize(16777215, 200))
        self.notesBox.setObjectName("notesBox")
        self.gridLayout.addWidget(self.notesBox, 3, 1, 1, 3)
        self.notesLabel = QtWidgets.QLabel(self.frame)
        self.notesLabel.setObjectName("notesLabel")
        self.gridLayout.addWidget(self.notesLabel, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.imageBox = DragNDropBox()
        self.imageBox.setParent(self.frame)
        #self.imageBox.setMinimumSize(QtCore.QSize(200, 200))
        #self.imageBox.setMaximumSize(QtCore.QSize(150, 150))
        #self.imageBox.setBaseSize(QtCore.QSize(200,200))
        #self.imageBox.baseSize(QtCore.QSize(200))
        self.imageBox.setObjectName("imageBox")
        self.gridLayout.addWidget(self.imageBox, 4, 2, 1, 2, QtCore.Qt.AlignVCenter)
        self.itemLabel = QtWidgets.QLabel(self.frame)
        self.itemLabel.setObjectName("itemLabel")
        self.gridLayout.addWidget(self.itemLabel, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.addImageButton = QtWidgets.QPushButton(self.frame)
        self.addImageButton.setAutoDefault(False)
        self.addImageButton.setDefault(False)
        self.addImageButton.setFlat(False)
        self.addImageButton.setObjectName("addImageButton")
        self.gridLayout.addWidget(self.addImageButton, 4, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.completeButton = QtWidgets.QPushButton(self.frame)
        self.completeButton.setObjectName("completeButton")
        self.gridLayout.addWidget(self.completeButton, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.addButton, self.practiceButton)
        MainWindow.setTabOrder(self.practiceButton, self.completeButton)
        MainWindow.setTabOrder(self.completeButton, self.cancelButton)
        MainWindow.setTabOrder(self.cancelButton, self.itemBox)
        MainWindow.setTabOrder(self.itemBox, self.notesBox)
        MainWindow.setTabOrder(self.notesBox, self.cancelImageButton)
        MainWindow.setTabOrder(self.cancelImageButton, self.addImageButton)

        #self.schedule = Schedule() # The main storage component

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.practiceButton.setText(_translate("MainWindow", "Practice"))
        self.cancelImageButton.setText(_translate("MainWindow", "x"))
        self.notesLabel.setText(_translate("MainWindow", "Notes"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.itemLabel.setText(_translate("MainWindow", "Item"))
        self.addImageButton.setText(_translate("MainWindow", "+  image"))
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.addButton.clicked.connect(self.addButtonClicked)
        self.addImageButton.clicked.connect(self.imageButtonClicked)
        self.cancelImageButton.clicked.connect(self.cancelImageButtonClicked)
        self.cancelButton.clicked.connect(self.cancelButtonClicked)
        self.completeButton.clicked.connect(self.completeButtonClicked)

    def addButtonClicked(self):
        self.frame.show()
        self.topButtonFrame.hide()
        #print(self.schedule.storage.iloc[0])

    def imageButtonClicked(self):
        self.addImageButton.hide()
        self.imageBox.show()
        self.cancelImageButton.show()
        self.imageBox.resize(200,200)

    def cancelImageButtonClicked(self):
        self.cancelImageButton.hide()
        self.imageBox.hide()
        self.addImageButton.show()
        # clear image:
        self.imageBox = DragNDropBox()
        self.imageBox.setParent(self.frame)
        self.imageBox.setObjectName("imageBox")
        self.gridLayout.addWidget(self.imageBox, 4, 2, 1, 2, QtCore.Qt.AlignVCenter)
        self.imageBox.hide()

    def cancelButtonClicked(self):
        self.frame.hide()
        self.topButtonFrame.show()
        self.cancelImageButtonClicked()
        self.itemBox.setText("")  # clear any items added
        self.notesBox.setText("") # clear any notes added

    def completeButtonClicked(self):
        #TODO Connect to DB or Json
        self.frame.hide()
        self.topButtonFrame.show()
        self.itemBox.setText("")  # clear any items added
        self.notesBox.setText("") # clear any notes added
        current_image = self.imageBox.current_image
        print(dir(self.itemLabel))
        print(self.itemBox.toPlainText())
        print(self.itemBox.toPlainText())
        #file_path = self.imageBox.current_image_address
        #new_name = hashlib.md5(Image.open(file_path).tobytes()).hexdigest() #<- trouble
        #current_image.save(f'data/{new_name}.png',"PNG")
        self.cancelImageButtonClicked() # clear the image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.frame.hide()
    ui.imageBox.hide()
    ui.cancelImageButton.hide()
    MainWindow.show()
    sys.exit(app.exec_())
