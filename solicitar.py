#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
__name__ = "solicitar"

from PyQt5 import QtSql
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from vtnsolicitar import Ui_vtnSolicitar
from solicitud import Solicitud
from PyQt5.QtCore import Qt
import time
class Solicitar(QMainWindow):
	def __init__(self, padre, db, COTA, AUTOR, TITULO, EJEMPLAR, CARRERA, SEMESTRE, SERIAL):
		QMainWindow.__init__(self, padre)
		self.solicitar = Ui_vtnSolicitar()
		self.solicitar.setupUi(self)
		self.solicitar.btnSalir.clicked.connect(lambda x: self.close() )
		self.solicitar.btnSolicitar.clicked.connect(self.__Guardar)
		self.setFixedSize(620, 318)
		self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
		
		self.COTA = COTA
		self.AUTOR = AUTOR
		self.TITULO = TITULO
		self.EJEMPLAR = EJEMPLAR
		self.CARRERA = CARRERA
		self.SEMESTRE = SEMESTRE
		self.SERIAL = SERIAL
		self.db = db
		
		self.__llenar()
	def __llenar(self):
		self.solicitar.leCota.setText(self.COTA)
		self.solicitar.leAutor.setText(self.AUTOR)
		self.solicitar.leTitulo.setText(self.TITULO)
		self.solicitar.leEjemplar.setText(self.EJEMPLAR)
		self.solicitar.leCarrera.setText(self.CARRERA)
		self.solicitar.leSemestre.setText(self.SEMESTRE)
		
	def __Guardar(self):
		Query = QtSql.QSqlQuery()
		self.db.open()
		Query.exec("SELECT CEDULA FROM entregas WHERE CEDULA = '%s'" %(self.solicitar.leCedula.text()))
		if self.solicitar.leCedula.text() != "" and self.solicitar.leNombre.text() != "" and self.solicitar.leApellido.text() != "":
			if Query.next():
				QMessageBox.warning(self, "Error", "%s Ya tiene un libro asignado" %(self.solicitar.leCedula.text()), QMessageBox.Ok)
			else:
				fecha = time.strftime("%d/%m/%y")
				Query.exec("INSERT INTO entregas VALUES('%s', %d, '%s')" %(self.solicitar.leCedula.text(), int(self.SERIAL), fecha))
				sol = Solicitud("Solicitud.pdf")
				dia = time.strftime("%d")
				dia = int(dia)
				dia = dia + 1
				fechaE = str(dia) + time.strftime("/%m/%y")
				sol.crear(self.solicitar.leNombre.text(),self.solicitar.leApellido.text(), self.solicitar.leCedula.text(), self.AUTOR, self.TITULO, self.COTA, self.EJEMPLAR, self.CARRERA, self.SEMESTRE, fecha, self.SERIAL, fechaE, self.solicitar.leSeccion.text(), self.solicitar.leTelefono.text())
				sol.guardar()
				QMessageBox.information(self, "Asignacion", "Libro asignado correctamente" , QMessageBox.Ok)
		else:
			QMessageBox.warning(self, "Error", "Campos vacios", QMessageBox.Ok)
		self.db.close()
		del Query

