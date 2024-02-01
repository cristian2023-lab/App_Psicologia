from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import ITALIC
import sqlite3
from PIL import Image, ImageTk
import re
import datetime


# ##############################################
# MODELO
# ##############################################

######## CREAR LA BASE DE DATOS SQLITE #######


def crear_base():
    con = sqlite3.connect("mispacientes.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
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
    cursor.execute(sql)
    con.commit()


#####  FUNCIONES ####


def alta(
    con,
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

    messagebox.askyesno("¿Desea dar de alta al paciente?")


def baja(
    con,
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

    messagebox.askyesno("¿Está seguro que desea dar de baja al paciente?.")


def actualizar(
    con,
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
    con = crear_base()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pacientes")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


def limpiar_entradas():
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


##### con doble click en el paciente cargado en el treeview te devuelve al formulario todos los datos cargados ########


def on_double_click(event):
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


#############################################################


# ##############################################
# VISTA
# ##############################################

# MASTER #

master = Tk()
master.geometry("1000x800")
master.title("Datos del paciente")
master.config(bg="cornflowerblue")

# IMAGEN

imagen_path = "psico.jpg"
imagen = Image.open(imagen_path)
imagen = imagen.resize((100, 100))
imagen_tk = ImageTk.PhotoImage(imagen)


label_imagen = Label(master, image=imagen_tk)
label_imagen.grid(row=13, column=0, columnspan=1, padx=1, pady=1, sticky="we")

# SEPARADOR FRAME

separador = Frame(master, height=100, relief="sunken", background="lightblue")
separador.grid(row=0, column=0, columnspan=14, sticky="we")
Label(
    separador,
    text="Bienvenido!",
    background="lightblue",
    font=("Arial", 10, ITALIC),
).grid(row=0, column=0, padx=5, pady=5)


# VARIABLES

var_nombre = StringVar()
var_apellido = StringVar()
var_fecha_nacimiento = StringVar()
var_obra_social = StringVar()
var_numero_carnet = StringVar()
var_direccion = StringVar()
var_localidad = StringVar()
var_partido = StringVar()
var_email = StringVar()
var_telefono = IntVar()
var_diagnostico = StringVar()


nombre = Label(master, text="Nombre", bg="orange", font="Arial, 10")
nombre.grid(row=1, column=0, sticky=W)
apellido = Label(master, text="Apellido", bg="orange", font="Arial, 10")
apellido.grid(row=2, column=0, sticky=W)
fecha_nacimiento = Label(
    master, text="Fecha de nacimiento", bg="orange", font="Arial, 10"
)
fecha_nacimiento.grid(row=3, column=0, sticky=W)
obra_social = Label(master, text="Obra social", bg="orange", font="Arial, 10")
obra_social.grid(row=4, column=0, sticky=W)
numero_carnet = Label(master, text="Numero de carnet", bg="orange", font="Arial, 10")
numero_carnet.grid(row=5, column=0, sticky=W)
direccion = Label(master, text="Direccion", bg="orange", font="Arial, 10")
direccion.grid(row=6, column=0, sticky=W)
localidad = Label(master, text="Localidad", bg="orange", font="Arial, 10")
localidad.grid(row=7, column=0, sticky=W)
partido = Label(master, text="Partido", bg="orange", font="Arial, 10")
partido.grid(row=8, column=0, sticky=W)
email = Label(master, text="Email", bg="orange", font="Arial, 10")
email.grid(row=9, column=0, sticky=W)
telefono = Label(master, text="Telefono", bg="orange", font="Arial, 10")
telefono.grid(row=10, column=0, sticky=W)
diagnostico = Label(master, text="Diagnostico", bg="orange", font="Arial, 10")
diagnostico.grid(row=11, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada #

(
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
) = (
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    IntVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    IntVar(),
    StringVar(),
)
w_ancho = 20


# ENTRADAS

entry_nombre = Entry(
    master, textvariable=var_nombre, bg="orange", width=25, font="Arial, 10"
)
entry_nombre.grid(row=1, column=1)
entry_apellido = Entry(
    master, textvariable=var_apellido, bg="orange", width=25, font="Arial, 10"
)
entry_apellido.grid(row=2, column=1)
entry_fecha_nacimiento = Entry(
    master, textvariable=var_fecha_nacimiento, bg="orange", width=25, font="Arial, 10"
)
entry_fecha_nacimiento.grid(row=3, column=1)
entry_obra_soacial = Entry(
    master, textvariable=var_obra_social, bg="orange", width=25, font="Arial, 10"
)
entry_obra_soacial.grid(row=4, column=1)
entry_numero_carnet = Entry(
    master, textvariable=var_numero_carnet, bg="orange", width=25, font="Arial, 10"
)
entry_numero_carnet.grid(row=5, column=1)
entry_direccion = Entry(
    master, textvariable=var_direccion, bg="orange", width=25, font="Arial, 10"
)
entry_direccion.grid(row=6, column=1)
entry_localidad = Entry(
    master, textvariable=var_localidad, bg="orange", width=25, font="Arial, 10"
)
entry_localidad.grid(row=7, column=1)
entry_partido = Entry(
    master, textvariable=var_partido, bg="orange", width=25, font="Arial, 10"
)
entry_partido.grid(row=8, column=1)
entry_email = Entry(
    master, textvariable=var_email, bg="orange", width=25, font="Arial, 10"
)
entry_email.grid(row=9, column=1)
entry_telefono = Entry(
    master, textvariable=var_telefono, bg="orange", width=25, font="Arial, 10"
)
entry_telefono.grid(row=10, column=1)
entry_diagnostico = Entry(
    master, textvariable=var_diagnostico, bg="orange", width=25, font="Arial, 10"
)
entry_diagnostico.grid(row=11, column=1)


############### TREEVIEW ###########

tree = ttk.Treeview(
    master,
    columns=(
        "col1",
        "col2",
        "col3",
        "col4",
        "col5",
        "col6",
        "col7",
        "col8",
        "col9",
        "col10",
        "col11",
    ),
)

### TITULOS DE LAS COLUMNAS

tree.heading("#0", text="ID")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="Fecha Nacimiento")
tree.heading("col4", text="Obra Social")
tree.heading("col5", text="Nro Carnet")
tree.heading("col6", text="Dirección")
tree.heading("col7", text="Localidad")
tree.heading("col8", text="Partido")
tree.heading("col9", text="Email")
tree.heading("col10", text="Teléfono")
tree.heading("col11", text="Diagnóstico")

# DIMENSION DE LAS COLUMNAS

tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.column("col3", width=80, minwidth=80, anchor=W)
tree.column("col4", width=80, minwidth=80, anchor=W)
tree.column("col5", width=80, minwidth=80, anchor=W)
tree.column("col6", width=80, minwidth=80, anchor=W)
tree.column("col7", width=80, minwidth=80, anchor=W)
tree.column("col8", width=80, minwidth=80, anchor=W)
tree.column("col9", width=80, minwidth=80, anchor=W)
tree.column("col10", width=80, minwidth=80, anchor=W)
tree.column("col11", width=80, minwidth=80, anchor=W)

tree.grid(column=0, row=12, columnspan=14)

actualizar_treeview(tree)

# BOTONES

# Botón Alta
boton_alta = Button(
    master,
    text="Alta",
    padx=10,
    pady=1,
    bg="orange",
    font="Arial, 10",
    command=lambda: alta_si_valido(),
)


def alta_si_valido():
    try:
        if validar_fecha_nacimiento(var_fecha_nacimiento.get()) and validar_mail(
            var_email.get()
        ):
            alta(
                crear_base(),
                var_nombre.get(),
                var_apellido.get(),
                var_fecha_nacimiento.get(),
                var_obra_social.get(),
                var_numero_carnet.get(),
                var_direccion.get(),
                var_localidad.get(),
                var_partido.get(),
                var_email.get(),
                var_telefono.get(),
                var_diagnostico.get(),
            )
        else:
            messagebox.showerror("Error", "Fecha de nacimiento o email no válidos")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    actualizar_treeview(tree)


boton_alta.grid(row=13, column=2)

boton_baja = Button(
    master,
    text="Baja",
    padx=10,
    pady=1,
    bg="orange",
    font="Arial, 10",
    command=lambda: [
        baja(
            crear_base(),
            var_nombre.get(),
            var_apellido.get(),
            var_fecha_nacimiento.get(),
            var_obra_social.get(),
            var_numero_carnet.get(),
            var_direccion.get(),
            var_localidad.get(),
            var_partido.get(),
            var_email.get(),
            var_telefono.get(),
            var_diagnostico.get(),
        ),
        actualizar_treeview(tree),
    ],
)

boton_baja.grid(row=13, column=3)

boton_actualizar = Button(
    master,
    text="Actualizar",
    padx=10,
    pady=1,
    bg="orange",
    font="Arial, 10",
    command=lambda: [
        actualizar(
            crear_base(),
            var_nombre.get(),
            var_apellido.get(),
            var_fecha_nacimiento.get(),
            var_obra_social.get(),
            var_numero_carnet.get(),
            var_direccion.get(),
            var_localidad.get(),
            var_partido.get(),
            var_email.get(),
            var_telefono.get(),
            var_diagnostico.get(),
        ),
        actualizar_treeview(tree),
    ],
)

boton_actualizar.grid(row=13, column=4)

boton_consulta = Button(
    master,
    text="Consulta",
    padx=10,
    pady=1,
    bg="orange",
    font="Arial, 10",
    command=lambda: consulta(tree),
)
boton_consulta.grid(row=13, column=5)

boton_limpiar_entradas = Button(
    master,
    text="Limpiar formulario",
    padx=10,
    pady=1,
    bg="orange",
    font="Arial, 10",
    command=limpiar_entradas,
)
boton_limpiar_entradas.grid(row=13, column=6)

tree.bind("<Double-1>", on_double_click)

master.mainloop()
