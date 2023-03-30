import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
import math

class MyWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title="Hola W")
		
		"""self.cajaPrincipal = Gtk.Box(spacing = 60)
		self.cajaPrincipal.set_homogeneous(False)
		"""
		"""self.add(self.cajaPrincipal)"""
		"""
		self.cajaSup = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
		self.cajaInf = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
		
		self.cajaPrincipal.pack_start(self.cajaSup, True, True, 0)
		self.cajaPrincipal.pack_start(self.cajaInf, True, True, 0)
		"""
		gri = Gtk.Grid()
		
		self.desbastadoX = 0
		self.desbastadoY = 0
		self.desbastadoZ = 0
		"""label = Gtk.Label()
		label.set_text("Solo para MEDIO CAÑO ")
		#self.cajaSup.pack_start(label, True, True, 0)"""
		label = Gtk.Label()
		label.set_text("Ancho (mm) ")
		gri.attach(label, 1, 1, 1, 1)
		#self.cajaSup.pack_start(label, True, True, 0)
		
		label = Gtk.Label()
		label.set_text("Largo (mm) ")
		gri.attach(label, 1, 2, 1, 1)
		#self.cajaSup.pack_start(label, True, True, 0)
		
		label = Gtk.Label()
		label.set_text("Profundidad (mm) ")
		gri.attach(label, 1, 3, 1, 1)
		#self.cajaSup.pack_start(label, True, True, 0)
		
		label = Gtk.Label()
		label.set_text("Altura de la pieza ")
		gri.attach(label, 1, 4, 1, 1)
		#self.cajaSup.pack_start(label, True, True, 0)
		
		label = Gtk.Label()
		label.set_text("despeje")
		gri.attach(label, 1, 5, 1, 1)
		#self.cajaSup.pack_start(label, True, True, 0)
		
		label = Gtk.Label()
		label.set_text("Diametro de Herram ")
		gri.attach(label, 1, 6, 1, 1)
		"""label = Gtk.Label()
		label.set_text("Absoluta de Z ")
		self.cajaSup.pack_start(label, True, True, 0)"""
		
		#label = Gtk.Label()
		#label.set_text("Distancia Z de Inicio ")
		#self.cajaSup.pack_start(label, True, True, 0)
		
		
		self.bCalcular = Gtk.Button(label="Calcular")
		self.bCalcular.connect("clicked", self.calcular)
		gri.attach(self.bCalcular, 1, 9, 1, 1)
		#self.cajaSup.pack_start(self.bCalcular, True, True, 0)
		
		
		#label = Gtk.Label()
		#label.set_text(" mm ")
		#self.cajaInf.pack_start(label, True, True, 0)
		
		
		self.ancho = Gtk.Entry()
		gri.attach(self.ancho, 2, 1, 1, 1)
		#self.cajaInf.pack_start(self.ancho, True, True, 0)
		
		self.largo = Gtk.Entry()
		gri.attach(self.largo, 2, 2, 1, 1)
		#self.cajaInf.pack_start(self.largo, True, True, 0)
		
		self.prof = Gtk.Entry()
		gri.attach(self.prof, 2, 3, 1, 1)
		#self.cajaInf.pack_start(self.prof, True, True, 0)
		
		#label = Gtk.Label()
		#label.set_text("La Herramienta ubicada en 0, 0, 0 ")
		#self.cajaInf.pack_start(label, True, True, 0)
		
		self.altPieza = Gtk.Entry()
		gri.attach(self.altPieza, 2, 4, 1, 1)
		#self.cajaInf.pack_start(self.absX, True, True, 0)
		
		self.despeje = Gtk.Entry()
		gri.attach(self.despeje, 2, 5, 1, 1)
		#self.cajaInf.pack_start(self.absY, True, True, 0)
		
		self.diamH = Gtk.Entry()
		gri.attach(self.diamH, 2, 6, 1, 1)
		
		self.bCerrar = Gtk.Button(label="Cerrar")
		self.bCerrar.connect("clicked", self.cerrar)
		gri.attach(self.bCerrar, 2, 9, 1, 1)
		#self.cajaInf.pack_start(self.bCerrar, True, True, 0)
		
		scrolledwindow = Gtk.ScrolledWindow()
		scrolledwindow.set_hexpand(True)
		scrolledwindow.set_vexpand(True)
		##########################################
		gri.attach(scrolledwindow, 1, 10, 2, 3)
		
		#self.cajaSup.pack_start(scrolledwindow, True, True, 0)
		self.textview = Gtk.TextView()
		self.textbuffer = self.textview.get_buffer()
		self.textbuffer.set_text("This is some text inside of a Gtk.TextView. "
            + "Select text and click one of the buttons 'bold', 'italic', "
            + "or 'underline' to modify the text accordingly.")
		scrolledwindow.add(self.textview)

		self.tag_bold = self.textbuffer.create_tag("bold", weight=Pango.Weight.BOLD)
		self.tag_italic = self.textbuffer.create_tag("italic", style=Pango.Style.ITALIC)
		self.tag_underline = self.textbuffer.create_tag("underline", underline=Pango.Underline.SINGLE)
		self.tag_found = self.textbuffer.create_tag("found", background="yellow")
		
		self.add(gri) #self.cajaPrincipal)
		
		self.ancho.set_text("8")
		self.largo.set_text("70")
		self.prof.set_text("4")
		self.altPieza.set_text("12")
		self.diamH.set_text("3")
		self.despeje.set_text("9")
		self.calcular(self,0.2)
		
		#self.anchoDeCapa()
		
	"""IMPLEMENTAR VELOCIDAD DE TRABAJO
	eliminar los absolutos
	agregar la altura total de la pieza
	agregar cuanto baja Z(cambiar 3; 3.2 y 0.2 y el valor de debvaste
	agregar la distancia del punto de inicio(0,0,0) al comienzo del ranurado
	agregar notas sobre la UBICACION de la pieza
	"""
	def calcular(self, widget, vd=0.2):
		print("Calcular...")

		##########################################################################
		#voy a hacer una ranura del ancho de la herramienta en direccion al eje Y
		##########################################################################
		#ubicacion:
		# el medio del corte es = (al ancho de la ranura / 2) + la distancia de posicion de la misma
		despeje = float(9); # Y 9 es donde empieza la ranura
		ancho = float(self.ancho.get_text())
		largo = float(self.largo.get_text())
		altPieza = float(self.altPieza.get_text())
		prof = float(self.prof.get_text())
		ubicX = float(round(despeje + (ancho/2), 2))
		ubicY = 0
		ubicZ = float(altPieza + 3) # +3 para que no toque la pieza
		velocCorte = 150
		porcCorte = 0.2 # mm de desbaste
		capas = int(prof / porcCorte)
		diamH = float(self.diamH.get_text())
		#Anotamos la pos:
		self.textbuffer.set_text("G0" + " F" + str(velocCorte) + "\n" )
		
		## unos huecos de referencia
		
		"""pendiente los huecos
		huecoX1 =  round(float((despeje) / 2) + 1.5, 2)
		huecoY1 = huecoX1 
		huecoY2 = largo - huecoX1 
		huecoX2 = despeje + ancho + huecoX1
		self.textbuffer.insert_at_cursor("Z15\n" )
		self.textbuffer.insert_at_cursor("X" + str(round(huecoX1, 2)) + "Y" + str(round(huecoY1))  + "\n" ) #6.6
		self.textbuffer.insert_at_cursor("Z9\n" )
		self.textbuffer.insert_at_cursor("Z15\n" )
		self.textbuffer.insert_at_cursor("Y" + str(round(huecoY2))  + "\n" ) #6.64
		self.textbuffer.insert_at_cursor("Z9\n" )
		self.textbuffer.insert_at_cursor("Z15\n" )
		self.textbuffer.insert_at_cursor(";fin\n" )
		self.textbuffer.insert_at_cursor("X" + str(round(huecoX2))  + "\n" ) 
		self.textbuffer.insert_at_cursor(";fin\n" )
		self.textbuffer.insert_at_cursor("Z9\n" )
		self.textbuffer.insert_at_cursor("Z15\n" )
		self.textbuffer.insert_at_cursor("Y" + str(round(huecoY1, 2)) + "\n" )
		self.textbuffer.insert_at_cursor(";fin\n" )"""
		### ranura
		self.textbuffer.insert_at_cursor("X" + str(round(ubicX, 2)) + "\n" )
		self.textbuffer.insert_at_cursor("Y000\n") ##\n ;vuelta" + str(fila) +"\n\n"  )
		
		
		#ahora el ranurado
		self.textbuffer.insert_at_cursor("Z" + str(ubicZ) + "\n" )
		self.textbuffer.insert_at_cursor("X" + str(ubicX) + " Y" + str(ubicY) + "\n" )
		#empezamos la ranura
		ubicZ = ubicZ - 3 - porcCorte
		self.textbuffer.insert_at_cursor("Z" + str(ubicZ) + "\n" )
		
		""" capas eje Z
		    filas eje X
		"""
		
		#avanza / retros
		#self.textbuffer.insert_at_cursor(";Comienzo ranurado\n" )
		for capa in range(int(capas/2)):
			avY = largo + diamH
			self.textbuffer.insert_at_cursor("Y" + str(round(avY, 2)) + "\n" )
			ubicZ -= porcCorte
			self.textbuffer.insert_at_cursor("Z" + str(round(ubicZ, 2)) + "\n" )
			self.textbuffer.insert_at_cursor("Y000\n" )
			ubicZ -= porcCorte
			self.textbuffer.insert_at_cursor("Z" + str(round(ubicZ, 2)) + "\n" )
			
		
		#self.textbuffer.insert_at_cursor(";Fin de la caladura -- corte Lat\n" )
		#ahora las paredes
		##Ubicacion
		ubicZ = altPieza - porcCorte
		#self.textbuffer.insert_at_cursor(";Ubicacion\n" )
		self.textbuffer.insert_at_cursor("Z" + str(round(ubicZ, 2)) + "\n" ) # linea descolgada pero SIRVE
		#self.textbuffer.insert_at_cursor("Y000\n" )
		#corte Y73 corta pared der ////  Y000 corta pared izq
		##################################################################################################
		## Filas a la derecha = 8 ancho(diametro) del corte / 2 - 1.5(caladura anterior(diam de la herram) /2
		## las capas se van achicando(grandes arriba-chicas abajo) y las filas se van eliminando(de abajo pa riba
		##################################################################################################
		##################################################################################################
		## para la distancia de cada capa(para que la caladura sea en semiCirculo)....
		## #primer capa de 0.2 de prof la dist es de 8...
		## #segund capa de 0.2 de prof la dist es de 8... 
		##################################################################################################
		##
		
		
		#print("f in ", filasInicial)
		medioX = float(round(despeje + (ancho/2), 2))
		dicc = self.evalCapa(ancho)  #info del largo de las capas
		print("ddiiiccc", dicc)
		#dicc = dato[1]   #info del largo de las capas
		#self.textbuffer.insert_at_cursor("\n;comienza desbaste de capas y filas\n" )
		for capa in dicc:
			# las FILAS varian de acuerdo al ancho de capa...
			#dicc = self.evalCapa(ancho)
			#dicc = dato[1]
			
			filas = int(((float(dicc.get(capa)) - diamH) / porcCorte))
			
				
			print("-------------- " , capa, dicc.get(capa), "cant de pasadas", filas)
			
			nuevaPorc = porcCorte #reinicio la nuevaPorc
			#ubicacion para iniciar cada capa
			ubicX = medioX
			#self.textbuffer.insert_at_cursor(";Se ubica en la capa " + str(capa) + "\n" )	
			self.textbuffer.insert_at_cursor("X" + str(round(ubicX, 2)) + "\n" )
			self.textbuffer.insert_at_cursor("Y000\n" )
			#self.textbuffer.insert_at_cursor(";desbaste de capa " + str(capa) + "\n" )	
			if filas > 0 :
				for fila in range(filas):
					#self.textbuffer.insert_at_cursor(";desbasta la fila " + str(fila) + "de " + str(filas) + "\n" )	
					ubicX = medioX + nuevaPorc
					ubicY = largo + diamH
					self.textbuffer.insert_at_cursor("X" + str(round(ubicX, 2)) + "\n" )
					self.textbuffer.insert_at_cursor("Y" + str(round(ubicY, 2)) + "\n" )
					#pcXi = pcXi + porcCorte
					
					
					ubicX = medioX - nuevaPorc
					self.textbuffer.insert_at_cursor("X" + str(round(ubicX, 2)) + "\n" )
					self.textbuffer.insert_at_cursor("Y000\n") ##\n ;vuelta" + str(fila) +"\n\n"  )
					
					nuevaPorc = nuevaPorc + porcCorte
					#self.textbuffer.insert_at_cursor(";fin de la fila " + str(fila) + "de " + str(filas) + "\n" )
			else:
				pass
			#self.textbuffer.insert_at_cursor(";fin de la capa ------------------ " + str(capa) + "de " + str(capas) + "\n" )	
			ubicZ -= porcCorte
			self.textbuffer.insert_at_cursor("Z" + str(round(ubicZ, 2)) + "\n" )
			
			
			ancho = ancho - nuevaPorc
			#print("achor: ", str(ancho), " np ", nuevaPorc)
			
			#self.anchoDeCapa()	
		## unos huecos de referencia
				
		self.crear()
	def evalCapa(self, ancho):
		print("\n evalCapa")
		
		#voy a hacer un diccionario con el nombre de la capa y el valor del ancho
		prof = float(self.prof.get_text())
		porcCorte = 0.2 # mm de desbaste
		capas = int(prof / porcCorte)
		radio = float(self.ancho.get_text()) / 2
		alt = prof
		diccAnchos = {}
		for capa in range(capas):
			aacos = 1 - (alt / radio)
			ang= 2 * math.degrees(math.acos(aacos))
			
			nuevoAncho = ang / 2
			nuevoAncho = math.sin(math.radians(nuevoAncho))
			nuevoAncho = 2 * radio * nuevoAncho
			#print("ang ", ang, "nuevoAncho", nuevoAncho)
			alt -= 0.2
			if nuevoAncho >= float(self.diamH.get_text()):
				textoCapa = str("capa" + str(capa))
				diccAnchos[textoCapa] = round(nuevoAncho, 2)
				#datos([capa, str(nuevoAncho), ])
			else:
				diccAnchos[textoCapa] = 1
		#print("dicc anchos:", diccAnchos)
		return diccAnchos
		
		"""
		capa1 = 8
		capa2 = 7.8
		capa3 = 7.6
		"""
			
		
		
		### MOCASO no jay forma de que me de los datos por capa
		"""calcular el angulo del centro del medio caño a la cuerda
		
		ang = 2*acos(1-(h/R)) h= altura R = radio
		
		el largo de capa = 2*R*sin((ang/2))  R = radio ang= angulo
		"""
		"""#print(math.degrees(math.acos(0.5)))
		radio = float(self.ancho.get_text()) / 2
		#print("radio", radio)
		# 1-(h/R):
		aacos = 1 - (float(self.prof.get_text()) / radio)
		#print("acos", aacos)
		#acos(...):
		degr = math.degrees(aacos)
		#print("degrr", degr)
		#print(math.degrees(math.acos(0.0)))
		ang= 2 * math.degrees(math.acos(degr))
		
		nuevoAncho = ang / 2
		#print("nuevoAncho", nuevoAncho)
		nuevoAncho = math.sin(math.radians(nuevoAncho))
		#print("nuevoAncho, radio", nuevoAncho, radio)
		nuevoAncho = 2 * radio * nuevoAncho
		#print(nuevoAncho)
		print("ang ", ang, "nuevoAncho", nuevoAncho)
		filas = int(((ancho - diamH) / 2) / porcCorte) # filas de cada lado
		#if nuevoAncho <= (nuevoAncho - 
		
		return nuevoAncho, filas"""
	def crear(self):
		ultimaLinea = int(self.textbuffer.get_line_count())
		f = open( "/home/ussd/gcodes-softw/Mis Gcodes/gCodeCreado2.gcode", "w")
		print(ultimaLinea)
		#for i un range(ultimaLinea):
		pIter = self.textbuffer.get_start_iter()
		fIter = self.textbuffer.get_end_iter()
		codigo = self.textbuffer.get_text(pIter, fIter, True)   
		f.write(codigo)	
		f.close()
		
	def corteYmas(self, absY, vd):
		#determino la distancia de desbaste
		dFd = round(float(self.largo.get_text()) - self.desbastadoY, 2) ## Distancia que Falta Desbastar #vd*2 DesvX + desvX
		absY = (dFd + absY) - vd ##tiene que dar 70.9
		self.desbastadoY += vd
		return absY
	def corteXmas(self, absX, vd, distX):
		#determino la distancia de desbaste
		dFd = round(float(self.ancho.get_text()) - self.desbastadoX, 2) ## Distancia que Falta Desbastar #vd*2 DesvX + desvX
		absX = (distX + float(self.ancho.get_text())) - ( (float(self.diamH.get_text()) / 2) - vd ) - self.desbastadoX
		self.desbastadoX += vd
		return absX
	def corteYmenos(self, absY, vd):
		#determino la distancia de desbaste
		dFd = round(float(self.largo.get_text()) - self.desbastadoY, 2) ## Distancia que Falta Desbastar #vd*2 DesvX + desvX
		absY = (absY - dFd) + vd ##tiene que dar 70.9
		self.desbastadoY += vd
		return absY	
	def corteXmenos(self, absX, vd, distX):
		#determino la distancia de desbaste
		dFd = round(float(self.ancho.get_text()) - self.desbastadoX, 2) ## Distancia que Falta Desbastar #vd*2 DesvX + desvX
		absX = distX + ( (float(self.diamH.get_text()) / 2) - vd ) + self.desbastadoX
		self.desbastadoX += vd
		return absX
		
				
	def cerrar(self, widget):
		print("Chau... culiau")
		Gtk.main_quit()
		
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()	
"""

Y70.9
X37.2
Y2.1
X11.1
	
win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()"""
