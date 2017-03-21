import amigos


 

class Agenda:
	
	def __init__(self,nombreA,ApellidoA,amigo):
		
	    self.amigo=amigo
	    self.nombreA=nombreA
	    self.ApellidoA=ApellidoA

	def agregarAmigo(self, amigo):
		
		self.amigo.append(amigo)
		
		
	def listar(self):
		u=1
		for tamano in self.amigo:
			print("["+str(u)+"]"+" "+"Amigo: ")
			u=u+1
			print(tamano.imprimir())

	def Eliminar(self,ubicacion):
		ubicacion=ubicacion-1
		del self.amigo[ubicacion]
	def AgregarTelefono(self, ubicacion,phone):
		ubicacion=ubicacion-1
		if(self.amigo[ubicacion].Telefonos[0]=="SinNumero"):
			del self.amigo[ubicacion].Telefonos[0]
			self.amigo[ubicacion].Telefonos.append(phone)
		if(self.amigo[ubicacion].Telefonos[0]!="SinNumero"):
			self.amigo[ubicacion].Telefonos.append(phone)



		##self.amigo[0].Telefonos.append("5555555")
		
		
		


