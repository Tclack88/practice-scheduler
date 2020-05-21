# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

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
        #self.photoViewer.setPixmap(QPixmap(file_path))
        self.photoViewer.setPixmap(QPixmap(file_path).scaledToWidth(400))#scaled(800,800,Qt.KeepAspectRatio))
        self.photoViewer.setPixmap(QPixmap(file_path).scaled(200,200,Qt.KeepAspectRatio))
        print(dir(self.photoViewer))
        self.resize(self.photoViewer.sizeHint())
        #print(self.photoViewer.sizeHint())
        print(self.photoViewer.size())

        #print(self.photoViewer.size()[0])
        print('PARENT')
        print(self.parent())

       


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("overflow:auto;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(250, 20, 51, 25))
        self.addButton.setObjectName("addButton")
        self.practiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.practiceButton.setGeometry(QtCore.QRect(310, 20, 71, 25))
        self.practiceButton.setObjectName("practiceButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 591, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cancelButton = QtWidgets.QPushButton(self.frame)
        self.cancelButton.setGeometry(QtCore.QRect(290, 0, 71, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.completeButton = QtWidgets.QPushButton(self.frame)
        self.completeButton.setGeometry(QtCore.QRect(200, 0, 81, 25))
        self.completeButton.setObjectName("completeButton")
        self.itemLabel = QtWidgets.QLabel(self.frame)
        self.itemLabel.setGeometry(QtCore.QRect(10, 20, 41, 20))
        self.itemLabel.setObjectName("itemLabel")
        self.itemBox = QtWidgets.QTextEdit(self.frame)
        self.itemBox.setGeometry(QtCore.QRect(50, 40, 501, 31))
        self.itemBox.setStyleSheet("overflow:scroll")
        self.itemBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.itemBox.setObjectName("itemBox")
        self.notesLabel = QtWidgets.QLabel(self.frame)
        self.notesLabel.setGeometry(QtCore.QRect(10, 70, 51, 20))
        self.notesLabel.setObjectName("notesLabel")
        self.notesBox = QtWidgets.QTextEdit(self.frame)
        self.notesBox.setGeometry(QtCore.QRect(50, 90, 501, 131))
        self.notesBox.setObjectName("notesBox")

        #self.imageWidget = QtWidgets.QWidget(self.frame)
        self.imageWidget = DragNDropBox() # change class as defined above
        self.imageWidget.setGeometry(QtCore.QRect(220, 230, 150, 150))
        self.imageWidget.setGeometry(QtCore.QRect(220, 230, 150, 150))
        #self.imageWidget.setAcceptDrops(True)
        #self.imageWidget.setAccessibleName("")
        #self.imageWidget.setAutoFillBackground(False)
        #self.imageWidget.setStyleSheet("border: 4px dashed #aaa;")
        self.imageWidget.setObjectName("imageWidget")
        self.imageWidget.setParent(self.frame)

        self.addImageButton = QtWidgets.QPushButton(self.frame)
        self.addImageButton.setGeometry(QtCore.QRect(50, 220, 71, 25))
        self.addImageButton.setAutoDefault(False)
        self.addImageButton.setDefault(False)
        self.addImageButton.setFlat(False)
        self.addImageButton.setObjectName("addImageButton")
        self.cancelImageButton = QtWidgets.QPushButton(self.frame)
        self.cancelImageButton.setGeometry(QtCore.QRect(20, 220, 21, 25))
        self.cancelImageButton.setObjectName("cancelImageButton")
        self.frame.raise_()
        self.addButton.raise_()
        self.practiceButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.practiceButton.setText(_translate("MainWindow", "Practice"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.itemLabel.setText(_translate("MainWindow", "Item"))
        self.notesLabel.setText(_translate("MainWindow", "Notes"))
        self.addImageButton.setText(_translate("MainWindow", "+  image"))
        self.cancelImageButton.setText(_translate("MainWindow", "x"))
        self.addButton.clicked.connect(self.addButtonClicked)
        self.addImageButton.clicked.connect(self.imageButtonClicked)
        self.cancelImageButton.clicked.connect(self.cancelImageButtonClicked)
        self.cancelButton.clicked.connect(self.cancelButtonClicked)

    def addButtonClicked(self):
        self.frame.show()
        self.addButton.hide()
        self.practiceButton.hide()

    def imageButtonClicked(self):
        self.addImageButton.hide()
        self.imageWidget.show()
        self.cancelImageButton.show()

    def cancelImageButtonClicked(self):
        self.cancelImageButton.hide()
        self.imageWidget.hide()
        self.addImageButton.show()

    def cancelButtonClicked(self):
        self.frame.hide()
        self.addButton.show()
        self.practiceButton.show()
        self.cancelImageButtonClicked()
        #TODO Connect to DB or Json
        self.itemBox.setText("")  # clear any items added
        self.notesBox.setText("") # clear any notes added

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.frame.hide()
    ui.imageWidget.hide()
    ui.cancelImageButton.hide()
    MainWindow.show()
    sys.exit(app.exec_())
