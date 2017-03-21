
index=0

class amigo:
	
	def __init__(self,Nombre,Apellido,Telefonos):
		
		self.Nombre=Nombre
		self.Apellido=Apellido 					#Constructor
		self.Telefonos=Telefonos
		
	def imprimir(self):
		print(self.Nombre+' '+self.Apellido)
		print(self.Telefonos)


