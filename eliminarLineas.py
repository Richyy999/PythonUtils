#!/usr/bin/python3

import sys, getopt

verbouse = False

file = None

palabra = None

output = None

ignoreCase = False

def mostrarAyuda():
	texto = """This script removes every line that contains a WORD from a FILE

Usage: ./eliminarPalabras.py [OPTIONS]

[OPTIONS]:

-f <FILE> ----------------------- Path of the file to read
-w <WORD> ----------------------- Word that the line must contain to remove it
-i <IGNORE CASE> (OPTIONAL) ----- Ignore case sensivity
-o <OUTPUT> (OPTIONAL) ---------- Path to the output file
-v <VERBOUSE> (OPTIONAL) -------- Enables vervouse mode
-h <HELP> (OPTIONAL) ------------ Shows this help message
"""

	sys.exit(texto)


def cargarParametros():
	opt, argvs = getopt.getopt(sys.argv[1:], "f:w:o:ivh")

	for o, a in opt:
		if o == "-f":
			global file
			file = a
		elif o == "-w":
			global word
			word = a
		elif o == "-o":
			global output
			output = a
		elif o == "-v":
			global verbouse
			verbouse = True
		elif o == "-i":
			global ignoreCase
			ignoreCase = True
		elif o == "-h":
			mostrarAyuda()


def eliminarLineas():
	lineasRestantes = []
	lineasTotales = 0
	global file
	with open(file, 'r') as f:
		for linea in f.readlines():
			global word
			global verbouse
			global ignoreCase
			linea = linea.strip()
			if ignoreCase:
				word = word.lower()
				linea = linea.lower()

			if not word in linea and len(linea) > 0:
				lineasRestantes.append(linea)
			elif word in linea and verbouse:
				print("Removed: " + linea)

			lineasTotales += 1

	global output
	if output is None:
		output = "output.txt"

	with open(output, 'w') as out:
		for linea in lineasRestantes:
			out.write(linea + "\n")

	if len(lineasRestantes) > 0:
		print("Removed %i of %i lines" %((lineasTotales - len(lineasRestantes)), lineasTotales))
	else:
		print("Removed 0 of %i" %lineasTotales)

	print("Saved in " + output)


try:
	cargarParametros()
	eliminarLineas()
except Exception:
	mostrarAyuda()
