from flask import Flask, render_template,request,redirect,url_for
from base_de_datos import db
from models.models import Cliente, Producto, Costes_producto




# --------------- APP FLASK -------------------
app = Flask(__name__)

# -------------------------------------------- Home ------------------------------------------------------------------

# ----Home  Route----
@app.route("/")


def index():

    # ----Return
    return render_template("/index/index.html")



# ----------------------------------------- Clientes ---------------------------------------------------------------

# ----Agregar Cliente Home----
@app.route("/clientes/agregar_cliente")

def agregar_cliente():

    # ----Return
    return render_template("/clientes/agregar_cliente.html")

#------ Crear Clientes -------
@app.route("/crear_cliente", methods = ["post"])
def crear_cliente():

    '''Se crean los clientes en base a lo que se introdujo en los campos pedidos, con sus respectivos nombres'''

    cliente = Cliente(nombre_cliente=request.form['nombre_cliente'],
                          CIF_cliente=request.form['CIF_cliente'],
                          direccion_cliente=request.form['direccion_cliente'],
                          codigo_postal_cliente=request.form['codigo_postal_cliente'],
                          poblacion_cliente=request.form['poblacion_cliente'],
                          provincia_cliente=request.form['provincia_cliente'],
                          pais_cliente=request.form['pais_cliente'],
                          telefono_cliente=request.form['telefono_cliente'],
                          movil_cliente=request.form['movil_cliente'],
                          email_cliente=request.form['email_cliente'],
                          web_cliente=request.form['web_cliente'],
                          comentario_cliente=request.form['comentario_cliente'])

    db.session.add(cliente)
    db.session.commit()
    db.session.close()

    #------- Return
    return redirect(url_for ("agregar_cliente"))


#-------------Lista Clientes --------------
@app.route("/clientes/lista_clientes")
def lista_clientes():

    '''Se realiza un Query de todos los clientes y se los ordena alfabéticamente'''
    todos_clientes = db.session.query(Cliente).order_by(Cliente.nombre_cliente).all()

    #----- Return (se envía la información para ser leída por HTML)
    return render_template("/clientes/lista_clientes.html", lista_clientes = todos_clientes)



#------------------Eliminar Clientes -------------

@app.route("/eliminar_cliente/<id>")
def eliminar_cliente(id):

    '''Se realiza un Query de un único cliente filtrandolo por el ID para ELIMINARLO'''
    cliente = db.session.query(Cliente).filter_by(id=int(id)).delete()


    db.session.commit()
    db.session.close()

    #---- Return
    return redirect(url_for ("lista_clientes"))

#------------------Ficha Cliente ----------------


@app.route("/clientes/ficha_cliente/<id>")
def ficha_cliente(id):

    '''Se realiza un Query de un único cliente filtrandolo por el ID'''
    cliente = db.session.query(Cliente).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    #----- Return (se envía la información para ser leída por HTML)
    return render_template("/clientes/ficha_cliente.html", ficha_cliente = cliente)


#------------------Edición Ficha Cliente -------------


#----------HOME
@app.route("/clientes/edicion_ficha_cliente_home/<id>")
def edicion_ficha_cliente_home(id):

    '''Se realiza un Query de un único cliente filtrandolo por el ID'''
    cliente = db.session.query(Cliente).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    #----- Return (se envía la información para ser leída por HTML)
    return render_template("/clientes/edicion_ficha_cliente_home.html", ficha_cliente = cliente)


#---------def Edición ficha cliente
@app.route("/edicion_ficha_cliente/<id>",methods = ["post"])
def edicion_ficha_cliente(id):

    '''Se realiza un Query de un único cliente filtrandolo por el ID, para luego poder modificar la información
    de los campos anteriormente guardados'''

    cliente = db.session.query(Cliente).filter_by(id=int(id)).first()
    cliente.nombre_cliente = request.form['nombre_cliente']
    cliente.CIF_cliente = request.form['CIF_cliente']
    cliente.direccion_cliente = request.form['direccion_cliente']
    cliente.codigo_postal_cliente = request.form['codigo_postal_cliente']
    cliente.poblacion_cliente = request.form['poblacion_cliente']
    cliente.provincia_cliente = request.form['provincia_cliente']
    cliente.pais_cliente = request.form['pais_cliente']
    cliente.telefono_cliente = request.form['telefono_cliente']
    cliente.movil_cliente = request.form['movil_cliente']
    cliente.email_cliente = request.form['email_cliente']
    cliente.web_cliente = request.form['web_cliente']
    cliente.comentario_cliente = request.form['comentario_cliente']

    db.session.commit()
    db.session.close()

    '''Luego de que se hayan modificado y guardado los cambios de la información nueva, se hace nuevamente
    un QUERY de ese mismo cliente filtrado por un ID para mostra su ficha YA modificada con la nueva información'''

    aux= db.session.query(Cliente).filter_by(id=int(id))

    db.session.commit()
    db.session.close()

    # ----- Return (se envía la información para ser leída por HTML)
    return render_template("/clientes/ficha_cliente.html", ficha_cliente = aux)



# ----------------------------------------- Productos ---------------------------------------------------------------

# ----Agregar Producto Home----
@app.route("/productos/agregar_producto")

# ----Home agregar Producto----
def agregar_producto():

    # ----Return
    return render_template("/productos/agregar_producto.html")

#------ Crear Producto -------
@app.route("/crear_producto", methods = ["post"])
def crear_producto():

    '''Se crean los productos en base a lo que se introdujo en los campos pedidos, con sus respectivos nombres'''

    producto = Producto(nombre_producto=request.form['nombre_producto'],
                          Numero_de_serie_producto=request.form['Numero_de_serie_producto'],
                          sistema_operativo_producto=request.form['sistema_operativo_producto'],
                          color_producto=request.form['color_producto'],
                          tamanio_producto=request.form['tamanio_producto'],
                          peso_producto=request.form['peso_producto'],
                          pantalla_producto=request.form['pantalla_producto'],
                          microfonos_producto=request.form['microfonos_producto'],
                          audio_producto=request.form['audio_producto'],
                          camaras_producto=request.form['camaras_producto'],
                          cpu_producto=request.form['cpu_producto'],
                          alimentacion_producto=request.form['alimentacion_producto'],
                          velocidad_producto=request.form['velocidad_producto'],
                          puertos_producto=request.form['puertos_producto'],
                          descripcion_producto=request.form['descripcion_producto'])

    db.session.add(producto)
    db.session.commit()
    db.session.close()
    return redirect(url_for ("agregar_producto"))


#-------------Lista Productos --------------
@app.route("/productos/lista_productos")
def lista_productos():

    '''Se realiza un Query de todos los productos y se los ordena alfabéticamente'''

    todos_productos = db.session.query(Producto).order_by(Producto.nombre_producto).all()

    # ----- Return (se envía la información para ser leída por HTML)
    return render_template("/productos/lista_productos.html", lista_productos = todos_productos)



#------------------Eliminar Productos -------------

@app.route("/eliminar_producto/<id>")
def eliminar_producto(id):

    '''Se realiza un Query de un único producto filtrandolo por el ID para ELIMINARLO'''

    producto = db.session.query(Producto).filter_by(id=int(id)).delete()


    db.session.commit()
    db.session.close()

    # ---- Return
    return redirect(url_for ("lista_productos"))

#------------------Ficha Producto -------------


@app.route("/productos/ficha_producto/<id>")
def ficha_producto(id):

    '''Se realiza un Query de un único producto filtrandolo por el ID'''

    producto = db.session.query(Producto).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    # ----- Return (se envía la información para ser leída por HTML)
    return render_template("/productos/ficha_producto.html", ficha_producto = producto)


#------------------Edición Ficha Producto -------------


#----------HOME ------------
@app.route("/producto/edicion_ficha_producto_home/<id>")
def edicion_ficha_producto_home(id):

    '''Se realiza un Query de un único producto filtrandolo por el ID'''

    producto = db.session.query(Producto).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    # ----- Return (se envía la información para ser leída por HTML)
    return render_template("/productos/edicion_ficha_productos_home.html", ficha_producto = producto)


#---------def Edición ficha producto
@app.route("/edicion_ficha_producto/<id>",methods = ["post"])
def edicion_ficha_producto(id):

    '''Se realiza un Query de un único producto filtrandolo por el ID, para luego poder modificar la información
        de los campos anteriormente guardados'''

    producto = db.session.query(Producto).filter_by(id=int(id)).first()
    producto.nombre_producto = request.form['nombre_producto']
    producto.Numero_de_serie_producto = request.form['Numero_de_serie_producto']
    producto.sistema_operativo_producto = request.form['sistema_operativo_producto']
    producto.color_producto = request.form['color_producto']
    producto.tamanio_producto = request.form['tamanio_producto']
    producto.peso_producto = request.form['peso_producto']
    producto.pantalla_producto = request.form['pantalla_producto']
    producto.microfonos_producto = request.form['microfonos_producto']
    producto.audio_producto = request.form['audio_producto']
    producto.camaras_producto = request.form['camaras_producto']
    producto.cpu_producto = request.form['cpu_producto']
    producto.alimentacion_producto = request.form['alimentacion_producto']
    producto.velocidad_producto = request.form['velocidad_producto']
    producto.puertos_producto = request.form['puertos_producto']
    producto.comentario_cliente = request.form['comentario_cliente']

    db.session.commit()
    db.session.close()

    '''Luego de que se hayan modificado y guardado los cambios de la información nueva, se hace nuevamente
    un QUERY de ese mismo producto filtrado por un ID para mostra su ficha YA modificada con la nueva información'''

    aux= db.session.query(Producto).filter_by(id=int(id))

    db.session.commit()
    db.session.close()

    # ----- Return (se envía la información para ser leída por HTML)
    return render_template("/productos/ficha_producto.html", ficha_producto = aux)





# ----------------------------------------- COSTES Productos --------------------------------------------------------

# ----Agregar Costes Producto Home----
@app.route("/costes/agregar_costes_producto")

# ----Home agregar COSTES Producto----
def agregar_costes_producto():

    #Productos
    todos_productos =db.session.query(Producto).order_by(Producto.nombre_producto).all()

    # ----Return
    return render_template("/costes/agregar_costes_producto.html",todos_productos = todos_productos)

#------ Crear Costes Producto -------
@app.route("/crear_costes_producto", methods = ["post"])
def crear_costes_producto():


    costes_producto = Costes_producto(nombre_producto=request.form['nombre_producto'],
                          coste_inicial_producto=request.form['coste_inicial_producto'],
                          coste_mantenimiento_producto=request.form['coste_mantenimiento_producto'],
                          coste_carga_producto=request.form['coste_carga_producto'])

    db.session.add(costes_producto)
    db.session.commit()
    db.session.close()
    return redirect(url_for ("agregar_costes_producto"))


#-------------Lista Productos --------------
@app.route("/costes/lista_costes_productos")
def lista_costes_productos():
    todos_costes_productos = db.session.query(Costes_producto).order_by(Costes_producto.nombre_producto).all()


    return render_template("/costes/lista_costes_productos.html", lista_costes_productos = todos_costes_productos)



#------------------Eliminar Costes Productos -------------

@app.route("/eliminar_costes_producto/<id>")
def eliminar_costes_producto(id):

    costes_producto = db.session.query(Costes_producto).filter_by(id=int(id)).delete()


    db.session.commit()
    db.session.close()
    return redirect(url_for ("lista_costes_productos"))

#------------------Ficha Costes Producto -------------


@app.route("/costes/ficha_costes_producto/<id>")
def ficha_costes_producto(id):
    costes_producto = db.session.query(Costes_producto).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    return render_template("/costes/ficha_costes_producto.html", ficha_costes_producto = costes_producto)


#------------------Edición Ficha Costes Producto -------------


#----------HOME ------------
@app.route("/costes/edicion_ficha_costes_producto_home/<id>")
def edicion_ficha_costes_producto_home(id):
    costes_producto = db.session.query(Costes_producto).filter_by(id=int(id))
    db.session.commit()
    db.session.close()

    return render_template("/costes/edicion_ficha_costes_producto_home.html", ficha_costes_producto = costes_producto)


#---------def Edición ficha costes producto
@app.route("/edicion_ficha_costes_producto/<id>",methods = ["post"])
def edicion_ficha_costes_producto(id):

    costes_producto = db.session.query(Costes_producto).filter_by(id=int(id)).first()
    costes_producto.nombre_producto = request.form['nombre_producto']
    costes_producto.coste_inicial_producto = request.form['coste_inicial_producto']
    costes_producto.coste_mantenimiento_producto = request.form['coste_mantenimiento_producto']
    costes_producto.coste_carga_producto = request.form['coste_carga_producto']


    db.session.commit()
    db.session.close()

    aux= db.session.query(Costes_producto).filter_by(id=int(id))

    db.session.commit()
    db.session.close()

    return render_template("/costes/ficha_costes_producto.html", ficha_costes_producto = aux)


# ----------------------------------------- Calculadora WEB -----------------------------------------------------------

# ----Calculadora WEB Home----
@app.route("/calculadora_web/calculadora_web_home")
# ----Home Calculadora WEB----
def calculadora_web_home():
    # ----Return
    return render_template("/calculadora_web/calculadora_web_home.html")


# ------ Formula Calculadora WEB -------
@app.route("/calcular_amortizacion", methods=["post"])
def calcular_amortizacion():
    '''Se trabajará con una fórmula que a continuación se mostrará tomando como X el salario bruto de un trabajador,
    se utilizaran como medidas de coste los euros (€) y de tiempo los meses (1 mes = 1, 1 año = 12) y
    se comparará el contratar a un trabajador con un TEMI v2 y su amortización'''

    #---------------------------------------- Costes dse un Trabajador ------------------------------------------------

    # ----- El input del usuario (salario bruto del trabajador)

    salario_bruto_trabajador = int(request.form['salario_bruto_trabajador'])

    #---- Se calcula la seguridad social del trabajador respecto al salario bruto introducido
    #---- Los aportes estandares de una empresa es de 31,75%

    seguridad_social_trabajador = (salario_bruto_trabajador * 31.75) // 100




    #---- Coste reclutamiento del trabajador (Primer mes)
    #----Coste total de contratación = coste reclutador + portales + administrativo + headhunting (aproximado 4500)

    coste_contratacion = 4500

    #---- Coste de material y equipo
    #---- En este caso vamos a poner solo uniforme de trabajo que haremos un estimado de 150 euros (cada seis meses)

    coste_materiales_equipo_trabajador = 150

    #---- Coste de sustitución de Vacaciones (1 vez por año, osea cada 12 meses)
    #----sueldo bruto + Seguridad Social de 1 mes + coste_de_empleado_temporal (aprox 2700€)

    coste_empleado_temporal = 2700

    coste_sustitucion_vacaciones = salario_bruto_trabajador + seguridad_social_trabajador + coste_empleado_temporal

    #---- Coste o aumento de salario por antiguedad (2% por año, osea 2% cada 12 meses)

    coste_antiguedad = (salario_bruto_trabajador * 2) // 100



    #---------- Coste constante por mes de un trabajador

    coste_trebajador_mes = salario_bruto_trabajador + seguridad_social_trabajador

    #-------------------------------- Costes de un TEMI v2  ---------------------------------------------------------

    #------Coste inicial de un Temi v2 (el precio + IVA)

    coste_precio_temiv2 = 8900

    coste_iva_temiv2 = (coste_precio_temiv2 * 21) // 100

    coste_inicial_temiv2 = coste_precio_temiv2 + coste_iva_temiv2

    #-------Coste de carga/gasto electricidad Temi v2 aproximado por mes

    coste_carga_temiv2_mes = 10

    #-------Coste de servicio de mantenimiento Temi v2 aproximado cada 3 meses los primeros 5 años

    coste_mantenimiento = 150



    #--------------------- RESULTADO UNO (1 mes) ---------------------------------------------------------------------

    resultado1_t = coste_trebajador_mes + coste_contratacion + coste_materiales_equipo_trabajador

    resultado1_Temiv2 = coste_inicial_temiv2 + coste_carga_temiv2_mes

    #------ Diferencia de costes (1 mes)

    diferencia_costes = resultado1_t - resultado1_Temiv2

    #---------------------- RESULTADO DOS (3 meses) ------------------------------------------------------------------

    resultado2_t = coste_trebajador_mes * 2

    resultado2_Temiv2 = coste_carga_temiv2_mes * 2 + coste_mantenimiento

    # ------ Diferencia de costes (3 meses)

    diferencia_costes_2 = resultado2_t - resultado2_Temiv2

    # ---------------------- RESULTADO TRES (12 meses / 1 Año) -------------------------------------------------------

    resultado3_t = (coste_trebajador_mes * 9 + coste_materiales_equipo_trabajador +
                    coste_sustitucion_vacaciones + coste_antiguedad )

    resultado3_Temiv2 = coste_carga_temiv2_mes * 9 + coste_mantenimiento * 3

    # ------ Diferencia de costes (12 meses)

    diferencia_costes_3 = resultado3_t - resultado3_Temiv2

    # ---------------------- RESULTADO CUATRO (60 meses / 5 años) -------------------------------------------------------

    resultado4_t = (coste_trebajador_mes * 48 + coste_materiales_equipo_trabajador * 8+
                    coste_sustitucion_vacaciones * 4 + coste_antiguedad * 4)

    resultado4_Temiv2 = coste_carga_temiv2_mes * 48 + coste_mantenimiento * 16

    # ------ Diferencia de costes (60 meses / 5 años)

    diferencia_costes_4 = resultado4_t - resultado4_Temiv2

    # ---------------------- RESULTADO CINCO (120 meses / 10 años) ---------------------------------------------------

    resultado5_t = (coste_trebajador_mes * 60 + coste_materiales_equipo_trabajador * 10 +
                    coste_sustitucion_vacaciones * 5 + coste_antiguedad * 5)

    resultado5_Temiv2 = coste_carga_temiv2_mes * 60 + coste_mantenimiento * 30

    # ------ Diferencia de costes (120 meses / 10 años)

    diferencia_costes_5= resultado5_t - resultado5_Temiv2


    '''Return: se pasan todos los resultados obtenidos para capturarlos en HTML'''

    return render_template("/calculadora_web/resultado_calculadora.html", resultado1_t_web = resultado1_t,
                           resultado1_Temiv2_web = resultado1_Temiv2, diferencia_costes_web = diferencia_costes,
                           resultado2_t_web=resultado2_t, resultado2_Temiv2_web=resultado2_Temiv2,
                           diferencia_costes_2_web=diferencia_costes_2,resultado3_t_web = resultado3_t,
                           resultado3_Temiv2_web = resultado3_Temiv2, diferencia_costes_3_web = diferencia_costes_3,
                           resultado4_t_web=resultado4_t, resultado4_Temiv2_web=resultado4_Temiv2,
                           diferencia_costes_4_web=diferencia_costes_4,resultado5_t_web = resultado5_t,
                           resultado5_Temiv2_web = resultado5_Temiv2, diferencia_costes_5_web = diferencia_costes_5)




# -------------------------------------------- Próximamente ----------------------------------------------------------
# ----Próximamente  Route----
@app.route("/proximamente/proximamente")


def proximamente():

    # ----Return
    return render_template("/proximamente/proximamente.html")







#-------------------------------- MAIN ---------------------------------------------

if __name__ == '__main__':

    # -------- Base de datos -------
    db.Base.metadata.create_all(db.engie)

    # ------- Flask Main Run --------
    app.run(debug=True)