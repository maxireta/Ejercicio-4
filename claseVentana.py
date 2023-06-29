from claseImaginario import imaginario
from tkinter import *
from tkinter import ttk
from functools import partial
import re

class ventana:
    def __init__(self):
        self.__i = imaginario()
        self.__a = Tk()
        self.__a.geometry("300x190")
        self.__a.title("Calculadora")
        self.__num = StringVar()
        self.__resultado = StringVar()
        mainframe = LabelFrame(self.__a, width= 290, height=175, borderwidth= 2, relief="sunken").place(x=5, y=10)
        entry = ttk.Entry(mainframe, width= 30, textvariable= self.__num).place(x=101, y= 20)
        ttk.Button(mainframe, text= "1", width= 14, command= partial(self.agregar, self.__num, 1)).place(x=8, y=42)
        ttk.Button(mainframe, text= "2", width= 14, command=partial(self.agregar, self.__num, 2)).place(x= 101, y=42)
        ttk.Button(mainframe, text= "3", width= 14, command=partial(self.agregar, self.__num, 3)).place(x=194, y=42)
        ttk.Button(mainframe, text= "4", width= 14, command=partial(self.agregar, self.__num, 4)).place(x=8, y=67)
        ttk.Button(mainframe, text= "5", width= 14, command=partial(self.agregar, self.__num, 5)).place(x=101, y=67)
        ttk.Button(mainframe, text= "6", width= 14, command=partial(self.agregar, self.__num, 6)).place(x=194, y=67)
        ttk.Button(mainframe, text= "7", width= 14, command=partial(self.agregar, self.__num, 7)).place(x=8, y=92)
        ttk.Button(mainframe, text= "8", width= 14, command=partial(self.agregar, self.__num, 8)).place(x=101, y=92)
        ttk.Button(mainframe, text= "9", width= 14, command=partial(self.agregar, self.__num, 9)).place(x=194, y=92)
        ttk.Button(mainframe, text= "0", width= 14, command=partial(self.agregar, self.__num, 0)).place(x=8, y=117)
        ttk.Button(mainframe, text= "+", width= 14, command=partial(self.agregar, self.__num, "+")).place(x=101, y=117)
        ttk.Button(mainframe, text= "-", width= 14, command=partial(self.agregar, self.__num, "-")).place(x=194, y=117)
        ttk.Button(mainframe, text= "*", width= 14, command=partial(self.agregar, self.__num, "*")).place(x=8, y=142)
        ttk.Button(mainframe, text= "7", width= 14, command=partial(self.agregar, self.__num, "/")).place(x=101, y=142)
        ttk.Button(mainframe, text= "=", width= 14, command=self.calcular).place(x=194, y=142)
        ttk.Label(mainframe, textvariable= self.__resultado).place(x=8, y=20)
        self.__a.mainloop()

    def agregar(self, a, b):
        actual = a.get()
        cadena = actual + str(b)
        self.__num.set(cadena)
    def calcular(self):
        text = self.__num.get()
        if re.search('[a-zA-Z]', text):
            resultado = self.__i.calcular(text)
            self.__resultado.set(str(resultado))
        else:
            self.calcularenteros()
    def calcularenteros(self):
        expresion = self.__num.get()
        try:
            resultado = eval(expresion)
            self.__resultado.set(str(resultado))
        except:
            self.__resultado.set("Error en la expresión")