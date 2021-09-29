#!/usr/bin/python

import sys, getopt

max = None

file = None

verbouse = False

def mostrarAyuda():
	textoAyuda = """This script create a new list of words with a specific size from a word list in a file.

Usage:acortarPalabras.py [OPTIONS]

OPTIONS:

-f <file path> ----------- File with the list of words to filter
-m <max length> ---------- Max size of the words to filter. May be bigger than 0
-v <verbouse> (OPTOINAL) - Enable verbouse mode
-h <help> (OPTIONAL) ----- Shows this help message
"""

	print(textoAyuda)


def cargarParametros():
	opt, argvs = getopt.getopt(sys.argv[1:], "f:m:vh")

	needHelp = False

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
		elif o == "-h":
			needHelp = True

	return needHelp


def filtrarPalabras():
	palabrasFiltradas = []
	global file
	global max
	if max is None or max == 0:
		raise IllegalArgumentException

	with open(file, 'r') as f:
		for i in f.readlines():
			if len(i) <= max:
				global verbouse
				if verbouse:
					print(i.strip())

				palabrasFiltradas.append(i)
	

	guardarFichero(palabrasFiltradas)

def guardarFichero(palabras):
	output = open("output.txt", 'wa')

	for i in palabras:
		output.write(i)

	output.close()

	print("Saved in output.txt")


try:
	if cargarParametros():
		mostrarAyuda()
	else:
		filtrarPalabras()
except Exception:
	mostrarAyuda()
