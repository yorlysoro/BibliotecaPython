# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vntconsulta.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vtnConsulta(object):
    def setupUi(self, vtnConsulta):
        vtnConsulta.setObjectName("vtnConsulta")
        vtnConsulta.resize(745, 468)
        vtnConsulta.setStyleSheet("QPushButton:hover{\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 yellow);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 green);\n"
"}\n"
"QComboBox{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #86E094;\n"
"    selection-color: yellow;;\n"
"      border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    color: black;\n"
"    font: bold 12px\n"
"}\n"
"QComboBox:hover{\n"
"    border: 1px solid  #D0C293;\n"
"    color: yellow;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"QHeaderView::section {\n"
"    background-color: QLinearGradient(x1: 5, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #F1EEE1);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color:  QLinearGradient(x1: 5, y1: 0, x2: 0, y2: 3, stop: 0 #2198c0, stop: 1 #F1EEE1);\n"
"    gridline-color: #E4EE9A;\n"
"     border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: white;\n"
"     border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QMainWindow{\n"
"     background-color:  QLinearGradient(x1: 5, y1: 0, x2: 0, y2: 3, stop: 0 #2198c0, stop: 1 #F1EEE1);\n"
"}\n"
"QPushButton {\n"
"            margin: 4px;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"            background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #A3E6EE);\n"
" }")
        self.centralwidget = QtWidgets.QWidget(vtnConsulta)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboSemestre = QtWidgets.QComboBox(self.centralwidget)
        self.comboSemestre.setObjectName("comboSemestre")
        self.comboSemestre.addItem("")
        self.comboSemestre.addItem("")
        self.comboSemestre.addItem("")
        self.horizontalLayout.addWidget(self.comboSemestre)
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName("btnBuscar")
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tablaConsulta = QtWidgets.QTableWidget(self.centralwidget)
        self.tablaConsulta.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaConsulta.setObjectName("tablaConsulta")
        self.tablaConsulta.setColumnCount(0)
        self.tablaConsulta.setRowCount(0)
        self.verticalLayout.addWidget(self.tablaConsulta)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnSolicitar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSolicitar.setObjectName("btnSolicitar")
        self.horizontalLayout_2.addWidget(self.btnSolicitar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout_2.addWidget(self.btnSalir)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        vtnConsulta.setCentralWidget(self.centralwidget)

        self.retranslateUi(vtnConsulta)
        self.btnSalir.clicked.connect(vtnConsulta.close)
        QtCore.QMetaObject.connectSlotsByName(vtnConsulta)

    def retranslateUi(self, vtnConsulta):
        _translate = QtCore.QCoreApplication.translate
        vtnConsulta.setWindowTitle(_translate("vtnConsulta", "Solicitud"))
        self.comboSemestre.setItemText(0, _translate("vtnConsulta", "Semestre 1"))
        self.comboSemestre.setItemText(1, _translate("vtnConsulta", "Semestre 3"))
        self.comboSemestre.setItemText(2, _translate("vtnConsulta", "Semestre 5"))
        self.btnBuscar.setText(_translate("vtnConsulta", "Buscar"))
        self.btnSolicitar.setText(_translate("vtnConsulta", "Solicitar"))
        self.btnSalir.setText(_translate("vtnConsulta", "Salir"))

