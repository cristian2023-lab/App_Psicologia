import sqlite3
from tkinter import ttk
from tkinter import Tk
from tkinter.font import ITALIC
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import datetime
import os


# ##############################################
# MODELO
# ##############################################

######## CREAR LA BASE DE DATOS SQLITE #######

class Conexion:
    def __init__(self):
        self.con = sqlite3.connect("mispacientes.db")
        self.cursor = self.con.cursor()
        self.crear_tabla()
        
    def crear_tabla(self):
        self.cursor = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS pacientes(
        mi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellido TEXT,
        fecha_nacimiento TEXT,
        obra_social TEXT,
        numero_carnet INTEGER,
        direccion TEXT,
        localidad TEXT,
        partido TEXT,
        email TEXT,
        telefono INTEGER,
        diagnostico TEXT
    )"""
        self.cursor.execute(sql)
        self.con.commit()

class FechaNacimientoLogError(Exception):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(BASE_DIR, "log.txt")

    def __init__(self, archivo, fecha_nacimiento):
        self.archivo = archivo
        self.fecha_nacimiento = fecha_nacimiento

    def registrar_error(self):
        with open(self.ruta, "a") as log:
            log.write(f"Se ha producido un error en {self.archivo}: {self.fecha_nacimiento}\n")

def registrar():
    raise FechaNacimientoLogError("archivo1.txt", datetime.datetime.now())

try:
    registrar()
except FechaNacimientoLogError as log:
    log.registrar_error()

          

#####  FUNCIONES ####

def alta(
    nombre,
    apellido,
    fecha_nacimiento,
    obra_social,
    numero_carnet,
    direccion,
    localidad,
    partido,
    email,
    telefono,
    diagnostico,
):
    
    con = sqlite3.connect("mispacientes.db")
    cursor = con.cursor()
    data = (
        nombre,
        apellido,
        fecha_nacimiento,
        obra_social,
        numero_carnet,
        direccion,
        localidad,
        partido,
        email,
        telefono,
        diagnostico,
    )
    
    sql = """INSERT INTO pacientes(nombre, apellido, fecha_nacimiento, obra_social, numero_carnet, direccion, localidad, partido, email, telefono, diagnostico)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, data)
    con.commit()
    
    tk = Tk()
    tk.withdraw()
    messagebox.askyesno("¿Desea dar de alta al paciente?")
    

def baja(
    nombre,
    apellido,
    fecha_nacimiento,
    obra_social,
    numero_carnet,
    direccion,
    localidad,
    partido,
    email,
    telefono,
    diagnostico,
):
    
    con = sqlite3.connect("mispacientes.db")
    cursor = con.cursor()
    data = (
        nombre,
        apellido,
        fecha_nacimiento,
        obra_social,
        numero_carnet,
        direccion,
        localidad,
        partido,
        email,
        telefono,
        diagnostico,
    )
    sql = "DELETE FROM pacientes WHERE nombre = ? AND apellido = ? AND fecha_nacimiento = ? AND obra_social = ? AND numero_carnet = ? AND direccion = ? AND localidad = ? AND partido = ? AND email = ? AND telefono = ? AND diagnostico = ?"
    cursor.execute(sql, data)
    con.commit()

    tk = Tk()
    tk.withdraw()
    messagebox.askyesno("¿Está seguro que desea dar de baja al paciente?.")


def actualizar(
    nombre,
    apellido,
    fecha_nacimiento,
    obra_social,
    numero_carnet,
    direccion,
    localidad,
    partido,
    email,
    telefono,
    diagnostico,
):
    
    con = sqlite3.connect("mispacientes.db")
    cursor = con.cursor()
    data = (
        apellido,
        fecha_nacimiento,
        obra_social,
        numero_carnet,
        direccion,
        localidad,
        partido,
        email,
        telefono,
        diagnostico,
        nombre,
    )

    sql = "UPDATE pacientes SET apellido=?, fecha_nacimiento=?, obra_social=?, numero_carnet=?, direccion=?, localidad=?, partido=?, email=?, telefono=?, diagnostico=? WHERE nombre=?"
    cursor.execute(sql, data)
    con.commit()

    tk = Tk()
    tk.withdraw()
    messagebox.askyesno("Éxito", "Se ha dado actualizado exitosamente el paciente.")


def consulta(tree):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")

        nombre = values[1]
        apellido = values[2]
        fecha_nacimiento = values[3]
        obra_social = values[4]
        numero_carnet = values[5]
        direccion = values[6]
        localidad = values[7]
        partido = values[8]
        email = values[9]
        telefono = values[10]
        diagnostico = values[11]

        datos_paciente = f"Nombre: {nombre}\nApellido: {apellido}\nFecha de Nacimiento: {fecha_nacimiento}\nObra Social: {obra_social}\nNúmero de Carnet: {numero_carnet}\nDirección: {direccion}\nLocalidad: {localidad}\nPartido: {partido}\nEmail: {email}\nTeléfono: {telefono}\nDiagnóstico: {diagnostico}"
        messagebox.showwarning("Datos del paciente", datos_paciente)
    else:
        messagebox.showerror("Error", "Seleccione un paciente para consultar.")


def actualizar_treeview(tree):
    for item in tree.get_children():
        tree.delete(item)

    con = sqlite3.connect("mispacientes.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pacientes")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


def limpiar_entradas(
    var_nombre,
    var_apellido,
    var_fecha_nacimiento,
    var_obra_social,
    var_numero_carnet,
    var_direccion,
    var_localidad,
    var_partido,
    var_email,
    var_telefono,
    var_diagnostico,
):
    var_nombre.set("")
    var_apellido.set("")
    var_fecha_nacimiento.set("")
    var_obra_social.set("")
    var_numero_carnet.set("")
    var_direccion.set("")
    var_localidad.set("")
    var_partido.set("")
    var_email.set("")
    var_telefono.set("")  
    var_diagnostico.set("")

def on_double_click(event, tree, var_nombre, var_apellido, var_fecha_nacimiento, var_obra_social, var_numero_carnet, var_direccion, var_localidad, var_partido, var_email, var_telefono, var_diagnostico):
    item = tree.selection()[0]
    try:
        var_nombre.set(tree.item(item, "values")[1])
        var_apellido.set(tree.item(item, "values")[2])
        var_fecha_nacimiento.set(tree.item(item, "values")[3])
        var_obra_social.set(tree.item(item, "values")[4])
        var_numero_carnet.set(tree.item(item, "values")[5])
        var_direccion.set(tree.item(item, "values")[6])
        var_localidad.set(tree.item(item, "values")[7])
        var_partido.set(tree.item(item, "values")[8])
        var_email.set(tree.item(item, "values")[9])
        var_telefono.set(tree.item(item, "values")[10])
        var_diagnostico.set(tree.item(item, "values")[11])
    except IndexError:
        pass


#################### REG



#################### REGREX PARA VALIDAR MAIL Y FECHA ###############
def validar_mail(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, email))


def validar_fecha_nacimiento(fecha_nacimiento):
    patron = r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}$"

    if re.match(patron, fecha_nacimiento):
        return True
    else:
        raise ValueError(
            "La fecha de nacimiento no tiene el formato correcto (dd/mm/yyyy o dd-mm-yyyy)"
        )