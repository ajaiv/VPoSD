# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_collector.ui'
#
# Created: Sun Nov 10 21:09:18 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(433, 477)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.qlist = QtGui.QListView(self.centralwidget)
        self.qlist.setGeometry(QtCore.QRect(90, 70, 256, 301))
        self.qlist.setObjectName(_fromUtf8("qlist"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.err_lbl = QtGui.QLabel(self.centralwidget)
        self.err_lbl.setGeometry(QtCore.QRect(20, 240, 381, 71))
        self.err_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.err_lbl.setObjectName(_fromUtf8("err_lbl"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(90, 170, 262, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.a = QtGui.QLineEdit(self.splitter)
        self.a.setObjectName(_fromUtf8("a"))
        self.lbl = QtGui.QLabel(self.splitter)
        self.lbl.setObjectName(_fromUtf8("lbl"))
        self.b = QtGui.QLineEdit(self.splitter)
        self.b.setObjectName(_fromUtf8("b"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 391, 351))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.plotBtn = QtGui.QPushButton(self.centralwidget)
        self.plotBtn.setGeometry(QtCore.QRect(170, 380, 85, 27))
        self.plotBtn.setObjectName(_fromUtf8("plotBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.err_lbl.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl.setText(QtGui.QApplication.translate("MainWindow", "x 10 ^", None, QtGui.QApplication.UnicodeUTF8))
        self.plotBtn.setText(QtGui.QApplication.translate("MainWindow", "plot", None, QtGui.QApplication.UnicodeUTF8))
        
        #chumma oru comment

