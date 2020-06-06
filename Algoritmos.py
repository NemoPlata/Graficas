import pandas as pd
from tkinter import *
import tkinter as tk
import webbrowser

pd.__version__

#ALGORITMO DE TIPO CLUSTERING
doc_aut = pd.read_csv("Autos.csv", header=0)
#Obtenemos a las personas que prefieren un audi tipo sedan
audSed = doc_aut[(doc_aut["make"] == "audi") & (doc_aut["style"] == "sedan")]

#Obtenemos a las persona que prefienre un chevrolet tipo sedan
cheSed = doc_aut[(doc_aut["make"] == "chevrolet") & (doc_aut["style"] == "sedan")]

if len(audSed) > len(cheSed) and len(audSed) > len(bmw) :
	audSed = doc_aut[(doc_aut["make"] == "audi") & (doc_aut["wb"] >= 100) & (doc_aut["fuel.sys"] == "mpfi")]
	print(audSed)

if len(cheSed) >  len(bmw) and len(cheSed) > len(audSed):
	cheSed = doc_aut[(doc_aut["make"] == "chevrolet") & (doc_aut["wb"] >= 100) & (doc_aut["fuel.sys"] == "mpfi")]
	print(cheSed)	


#DESPLEGAR PAGINA WEB
def desplegar_web():
	print('Desplegando')
	webbrowser.open('http://webexamen.herokuapp.com/')	
	print('Desplegado con exito')