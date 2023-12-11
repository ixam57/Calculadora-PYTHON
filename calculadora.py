import tkinter as tk

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def suma(self, num1, num2):
        self.resultado = num1 + num2
        return self.resultado

    def resta(self, num1, num2):
        self.resultado = num1 - num2
        return self.resultado

    def multiplicacion(self, num1, num2):
        self.resultado = num1 * num2
        return self.resultado

    def division(self, num1, num2):
        if num2 != 0:
            self.resultado = num1 / num2
            return self.resultado
        else:
            return "Error: División por cero"

class Interfaz:
    def __init__(self, ventana):
        # Inicializar la ventana con un título
        ventana.title("Calculadora")
        
        # Inicializar la calculadora
        self.calc = Calculadora()
        
        # Crear los elementos de la interfaz
        self.num1 = tk.Entry(ventana)
        self.num1.pack()
        
        self.num2 = tk.Entry(ventana)
        self.num2.pack()
        
        self.boton_suma = tk.Button(ventana, text="+", command=self.sumar)
        self.boton_suma.pack()

        self.boton_resta = tk.Button(ventana, text="-", command=self.restar)
        self.boton_resta.pack()

        self.boton_multiplicacion = tk.Button(ventana, text="x", command=self.multiplicar)
        self.boton_multiplicacion.pack()

        self.boton_division = tk.Button(ventana, text=" / ", command=self.dividir)
        self.boton_division.pack()
        
        self.resultado = tk.Label(ventana, text="")
        self.resultado.pack()
    
    def sumar(self):
        res = self.calc.suma(float(self.num1.get()), float(self.num2.get()))
        self.resultado.config(text=str(res))

    def restar(self):
        res = self.calc.resta(float(self.num1.get()), float(self.num2.get()))
        self.resultado.config(text=str(res))

    def multiplicar(self):
        res = self.calc.multiplicacion(float(self.num1.get()), float(self.num2.get()))
        self.resultado.config(text=str(res))

    def dividir(self):
        res = self.calc.division(float(self.num1.get()), float(self.num2.get()))
        self.resultado.config(text=str(res))
        
# Crear una instancia de la interfaz y arrancar el bucle de la aplicación
root = tk.Tk()
Interfaz(root)
root.mainloop()
