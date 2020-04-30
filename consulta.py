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
#  
__name__ = "consulta"

from PyQt5 import QtSql
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from vtncosulta import Ui_vtnConsulta
from solicitar import Solicitar

class Consulta(QMainWindow):
	def __init__(self, padre, db):
		QMainWindow.__init__(self, padre)
		self.consulta = Ui_vtnConsulta()
		self.consulta.setupUi(self)
		self.consulta.btnSalir.clicked.connect(lambda x: self.close() )
		self.consulta.btnBuscar.clicked.connect(self.__Buscar)
		self.consulta.btnSolicitar.clicked.connect(self.__Solicitud)
		self.db = db
		self.consulta.tablaConsulta.setColumnCount(7)
		self.consulta.tablaConsulta.setHorizontalHeaderLabels(['COTA', 'AUTOR', 'TITULO', 'EJEMPLAR', 'CARRERA', 'SEMESTRE', 'SERIAL'])
	def __Solicitud(self):
		row = self.consulta.tablaConsulta.currentRow()
		if row > -1:
			COTA = self.consulta.tablaConsulta.item(row, 0).text()
			AUTOR = self.consulta.tablaConsulta.item(row, 1).text()
			TITULO = self.consulta.tablaConsulta.item(row, 2).text()
			EJEMPLAR = self.consulta.tablaConsulta.item(row, 3).text()
			CARRERA = self.consulta.tablaConsulta.item(row, 4).text()
			SEMESTRE = self.consulta.tablaConsulta.item(row, 5).text()
			SERIAL = self.consulta.tablaConsulta.item(row, 6).text()
			solicitud = Solicitar(None,self.db,COTA, AUTOR, TITULO, EJEMPLAR, CARRERA, SEMESTRE, SERIAL)
			solicitud.show()
		else:
			QMessageBox.warning(self, "Error", "No ha seleccionado un libro", QMessageBox.Ok)
	def __Buscar(self):
		semestre = self.consulta.comboSemestre.currentText()
		Query = QtSql.QSqlQuery()
		self.db.open()
		if semestre == "Semestre 1":
			Query.exec("SELECT inventario.COTA, inventario.AUTOR, inventario.TITULO, inventario.EJEMPLAR, carreras.nombre, semestres.nombre, inventario.SERIAL FROM inventario, carreras, semestres WHERE inventario.codsemestre = '01S' AND inventario.codcarrera = carreras.codigo AND semestres.codigo = '01S'")
		elif semestre == "Semestre 3":
			Query.exec("SELECT inventario.COTA, inventario.AUTOR, inventario.TITULO, inventario.EJEMPLAR, carreras.nombre, semestres.nombre, inventario.SERIAL FROM inventario, carreras, semestres WHERE inventario.codsemestre = '03S' AND inventario.codcarrera = carreras.codigo AND semestres.codigo = '03S'")
		else:
			Query.exec("SELECT inventario.COTA, inventario.AUTOR, inventario.TITULO, inventario.EJEMPLAR, carreras.nombre, semestres.nombre, inventario.SERIAL FROM inventario, carreras, semestres WHERE inventario.codsemestre = '05S' AND inventario.codcarrera = carreras.codigo AND semestres.codigo = '05S'")
		row = 0
		self.consulta.tablaConsulta.clear()
		self.consulta.tablaConsulta.setRowCount(0)
		self.consulta.tablaConsulta.setColumnCount(0)
		self.consulta.tablaConsulta.setColumnCount(7)
		self.consulta.tablaConsulta.setHorizontalHeaderLabels(['COTA', 'AUTOR', 'TITULO', 'EJEMPLAR', 'CARRERA', 'SEMESTRE', 'SERIAL'])
		while Query.next():
			self.consulta.tablaConsulta.insertRow(row)
			COTA = QTableWidgetItem(str(Query.value(0)))
			AUTOR = QTableWidgetItem(str(Query.value(1)))
			TITULO = QTableWidgetItem(str(Query.value(2)))
			EJEMPLAR = QTableWidgetItem(str(Query.value(3)))
			CARRERA = QTableWidgetItem(str(Query.value(4)))
			SEMESTRE = QTableWidgetItem(str(Query.value(5)))
			SERIAL = QTableWidgetItem(str(Query.value(6)))
			 
			self.consulta.tablaConsulta.setItem(row, 0, COTA)
			self.consulta.tablaConsulta.setItem(row, 1, AUTOR)
			self.consulta.tablaConsulta.setItem(row, 2, TITULO)
			self.consulta.tablaConsulta.setItem(row, 3, EJEMPLAR)
			self.consulta.tablaConsulta.setItem(row, 4, CARRERA)
			self.consulta.tablaConsulta.setItem(row, 5, SEMESTRE)
			self.consulta.tablaConsulta.setItem(row, 6, SERIAL)
		row = row + 1
		del Query
		self.db.close()
