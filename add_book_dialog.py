# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_book_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1006, 721)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(610, 670, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 100, 891, 551))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.id_spinbox = QtWidgets.QSpinBox(self.splitter)
        self.id_spinbox.setObjectName("id_spinbox")
        self.name_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.description_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_input.setFont(font)
        self.description_input.setObjectName("description_input")
        self.isbn_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.isbn_input.setFont(font)
        self.isbn_input.setObjectName("isbn_input")
        self.page_count_spinbox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.page_count_spinbox.setFont(font)
        self.page_count_spinbox.setObjectName("page_count_spinbox")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yes.setFont(font)
        self.yes.setObjectName("yes")
        self.horizontalLayout.addWidget(self.yes)
        self.no = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.no.setFont(font)
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no)
        self.author_input = QtWidgets.QLineEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_input.setFont(font)
        self.author_input.setObjectName("author_input")
        self.year_spinbox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_spinbox.setFont(font)
        self.year_spinbox.setObjectName("year_spinbox")
        self.horizontalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Dialog"))
        self.label.setText(_translate("Dialog", "Edit Book"))
        self.label_2.setText(_translate("Dialog", "Id"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Description"))
        self.label_5.setText(_translate("Dialog", "Isbn"))
        self.label_7.setText(_translate("Dialog", "Page Count"))
        self.label_6.setText(_translate("Dialog", "Issued"))
        self.label_8.setText(_translate("Dialog", "Author"))
        self.label_9.setText(_translate("Dialog", "Year"))
        self.yes.setText(_translate("Dialog", "Yes"))
        self.no.setText(_translate("Dialog", "No"))
