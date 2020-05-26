from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.utils import iface
import os.path


class Ui_VAAnalyseDialogBaseResult(object):
    def setupUi(self, VAAnalyseDialogBaseResult, worksheet):
        VAAnalyseDialogBaseResult.setObjectName("VAAnalyseDialogBaseResult")
        VAAnalyseDialogBaseResult.resize(500, 350)
        self.gridLayout = QGridLayout(VAAnalyseDialogBaseResult)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QDialogButtonBox(VAAnalyseDialogBaseResult)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.tableWidget = QTableWidget(VAAnalyseDialogBaseResult)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(9)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        
        self.tableWidget.setHorizontalHeaderLabels(["Gruppe","Total lengde","Total feil","Feil pr 100 km pr år"]) 
        I = 9
        for i in range(I):
            name = worksheet.cell(i+4,1).value
            self.tableWidget.setItem(i,0, QTableWidgetItem(str(name)))
            lengde = worksheet.cell(i+4,2).value
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(lengde)))
            lekkajser = worksheet.cell(i+4,3).value
            self.tableWidget.setItem(i,2, QTableWidgetItem(str(lekkajser)))
            number =  worksheet.cell(i+4,5).value
            self.tableWidget.setItem(i,3, QTableWidgetItem(str(number)))
            
        self.tableWidget.resizeColumnsToContents() 
        self.retranslateUi(VAAnalyseDialogBaseResult)
        self.buttonBox.accepted.connect(VAAnalyseDialogBaseResult.accept)
        self.buttonBox.rejected.connect(VAAnalyseDialogBaseResult.reject)
        QMetaObject.connectSlotsByName(VAAnalyseDialogBaseResult)

    def retranslateUi(self, VAAnalyseDialogBaseResult):
        _translate = QCoreApplication.translate
        VAAnalyseDialogBaseResult.setWindowTitle(_translate("VAAnalyseDialogBaseResult", "Resultat"))
            

class MyDialog(QDialog):
    def __init__(self, worksheet):
        super().__init__()
        self.ui = Ui_VAAnalyseDialogBaseResult()
        self.ui.setupUi(self,worksheet)
        