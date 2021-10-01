#!/usr/bin/python

import sys, getopt

max = None

file = None

verbouse = False

output = None

def mostrarAyuda():
	textoAyuda = """This script create a new list of words with a specific size from a word list in a file.

Usage: ./acortarPalabras.py [OPTIONS]

OPTIONS:

-f <file path> ----------- File with the list of words to filter
-m <max length> ---------- Max size of the words to filter. Must be bigger than 0
-o <output> (OPTIONAL) --- Path to the output file
-v <verbouse> (OPTOINAL) - Enable verbouse mode
-h <help> (OPTIONAL) ----- Shows this help message
"""

	sys.exit(textoAyuda)


def cargarParametros():
	opt, argvs = getopt.getopt(sys.argv[1:], "f:m:o:vh")

	for o, a in opt:
		if o == "-f":
			global file
			file = a
		elif o == "-m":
			global max
			max = int(a)
		elif o == "-v":
			global verbouse
			verbouse = True
		elif o == "-o":
			global output
			output = a
		elif o == "-h":
			mostrarAyuda()


def filtrarPalabras():
	palabrasFiltradas = []
	palabrasTotales = 0
	global file
	global max
	if max is None or max == 0:
		raise IllegalArgumentException

	with open(file, 'r') as f:
		for i in f.readlines():
			if len(i) <= max and len(i) > 0:
				global verbouse
				if verbouse:
					print(i.strip())

				palabrasFiltradas.append(i.strip())

			palabrasTotales += 1
	
	print("Reduced from %i to %i words" %(palabrasTotales, len(palabrasFiltradas)))


	guardarFichero(palabrasFiltradas)


def guardarFichero(palabras):
	global output
	if output is None:
		output = "output.txt"

	with open(output, 'w') as out:
		for palabra in palabras:
			out.write(palabra + "\n")

	print("Saved in %s" % output)


try:
	cargarParametros()
	filtrarPalabras()
except Exception:
	mostrarAyuda()
