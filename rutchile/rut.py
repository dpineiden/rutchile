import re
import string
import os, sys
#git clone https://github.com/dpineiden/number2name
from number2name_es.nombre_numero import Nombre_Numero

class RutChile:
	def __init__(self, ver_rut):
		#self.verifica_rut(ver_rut)
		self.rut=""
		self.verifica_rut(ver_rut)	
		print(self.rut)
		self.digito_verificador()
		self.rut_palabras()

	def verifica_rut(self,rut_raw):
		rut = ""
		pre_rut = "" 
		cuenta = 0

		rut_raw_separado = rut_raw.split("-")
		numero_raw =re.sub(r"[\.]",r"",rut_raw_separado[0])
		#print(numero_raw)
		l_raw = len(numero_raw)
		print("Digitos: "+str(l_raw))
		if l_raw == 6:
			char_1 = "."
			r_punto = 2
		elif l_raw == 7:
			r_punto = 1 	
		elif l_raw == 8:
			r_punto = 0

		l = len(numero_raw)

		if numero_raw.isdigit():
			if r_punto<2:
				char_1 = rut_raw[2-r_punto]
				char_2 = rut_raw[6-r_punto]
			else:
				char_1 = "."
				char_2 = rut_raw[3]

			if char_1 == char_2 and char_2 == ".":
				pre_rut = re.sub(r"[\. - \-]",r"",rut_raw)
			else:
				pre_rut = re.sub(r"[\-]",r"",rut_raw)
			if pre_rut[0].isdigit():
				if int(pre_rut[0])>0:
					if pre_rut[len(pre_rut)-1] == "k" or pre_rut[len(pre_rut)-1].isdigit():
						#Verificar numeros desde 1 a n-1 que sean enteros
						inter_rut = pre_rut[1:len(pre_rut)-1]
						lir = len(inter_rut)
						#print(pre_rut)
						for x  in range(lir):
							if inter_rut[x].isdigit():
								cuenta +=1
		#print("Pre rut "+pre_rut)
		pre_val = 7 - r_punto
		#print("Pre val "+str(pre_val))
		if cuenta == pre_val:
			rut = pre_rut[0:len(pre_rut)-1]+"-"+pre_rut[len(pre_rut)-1]
			self.rut = rut

		elif cuenta != pre_val:
			print("El valor ingresado no es un RUT")


		return self.rut

	def digito_verificador(self):
		rut_separado = self.rut.split("-")
		numero = rut_separado[0][::-1]
		digito = rut_separado[1]
		l = len(numero)
		valor = 0
		test = 0
		serie = [2,3,4,5,6,7]
		for x in range(l):
			if x<len(serie):
				i= x
			elif x>=len(serie):
				i = x - len(serie)
			valor += serie[i]*int(numero[x])	
			print("Serie: "+str(serie[i])+" valor: "+numero[x]+" valor: "+str(valor))	
		division = float(valor)/11
		resto = valor-int(division)*11
		diferencia = 11 - resto
		#print("Diferencia "+str(diferencia))
		if diferencia == 11:
			test = 0
		elif diferencia == 10:
			test = "k"
		elif diferencia<10:
			test = diferencia
		if digito.isdigit():
			if int(digito) == int(test):
				self.es_rut = True
				print(self.rut)
			else:
				print(str(valor)+":"+str(division)+":"+str(resto)+":"+str(diferencia)+":"+self.rut)
				self.es_rut = False
				print("El digito verificador no concuerda")
		elif digito == "k":
			self.es_rut = True
		else:
			self.es_rut = False
			print("El digito verificador no concuerda")

		return self.es_rut

	def rut_palabras(self):
		rut_separado = self.rut.split("-")
		numero = rut_separado[0]
		digito = rut_separado[1]
		Nombre_numero = Nombre_Numero(int(numero))
		if digito.isdigit():
			Nombre_digito = Nombre_Numero(int(digito)).Name_Total.lower()
		else:
			Nombre_digito = "ka"

		self.en_palabras = Nombre_numero.Name_Total + " raya " + Nombre_digito
