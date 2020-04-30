# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnsolicitar.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vtnSolicitar(object):
    def setupUi(self, vtnSolicitar):
        vtnSolicitar.setObjectName("vtnSolicitar")
        vtnSolicitar.setWindowModality(QtCore.Qt.ApplicationModal)
        vtnSolicitar.resize(609, 362)
        vtnSolicitar.setStyleSheet("QPushButton:hover{\n"
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
"    background-color: #A3E6EE;\n"
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
" }\n"
"\n"
"QLineEdit\n"
"{\n"
"    border: 2px solid #006080;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #D0C293;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 2px solid #006080;\n"
"}\n"
"\n"
"QLabel{\n"
"        font: bold 14px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(vtnSolicitar)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblCedula = QtWidgets.QLabel(self.centralwidget)
        self.lblCedula.setObjectName("lblCedula")
        self.horizontalLayout.addWidget(self.lblCedula)
        self.leCedula = QtWidgets.QLineEdit(self.centralwidget)
        self.leCedula.setObjectName("leCedula")
        self.horizontalLayout.addWidget(self.leCedula)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblNombre = QtWidgets.QLabel(self.centralwidget)
        self.lblNombre.setObjectName("lblNombre")
        self.horizontalLayout_2.addWidget(self.lblNombre)
        self.leNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.leNombre.setObjectName("leNombre")
        self.horizontalLayout_2.addWidget(self.leNombre)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblApellido = QtWidgets.QLabel(self.centralwidget)
        self.lblApellido.setObjectName("lblApellido")
        self.horizontalLayout_3.addWidget(self.lblApellido)
        self.leApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.leApellido.setObjectName("leApellido")
        self.horizontalLayout_3.addWidget(self.leApellido)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lblSeccion = QtWidgets.QLabel(self.centralwidget)
        self.lblSeccion.setObjectName("lblSeccion")
        self.gridLayout.addWidget(self.lblSeccion, 0, 0, 1, 1)
        self.leSeccion = QtWidgets.QLineEdit(self.centralwidget)
        self.leSeccion.setObjectName("leSeccion")
        self.gridLayout.addWidget(self.leSeccion, 0, 1, 1, 1)
        self.lblTelefono = QtWidgets.QLabel(self.centralwidget)
        self.lblTelefono.setObjectName("lblTelefono")
        self.gridLayout.addWidget(self.lblTelefono, 0, 2, 1, 1)
        self.leTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.leTelefono.setObjectName("leTelefono")
        self.gridLayout.addWidget(self.leTelefono, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblCota = QtWidgets.QLabel(self.centralwidget)
        self.lblCota.setObjectName("lblCota")
        self.horizontalLayout_5.addWidget(self.lblCota)
        self.leCota = QtWidgets.QLineEdit(self.centralwidget)
        self.leCota.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.leCota.setPalette(palette)
        self.leCota.setDragEnabled(False)
        self.leCota.setReadOnly(True)
        self.leCota.setObjectName("leCota")
        self.horizontalLayout_5.addWidget(self.leCota)
        self.lblAutor = QtWidgets.QLabel(self.centralwidget)
        self.lblAutor.setObjectName("lblAutor")
        self.horizontalLayout_5.addWidget(self.lblAutor)
        self.leAutor = QtWidgets.QLineEdit(self.centralwidget)
        self.leAutor.setEnabled(True)
        self.leAutor.setReadOnly(True)
        self.leAutor.setObjectName("leAutor")
        self.horizontalLayout_5.addWidget(self.leAutor)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblTItulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTItulo.setObjectName("lblTItulo")
        self.horizontalLayout_6.addWidget(self.lblTItulo)
        self.leTitulo = QtWidgets.QLineEdit(self.centralwidget)
        self.leTitulo.setEnabled(True)
        self.leTitulo.setReadOnly(True)
        self.leTitulo.setObjectName("leTitulo")
        self.horizontalLayout_6.addWidget(self.leTitulo)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblEjemplar = QtWidgets.QLabel(self.centralwidget)
        self.lblEjemplar.setObjectName("lblEjemplar")
        self.horizontalLayout_7.addWidget(self.lblEjemplar)
        self.leEjemplar = QtWidgets.QLineEdit(self.centralwidget)
        self.leEjemplar.setEnabled(True)
        self.leEjemplar.setReadOnly(True)
        self.leEjemplar.setObjectName("leEjemplar")
        self.horizontalLayout_7.addWidget(self.leEjemplar)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblCarrera = QtWidgets.QLabel(self.centralwidget)
        self.lblCarrera.setObjectName("lblCarrera")
        self.horizontalLayout_8.addWidget(self.lblCarrera)
        self.leCarrera = QtWidgets.QLineEdit(self.centralwidget)
        self.leCarrera.setEnabled(True)
        self.leCarrera.setReadOnly(True)
        self.leCarrera.setObjectName("leCarrera")
        self.horizontalLayout_8.addWidget(self.leCarrera)
        self.lblSemestre = QtWidgets.QLabel(self.centralwidget)
        self.lblSemestre.setObjectName("lblSemestre")
        self.horizontalLayout_8.addWidget(self.lblSemestre)
        self.leSemestre = QtWidgets.QLineEdit(self.centralwidget)
        self.leSemestre.setEnabled(True)
        self.leSemestre.setReadOnly(True)
        self.leSemestre.setObjectName("leSemestre")
        self.horizontalLayout_8.addWidget(self.leSemestre)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 6, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnSolicitar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSolicitar.setObjectName("btnSolicitar")
        self.horizontalLayout_9.addWidget(self.btnSolicitar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setObjectName("btnSalir")
        self.horizontalLayout_9.addWidget(self.btnSalir)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        vtnSolicitar.setCentralWidget(self.centralwidget)

        self.retranslateUi(vtnSolicitar)
        self.btnSalir.clicked.connect(vtnSolicitar.close)
        QtCore.QMetaObject.connectSlotsByName(vtnSolicitar)

    def retranslateUi(self, vtnSolicitar):
        _translate = QtCore.QCoreApplication.translate
        vtnSolicitar.setWindowTitle(_translate("vtnSolicitar", "Solicitud"))
        self.lblCedula.setText(_translate("vtnSolicitar", "Cedula"))
        self.lblNombre.setText(_translate("vtnSolicitar", "Nombre"))
        self.lblApellido.setText(_translate("vtnSolicitar", "Apellido"))
        self.lblSeccion.setText(_translate("vtnSolicitar", "Seccion"))
        self.lblTelefono.setText(_translate("vtnSolicitar", "Telefono"))
        self.lblCota.setText(_translate("vtnSolicitar", "Cota"))
        self.lblAutor.setText(_translate("vtnSolicitar", "Autor"))
        self.lblTItulo.setText(_translate("vtnSolicitar", "Titulo"))
        self.lblEjemplar.setText(_translate("vtnSolicitar", "Ejemplar"))
        self.lblCarrera.setText(_translate("vtnSolicitar", "Carrera"))
        self.lblSemestre.setText(_translate("vtnSolicitar", "Semestre"))
        self.btnSolicitar.setText(_translate("vtnSolicitar", "Solicitar"))
        self.btnSalir.setText(_translate("vtnSolicitar", "Salir"))

