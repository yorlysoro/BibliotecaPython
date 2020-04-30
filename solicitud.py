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
__name__ = "solicitud"

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer, Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#from os import startfile

class Solicitud(object):
	def __init__(self, nombre):
		self.nombre_archivo = nombre
		self.width, self.height = letter
		self.doc = SimpleDocTemplate(self.nombre_archivo, pagesize = letter)
		self.story=[]
		
	def crear(self,nombre=None, apellido=None, ci=None, autor_libro=None, titulo_libro=None, cota_libro=None, ejemplar_libro=None,carrera_libro=None,semestre_libro=None, fecha_retiro=None, serial_libro=None, fecha_entrega=None, seccion=None, telefono=None):
		logo = Image('unefa.jpg', width=100, height=100)
		rect = Image('rect.png', width=30, height=10)
		estilo = getSampleStyleSheet()
		tituloP = Paragraph('''<para align=center spaceb=2><b><font color=black size=12>Universidad Nacional Experimetal\n
		de la fuerza armada-UNEFA\n
		BIBLIOTECA MAESTRO SIMON RODRIGUEZ\n
		</font></b></para>''',
		estilo["BodyText"])
		TiposA = []
		for i in ("Libros", "Disquete", "CD", "Revista", "Informe", "Trabajo de Grado"):
			TiposA.append(Table( data = [[rect,i]]))
		tipos = Table ( data = [[TiposA[0], TiposA[1],TiposA[2]], [TiposA[3], TiposA[4], TiposA[5]]])
		titulo = Table( data = [[tituloP], [tipos]])
		lineas = 0;
		termina = False
		rTitulo = {}
		inicio = 0
		fin = 29
		while(termina == False):
			rTitulo[lineas] = titulo_libro[inicio: -1 if fin >= len(titulo_libro) else fin] +  '\n'
			inicio = fin
			fin = fin + 30
			if fin >= len(titulo_libro):
				rTitulo[lineas+1] = titulo_libro[inicio: -1]
				termina = True
			lineas = lineas + 1
		print(rTitulo.keys())
		rTitulo2 = ""
		for i in rTitulo.values():
			rTitulo2 = rTitulo2 + i
		print(rTitulo2)
		AutTituT = Table( data = [["Autor: %s" %(autor_libro)], ["Titulo: %s" %(rTitulo2)]],
		style = [('ALIGN', (0,0), (-1, -1), 'LEFT')]
		)
		cotaT = Table( data = [["Cota: %s" %(cota_libro), AutTituT]],
		style = [('ALIGN', (0,0), (0, 0), 'LEFT'),
		('VALIGN', (0,0),(0,0), 'TOP')])
		Sexo = Table( data = [["Sexo"],["F( )             M( )"]],
		style = [('ALIGN', (0,0), (-1, -1), 'CENTER')])
		EjT = Table( data = [["Ej: %s" %(ejemplar_libro), "Serial: %s" %(serial_libro),Sexo ]],
		style = [('ALIGN', (0,0), (-1, -1), 'CENTER')])
		NombreApellidoT = Table (data = [["Nombre y Apellido: %s %s %s" %(nombre, apellido, " "*(109-len(nombre)-len(apellido)))]])
		CarreCed = Table( data = [["Carrera: %s %s" %(carrera_libro, " "*(59-len(carrera_libro))), "CI:%s %s" %(ci, " "*(59-len(ci)))]])
		Fechas = Table( data = [["Fecha Prestamo: %s %s" %(fecha_retiro, " "*(41-len(fecha_retiro))), "Fecha Entrega: %s %s" %(fecha_entrega, " "*(41-len(fecha_entrega)))]])
		Renovaciones = Table(data = [["Renovacion 1:%s" %(" "*55), "Renovacion 2:%s" %(" "*55)]])
		rect2 = Image('rect.png', width=13, height=20)
		TiposA = []
		for i in ("Pre-Grado", "Post-Grado", "Docente", "Personal \nAdmi", "Visitante"):
			TiposA.append(Table( data = [[rect2,i]]))
		TiposU = Table(data = [[TiposA[0], TiposA[1], TiposA[2], TiposA[3], TiposA[4]]],
		style = [('ALIGN', (0,0), (0, 0), 'LEFT')])
		SecionTelef = Table(data = [["Seccion: %s %s" %(seccion, " "*(50-len(seccion))), "Telefono: %s %s" %(telefono, " "*(50-len(telefono)))]])
		Condiciones = Table(data = [["Condiciones Fisicas del Material: "]])
		Firmas = Table(data = [["Firma Usuario %s" %(" "*50), "Bibliotecario %s" %(" "*50)]])
		Nota = Table(data = [["Nota: Un dia de retraso en la entrega del libro amerita 3 DÍAS DE SUSPENCIÓN"]])
		Titulo = Table ( data = 
			[[logo,titulo]],
		style = [('ALIGN', (0,0), (0, 0), 'CENTER')]
			)
		Tablas = Table(data = [[Titulo], [cotaT], [EjT], [NombreApellidoT], [CarreCed], [Fechas], [Renovaciones], [TiposU],[SecionTelef],[Condiciones],[Firmas], [Nota]],
		style = [
		('GRID',(0,0),(-1,-1),0.5,colors.black),
		('ALGIN',(0,7),(0,0),'LEFT')])
		self.story.append(Spacer(0, 10))
		self.story.append(Tablas)

	def guardar(self):	
		self.doc.build(self.story)
		#startfile(self.nombre_archivo)
