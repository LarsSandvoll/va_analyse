# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'va_analyse_dialogR_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VLAnalyseDialogBaseResult(object):
    def setupUi(self, VLAnalyseDialogBaseResult):
        VLAnalyseDialogBaseResult.setObjectName("VLAnalyseDialogBaseResult")
        VLAnalyseDialogBaseResult.resize(453, 283)
        self.gridLayout = QtWidgets.QGridLayout(VLAnalyseDialogBaseResult)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(VLAnalyseDialogBaseResult)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(VLAnalyseDialogBaseResult)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(VLAnalyseDialogBaseResult)
        self.buttonBox.accepted.connect(VLAnalyseDialogBaseResult.accept)
        self.buttonBox.rejected.connect(VLAnalyseDialogBaseResult.reject)
        QtCore.QMetaObject.connectSlotsByName(VLAnalyseDialogBaseResult)

    def retranslateUi(self, VLAnalyseDialogBaseResult):
        _translate = QtCore.QCoreApplication.translate
        VLAnalyseDialogBaseResult.setWindowTitle(_translate("VLAnalyseDialogBaseResult", "Dialog"))

