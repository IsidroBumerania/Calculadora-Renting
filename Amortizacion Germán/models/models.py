from sqlalchemy import Column, Integer, String, Boolean
from base_de_datos import db


#----------------------- Datos del Cliente -----------------------------
class Cliente (db.Base):
    __tablename__ = "clientes"
    __tableargs__ = {'sqlite_autoincrement' : True}
    id = Column(Integer, primary_key=True)
    nombre_cliente = Column(String, nullable=False)
    CIF_cliente = Column(String, nullable=False)
    direccion_cliente = Column(String, nullable=False)
    codigo_postal_cliente = Column(String, nullable=False)
    poblacion_cliente = Column(String, nullable=False)
    provincia_cliente = Column(String, nullable=False)
    pais_cliente = Column(String, nullable=False)
    telefono_cliente = Column(String, nullable=False)
    movil_cliente = Column(String, nullable=False)
    email_cliente = Column(String)
    web_cliente = Column(String)
    comentario_cliente = Column(String)



    def __init__(self,nombre_cliente,CIF_cliente,direccion_cliente,codigo_postal_cliente,poblacion_cliente,
                 provincia_cliente,pais_cliente,telefono_cliente,movil_cliente,email_cliente,
                 web_cliente,comentario_cliente):

        self.nombre_cliente = nombre_cliente
        self.CIF_cliente = CIF_cliente
        self.direccion_cliente = direccion_cliente
        self.codigo_postal_cliente = codigo_postal_cliente
        self.poblacion_cliente = poblacion_cliente
        self.provincia_cliente = provincia_cliente
        self.pais_cliente = pais_cliente
        self.telefono_cliente = telefono_cliente
        self.movil_cliente = movil_cliente
        self. email_cliente = email_cliente
        self.web_cliente = web_cliente
        self.comentario_cliente = comentario_cliente


#----------------------- Datos del Productos -----------------------------
class Producto (db.Base):
    __tablename__ = "productos"
    __tableargs__ = {'sqlite_autoincrement' : True}
    id = Column(Integer, primary_key=True)
    nombre_producto = Column(String, nullable=False)
    Numero_de_serie_producto = Column(String)
    sistema_operativo_producto = Column(String)
    color_producto = Column(String)
    tamanio_producto = Column(String)
    peso_producto = Column(String)
    pantalla_producto = Column(String)
    microfonos_producto = Column(String)
    audio_producto = Column(String)
    camaras_producto = Column(String)
    cpu_producto = Column(String)
    alimentacion_producto = Column(String)
    velocidad_producto = Column(String)
    puertos_producto = Column(String)
    descripcion_producto = Column(String)



    def __init__(self,nombre_producto,Numero_de_serie_producto,sistema_operativo_producto,color_producto,
                 tamanio_producto,peso_producto,pantalla_producto,microfonos_producto,
                 audio_producto,camaras_producto,cpu_producto,alimentacion_producto,velocidad_producto,
                 puertos_producto,descripcion_producto):

        self.nombre_producto = nombre_producto
        self.Numero_de_serie_producto = Numero_de_serie_producto
        self.sistema_operativo_producto = sistema_operativo_producto
        self.color_producto = color_producto
        self.tamanio_producto = tamanio_producto
        self.peso_producto = peso_producto
        self.pantalla_producto = pantalla_producto
        self.microfonos_producto = microfonos_producto
        self.audio_producto = audio_producto
        self.camaras_producto = camaras_producto
        self.cpu_producto = cpu_producto
        self.alimentacion_producto = alimentacion_producto
        self.velocidad_producto = velocidad_producto
        self.puertos_producto = puertos_producto
        self.descripcion_producto = descripcion_producto



#----------------------- Costes del Productos -----------------------------
class Costes_producto (db.Base):
    __tablename__ = "costes_productos"
    __tableargs__ = {'sqlite_autoincrement' : True}
    id = Column(Integer, primary_key=True)
    nombre_producto = Column(String, nullable=False)
    coste_inicial_producto = Column(Integer, nullable=False)
    coste_mantenimiento_producto = Column(Integer, nullable=False)
    coste_carga_producto = Column(Integer, nullable=False)




    def __init__(self,nombre_producto,coste_inicial_producto,coste_mantenimiento_producto,
                 coste_carga_producto):

        self.nombre_producto = nombre_producto
        self.coste_inicial_producto = coste_inicial_producto
        self.coste_mantenimiento_producto = coste_mantenimiento_producto
        self.coste_carga_producto = coste_carga_producto




#----------------------- Costes del Trabajador -----------------------------
class Costes_trabajador (db.Base):
    __tablename__ = "costes_trabajadores"
    __tableargs__ = {'sqlite_autoincrement' : True}
    id = Column(Integer, primary_key=True)
    nombre_empresa_trabajador = Column(String, nullable=False)
    coste_salario_bruto_trabajador = Column(Integer, nullable=False)
    coste_seguridad_social_trabajador = Column(Integer, nullable=False)
    coste_de_reclutamiento_trabajador = Column(Integer, nullable=False)
    coste_adicionales_trabajador = Column(Integer, nullable=False)




    def __init__(self,nombre_empresa_trabajador,coste_salario_bruto_trabajador,coste_seguridad_social_trabajador,
                 coste_de_reclutamiento_trabajador,coste_adicionales_trabajador):

        self.nombre_empresa_trabajador = nombre_empresa_trabajador
        self.coste_salario_bruto_trabajador = coste_salario_bruto_trabajador
        self.coste_seguridad_social_trabajador = coste_seguridad_social_trabajador
        self.coste_de_reclutamiento_trabajador = coste_de_reclutamiento_trabajador
        self.coste_adicionales_trabajador = coste_adicionales_trabajador