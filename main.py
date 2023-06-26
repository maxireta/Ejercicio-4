from tkinter import *
from tkinter import ttk
import requests
from tkinter import Tk, Button, Entry
from tkinter import messagebox
from functools import partial

ventana = Tk()
ventana.title("Calculadora")

def calcular():
    expresion = entrada.get()
    try:
        resultado = eval(expresion)
        entrada.delete(0, "end")
        entrada.insert("end", str(resultado))
    except Exception:
        messagebox.showerror("Error", "Expresión inválida")

def agregar_caracter(caracter):
    entrada.insert("end", caracter)

def borrar():
    entrada.delete(0, "end")

def crear_boton(texto, fila, columna, comando):
    boton = Button(ventana, text=texto, command=comando, width=7, height=1)
  
    boton.grid(row=fila, column=columna)
    return boton

entrada = Entry(ventana, width=30)
entrada.grid(row=0, column=0, columnspan=4)

boton1 = crear_boton("1", 1, 0, partial(agregar_caracter, "1"))
boton2 = crear_boton("2", 1, 1, partial(agregar_caracter, "2"))
boton3 = crear_boton("3", 1, 2, partial(agregar_caracter, "3"))
boton4 = crear_boton("4", 2, 0, partial(agregar_caracter, "4"))
boton5 = crear_boton("5", 2, 1, partial(agregar_caracter, "5"))
boton6 = crear_boton("6", 2, 2, partial(agregar_caracter, "6"))
boton7 = crear_boton("7", 3, 0, partial(agregar_caracter, "7"))
boton8 = crear_boton("8", 3, 1, partial(agregar_caracter, "8"))
boton9 = crear_boton("9", 3, 2, partial(agregar_caracter, "9"))
boton0 = crear_boton("0", 4, 0, partial(agregar_caracter, "0"))

boton_igual = crear_boton("=", 5, 2, calcular)
boton_borrar = crear_boton("C", 6, 0, borrar)

boton_suma = crear_boton("+", 4, 1, partial(agregar_caracter, "+"))
boton_resta = crear_boton("-", 4, 2, partial(agregar_caracter, "-"))
boton_multiplicacion = crear_boton("*", 5, 0, partial(agregar_caracter, "*"))
boton_division = crear_boton("/", 5, 1, partial(agregar_caracter, "/"))

if __name__ == '__main__':
    ventana.mainloop()



