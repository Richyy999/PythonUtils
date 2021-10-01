#!/usr/bin/python3

import sys, getopt

diccionario = None

palabras = []

output = None

verbouse = False

def mostrarAyuda():
	texto = """This script insert a word in a wordlist
Usage: ./insertarDiccionario.py [OPTIONS]

[OPTIONS]:

-f <WORDLIST> ---------------- Path to the wordlist file
-w <WORD TO INSERT> ---------- Word to insert, can be called many times to insert multiple words
-o <OUTPUT> (OPTIONAL) ------- Path to the output file
-v <VERBOUSE> (OPTIONAL) ----- Enables verbouse mode
-h <HELP> (OPTIONAL) --------- Shows this help message
"""
	sys.exit(texto)


def cargarParametros():
	opt, argv = getopt.getopt(sys.argv[1:], "f:w:o:vh")

	for o, a in opt:
		if o == "-f":
			global diccionario
			diccionario = a
		elif o == "-w":
			global palabras
			palabras.append(a)
		elif o == "-o":
			global output
			output = a
		elif o == "-v":
			global verbouse
			verbouse = True
		elif o == "-h":
			mostrarAyuda()


def insertarEnDiccionario():
	global diccionario
	global palabras
	global verbouse
	global output

	if len(palabras) == 0:
		mostrarAyuda()

	palabrasInsertadas = 0

	content = []

	with open(diccionario, 'r') as d:
		for linea in d.readlines():
			content.append(linea.strip())

		for palabra in palabras:
			palabra = palabra.strip()
			if palabra in content and verbouse:
				print("%s is present in %s, skipping" % (palabra, diccionario))
			elif palabra not in content and verbouse:
				content.append(palabra)
				print("%s inserted" % palabra)
				palabrasInsertadas += 1
			elif palabra not in content:
				content.append(palabra)
				palabrasInsertadas += 1

	print("%i words inserted" % palabrasInsertadas)

	content = sorted(content, key=str.lower)

	if output is None:
		output = "output.txt"

	with open(output, 'w') as out:
		for palabra in content:
			out.write(palabra.strip() + "\n")

	print("Saved in %s" % output)


try:
	cargarParametros()
	insertarEnDiccionario()
except Exception:
	mostrarAyuda()
