#!/usr/bin/python3

import sys
import getopt

ficheroAReemplazar = None

ficheroConReemplazo = None

palabraAReemplazar = None

output = None

verbouse = False

def mostrarAyuda():
	textoAyuda = """This script replaces a word from a wordlist file with each word in another wordlist file 
[USAGE]: ./reemplazarPalabras.py [OPTIONS]

OPTIONS:
-f <WORDLIST FILE> ------------ File with the words to replace
-F <ANOTHER WORDLIST FILE> ---- File with the words will replace the WORD in WORDLIST FILE
-w <WORD> --------------------- WORD present in WORDLIST FILE that will be replaced by each word in ANOTHER WORDLIST FILE
-o <OUTPUT> (OPTIONAL) ---------- Path to the output file
-v <VERBOUSE> (OPTIONAL) ------ Enable verbouse mode
-h <HELP> (OPTIONAL) ---------- Shows this help message
"""

	sys.exit(textoAyuda)


def cargarParametros():
	opt, argvs = getopt.getopt(sys.argv[1:], "f:F:w:o:vh")

	for o, a in opt:
		if o == "-f":
			global ficheroAReemplazar
			ficheroAReemplazar = a
		elif o == "-F":
			global ficheroConReemplazo
			ficheroConReemplazo = a
		elif o == "-w":
			global palabraAReemplazar
			palabraAReemplazar = a
		elif o == "-v":
			global verbouse
			verbouse = True
		elif o == "-o":
			global output
			output = a
		elif o == "-h":
			mostrarAyuda()


def reemplazar():
	listaNueva = []

	global ficheroAReemplazar
	global ficheroConReemplazo

	f = open(ficheroAReemplazar, 'r')

	for linea in f.readlines():
		with open(ficheroConReemplazo, 'r') as r:
			for reemplazo in r.readlines():
				global palabraAReemplazar
				nuevaLinea = linea.replace(palabraAReemplazar, reemplazo.strip()).strip()
				global verbouse
				if verbouse:
					print(nuevaLinea)

				listaNueva.append(nuevaLinea)

	f.close()

	global output
	if output is None:
		output = "output.txt"

	with open(output, 'a') as out:
		for linea in listaNueva:
			out.write(linea + "\n")

	print("Replaced %i lines" % len(listaNueva))
	print("Saved in %s" % output)


try:
	cargarParametros()
	reemplazar()
except Exception:
	mostrarAyuda()
