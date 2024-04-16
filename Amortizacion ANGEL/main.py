from flask import Flask, render_template, request, flash, redirect, url_for
import numpy as np
from matplotlib.figure import Figure
import base64
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calculo():
    #Formula para definir salario mensual
    salario = (request.form["salario"])
    salary = float(salario)
    ss = (salary * 0.236) + (salary * 0.055) + (salary * 0.035) + (salary * 0.006) + (salary * 0.002)

    salario_anual = (salary + ss) * 12
    total_anual = round(salario_anual, 2)

    #precio de un temi en el mercado
    temi = 8900
    total = round((total_anual - temi),2)

    #llamando a la funcion para graficar
    grafic = grafica(temi, total_anual)


    return render_template("index.html", sueldo_anual=total_anual, temi=temi, total=total, grafic=grafic)

#funcion de grafica
def grafica(temi,total_anual):

        #Pasamos los parametros de la grafica
        a = temi
        b = total_anual
        c = 1
        titulo = "COMPARACION GRAFICA"
        fig = Figure()
        ax = fig.subplots()
        ax.bar(c+1/2, a, label="TEMI", color="blue")
        ax.bar(c-1/2, b, label="Empleado", color="red")
        ax.legend()
        ax.set_ylabel('Euros')
        #ax.set_xlabel('Euros')
        ax.set_yticks(np.arange(0, 30001, 1000))

        fig.suptitle(titulo)

        #Creamos el archivo para luego decodificar y retornar
        buf = BytesIO()
        fig.savefig(buf, format="png")
        grafic = base64.b64encode(buf.getbuffer()).decode("ascii")
        return grafic

if __name__ == "__main__":
    app.run(debug=True)

