# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("overflow:auto;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.addImageButton.setGeometry(QtCore.QRect(70, 270, 71, 25))
        self.addImageButton.setAutoDefault(False)
        self.addImageButton.setDefault(False)
        self.addImageButton.setFlat(False)
        self.addImageButton.setObjectName("addImageButton")
        self.itemBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.itemBox.setGeometry(QtCore.QRect(70, 90, 481, 31))
        self.itemBox.setStyleSheet("overflow:scroll")
        self.itemBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.itemBox.setTabChangesFocus(True)
        self.itemBox.setReadOnly(False)
        self.itemBox.setObjectName("itemBox")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(230, 20, 51, 25))
        self.addButton.setObjectName("addButton")
        self.practiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.practiceButton.setGeometry(QtCore.QRect(288, 20, 71, 25))
        self.practiceButton.setObjectName("practiceButton")
        self.notesBox = QtWidgets.QTextEdit(self.centralwidget)
        self.notesBox.setGeometry(QtCore.QRect(70, 140, 481, 131))
        self.notesBox.setObjectName("notesBox")
        self.imageWidget = QtWidgets.QWidget(self.centralwidget)
        self.imageWidget.setGeometry(QtCore.QRect(70, 270, 481, 151))
        self.imageWidget.setObjectName("imageWidget")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(290, 50, 71, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.completeButton = QtWidgets.QPushButton(self.centralwidget)
        self.completeButton.setGeometry(QtCore.QRect(198, 50, 81, 25))
        self.completeButton.setObjectName("completeButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(36, 70, 41, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 120, 51, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addImageButton.setText(_translate("MainWindow", "+  image"))
        self.itemBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.practiceButton.setText(_translate("MainWindow", "Practice"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.label.setText(_translate("MainWindow", "Item"))
        self.label_2.setText(_translate("MainWindow", "Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
