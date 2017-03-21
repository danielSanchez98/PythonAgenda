import amigos
import Agenda

def pedirContacto():
	nombreContacto=input("Nombre del nuevo Contacto: ")
	apellidoContacto=input("apellido del nuevo Contacto: ")
	aux=input("Conoce el numero telefonico Si/No")
	if(aux=="no"):
		nuevoamigo=amigos.amigo(nombreContacto,apellidoContacto,["SinNumero"])
	if(aux=="si"):
		num=input("Digite el numero telefonico")
		nuevoamigo=amigos.amigo(nombreContacto,apellidoContacto,[num])
	return nuevoamigo

nombre_Agenda=input("Ingrese el nombre del dueno de la Agenda: ")
apellidoAgenda=input("ingrese el apellido del dueno de la Agenda")
agen=Agenda.Agenda(nombre_Agenda,apellidoAgenda,[])






opc=""
while(opc!="SALIR" and opc!="salir" and opc!="5"):
	print("MENU:")
	print("1. Agregar Amigo")
	print("2. Listar Amigos")
	print("3. Agregar Numero")
	print("4. Eliminar Amigos")
	print("5. SALIR")
	opc=input("Ingrese la opcion que quiera")
	if(opc== "Agregar" or opc=="1"):
		agen.agregarAmigo(pedirContacto())
		
	if(opc=="listar" or opc=="2"):
		agen.listar()
	if(opc=="3"):
		ub=int(input("Ingrese el numero del amigo a modificar telefono: " ))
		phone=input("Ingrese el numero")
		agen.AgregarTelefono(ub,phone)
		
	if(opc=="Eliminar" or opc=="4"):
		indice=int(input("Ingrese el numero de amigo a eliminar: " ))
		agen.Eliminar(indice)

		


#mi_amigo=amigos.amigo("daniel","sanchez",[])
#mi_amigo.agregaTelefono(4554455454)
#mi_amigo.agregaTelefono(45549999994)
#mi_amigo.imprimir()

