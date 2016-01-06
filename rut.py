import re
import string

class RutChile:
	def __init__(self, ver_rut):
		#self.verifica_rut(ver_rut)
		self.rut=""
		self.verifica_rut(ver_rut)		

	def verifica_rut(self,rut_raw):
		l = len(rut_raw)
		rut = ""
		pre_rut = "" 
		cuenta = 0

		if l >= 9:
			char_1 = rut_raw[2]
			char_2 = rut_raw[6]
			if char_1 == char_2 and char_1 == ".":
				pre_rut = re.sub(r"[\. - \-]",r"",rut_raw)
			else:
				pre_rut = rut_raw
			if pre_rut[0].isdigit():
				if int(pre_rut[0])>0:
					if pre_rut[len(pre_rut)-1] == "k" or pre_rut[len(pre_rut)-1].isdigit():
						#Verificar numeros desde 1 a n-1 que sean enteros
						inter_rut = pre_rut[1:len(pre_rut)-1]
						lir = len(inter_rut)
						for x  in range(lir):
							if inter_rut[x].isdigit():
								cuenta +=1
		
		if cuenta == 7:
			rut = pre_rut[0:len(pre_rut)-1]+"-"+pre_rut[len(pre_rut)-1]
			self.rut = rut

		elif cuenta != 7:
			print("El valor ingresado no es un RUT")


		return self.rut


