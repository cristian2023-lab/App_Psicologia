from tkinter import StringVar
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Tk
from tkinter import Frame
from tkinter.font import ITALIC
from tkinter import messagebox
from tkinter import W
from tkinter import Button
from typing import Self
from PIL import Image, ImageTk


from modelo import Conexion
from modelo import alta
from modelo import baja
from modelo import actualizar
from modelo import consulta
from modelo import actualizar_treeview
from modelo import limpiar_entradas
from modelo import on_double_click
from modelo import validar_fecha_nacimiento
from modelo import validar_mail


class VistaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x800")
        self.master.title("Datos del paciente")
        self.master.config(bg="cornflowerblue")
        
    def cargar_imagen(self):
        imagen_path = "psico.jpg"
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((100, 100))
        imagen_tk = ImageTk.PhotoImage(imagen)

        self.label_imagen =Label(self, image=imagen_tk)
        self.label_imagen.grid(row=13, column=0, columnspan=1, padx=1, pady=1, sticky="we")

        
    def separador_frame(self):
        self.separador = Frame(self, height=100, relief="sunken", background="lightblue")
        self.separador.grid(row=0, column=0, columnspan=14, sticky="we")
        Label(
             self.separador,
             text="Bienvenido!",
             background="lightblue",
             font=("Arial", 10, ITALIC),
        ).grid(row=0, column=0, padx=5, pady=5)  
    
    # VARIABLES
    def variables(self):
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_fecha_nacimiento = StringVar()
        self.var_obra_social = StringVar()
        self.var_numero_carnet = StringVar()
        self.var_direccion = StringVar()
        self.var_localidad = StringVar()
        self.var_partido = StringVar()
        self.var_email = StringVar()
        self.var_telefono = IntVar()
        self.var_diagnostico = StringVar()  

    def entradas(self):
        self.nombre = Label(self, text="Nombre", bg="orange", font="Arial, 10")
        self.nombre.grid(row=1, column=0, sticky="w")
        self.apellido = Label(self, text="Apellido", bg="orange", font="Arial, 10")
        self.apellido.grid(row=2, column=0, sticky="w")
        self.fecha_nacimiento = Label(self, text="Fecha de nacimiento", bg="orange", font="Arial, 10")
        self.fecha_nacimiento.grid(row=3, column=0, sticky="w")
        self.obra_social = Label(self, text="Obra social", bg="orange", font="Arial, 10")
        self.obra_social.grid(row=4, column=0, sticky="w")
        self.numero_carnet = Label(self, text="Numero de carnet", bg="orange", font="Arial, 10")
        self.numero_carnet.grid(row=5, column=0, sticky="w")
        self.direccion = Label(self, text="Direccion", bg="orange", font="Arial, 10")
        self.direccion.grid(row=6, column=0, sticky="w")
        self.localidad = Label(self, text="Localidad", bg="orange", font="Arial, 10")
        self.localidad.grid(row=7, column=0, sticky="w")
        self.partido = Label(self, text="Partido", bg="orange", font="Arial, 10")
        self.partido.grid(row=8, column=0, sticky="w")
        self.email = Label(self, text="Email", bg="orange", font="Arial, 10")
        self.email.grid(row=9, column=0, sticky="w")
        self.telefono = Label(self, text="Telefono", bg="orange", font="Arial, 10")
        self.telefono.grid(row=10, column=0, sticky="w")
        self.diagnostico = Label(self, text="Diagnostico", bg="orange", font="Arial, 10")
        self.diagnostico.grid(row=11, column=0, sticky="w")
        
        # Defino variables para tomar valores de campos de entrada #
    def variables_valores(self):
        self.var_nombre,
        self.var_apellido,
        self.var_fecha_nacimiento,
        self.var_obra_social,
        self.var_numero_carnet,
        self.var_direccion,
        self.var_localidad,
        self.var_partido,
        self.var_email,
        self.var_telefono,
        self.var_diagnostico,
    
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
    
    w_ancho = 20

    def entrys(self):
        self.entry_nombre = Entry(
            self, textvariable=self.var_nombre, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_nombre.grid(row=1, column=1)
        self.entry_apellido = Entry(
            self, textvariable=self.var_apellido, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_apellido.grid(row=2, column=1)
        self.entry_fecha_nacimiento = Entry(
            self, textvariable=self.var_fecha_nacimiento, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_fecha_nacimiento.grid(row=3, column=1)
        self.entry_obra_social = Entry(
            self, textvariable=self.var_obra_social, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_obra_social.grid(row=4, column=1)
        self.entry_numero_carnet = Entry(
            self, textvariable=self.var_numero_carnet, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_numero_carnet.grid(row=5, column=1)
        self.entry_direccion = Entry(
            self, textvariable=self.var_direccion, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_direccion.grid(row=6, column=1)
        self.entry_localidad = Entry(
            self, textvariable=self.var_localidad, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_localidad.grid(row=7, column=1)
        self.entry_partido = Entry(
            self, textvariable=self.var_partido, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_partido.grid(row=8, column=1)
        self.entry_email = Entry(
            self, textvariable=self.var_email, bg="orange", width=25, font="Arial, 10"
        )
        self.entry_email.grid(row=9, column=1)
        entry_telefono = Entry(
            self, textvariable=self.var_telefono, bg="orange", width=25, font="Arial, 10"
        )
        entry_telefono.grid(row=10, column=1)
        entry_diagnostico = Entry(
            self, textvariable=self.var_diagnostico, bg="orange", width=25, font="Arial, 10"
        )
        entry_diagnostico.grid(row=11, column=1)
    
        
        # Creación del Treeview
    def crear_Tree(self):
        self.tree = ttk.Treeview(self,
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

    def titulos_columnas(self):
        self.tree = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Fecha Nacimiento")
        self.tree.heading("col4", text="Obra Social")
        self.tree.heading("col5", text="Nro Carnet")
        self.tree.heading("col6", text="Dirección")
        self.tree.heading("col7", text="Localidad")
        self.tree.heading("col8", text="Partido")
        self.tree.heading("col9", text="Email")
        self.tree.heading("col10", text="Telefono")
        self.tree.heading("col11", text="Diagnostico")

    def dimension_columnas(self):    
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=80, minwidth=80, anchor=W)
        self.tree.column("col2", width=80, minwidth=80, anchor=W)
        self.tree.column("col3", width=80, minwidth=80, anchor=W)
        self.tree.column("col4", width=80, minwidth=80, anchor=W)
        self.tree.column("col5", width=80, minwidth=80, anchor=W)
        self.tree.column("col6", width=80, minwidth=80, anchor=W)
        self.tree.column("col7", width=80, minwidth=80, anchor=W)
        self.tree.column("col8", width=80, minwidth=80, anchor=W)
        self.tree.column("col9", width=80, minwidth=80, anchor=W)
        self.tree.column("col10", width=80, minwidth=80, anchor=W)
        self.tree.column("col11", width=80, minwidth=80, anchor=W)

        self.tree.grid(column=0, row=12, columnspan=14)

        self.actualizar_treeview(self)

        
    def botones(self):
        self.boton_alta = Button(
        self,
        text="Alta",
        padx=10,
        pady=1,
        bg="orange",
        font="Arial, 10",
        command=lambda: self.alta_si_valido(),
        )


    def alta_si_valido(self):
        try:
            if self.validar_fecha_nacimiento(self.var_fecha_nacimiento.get()) and self.validar_mail(
                self.var_email.get()
            ):
                alta(
                    self.crear_base(),
                    self.var_nombre.get(),
                    self.var_apellido.get(),
                    self.var_fecha_nacimiento.get(),
                    self.var_obra_social.get(),
                    self.var_numero_carnet.get(),
                    self.var_direccion.get(),
                    self.var_localidad.get(),
                    self.var_partido.get(),
                    self.var_email.get(),
                    self.var_telefono.get(),
                    self.var_diagnostico.get(),
                )
                messagebox.showinfo("Éxito", "El paciente se dio de alta exitosamente.")
            else:
                messagebox.showerror("Error", "Fecha de nacimiento o email no válidos")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        self.actualizar_treeview(self)


        self.boton_alta.grid(row=13, column=2)

        self.boton_baja = Button(
            self,
            text="Baja",
            padx=10,
            pady=1,
            bg="orange",
            font="Arial, 10",
            command=lambda: [
                self.baja(
                    self.crear_base(),
                    self.var_nombre.get(),
                    self.var_apellido.get(),
                    self.var_fecha_nacimiento.get(),
                    self.var_obra_social.get(),
                    self.var_numero_carnet.get(),
                    self.var_direccion.get(),
                    self.var_localidad.get(),
                    self.var_partido.get(),
                    self.var_email.get(),
                    self.var_telefono.get(),
                    self.var_diagnostico.get(),
                ),
                actualizar_treeview(self),
            ],
        )

        self.boton_baja.grid(row=13, column=3)

        self.boton_actualizar = Button(
            self,
            text="Actualizar",
            padx=10,
            pady=1,
            bg="orange",
            font="Arial, 10",
            command=lambda: [
                self.actualizar(
                    self.crear_base(),
                    self.var_nombre.get(),
                    self.var_apellido.get(),
                    self.var_fecha_nacimiento.get(),
                    self.var_obra_social.get(),
                    self.var_numero_carnet.get(),
                    self.var_direccion.get(),
                    self.var_localidad.get(),
                    self.var_partido.get(),
                    self.var_email.get(),
                    self.var_telefono.get(),
                    self.var_diagnostico.get(),
                ),
                actualizar_treeview(self),
            ],
        )

        self.boton_actualizar.grid(row=13, column=4)

        self.boton_consulta = Button(
            self,
            text="Consulta",
            padx=10,
            pady=1,
            bg="orange",
            font="Arial, 10",
            command=lambda: self.consulta(self),
        )
        self.boton_consulta.grid(row=13, column=5)

        self.boton_limpiar_entradas = Button(
        self,
        text="Limpiar formulario",
        padx=10,
        pady=1,
        bg="orange",
        font="Arial, 10",
        command=lambda: self.limpiar_entradas(
            self.var_nombre,
            self.var_apellido,
            self.var_fecha_nacimiento,
            self.var_obra_social,
            self.var_numero_carnet,
            self.var_direccion,
            self.var_localidad,
            self.var_partido,
            self.var_email,
            self.var_telefono,
            self.var_diagnostico,
        ),
    )

      
        self.boton_limpiar_entradas.grid(row=13, column=6)

        self.tree.bind("<Double-1>", lambda event: on_double_click(event, self.tree, self.var_nombre, self.var_apellido, self.var_fecha_nacimiento, self.var_obra_social, self.var_numero_carnet, self.var_direccion, self.var_localidad, self.var_partido, self.var_email, self.var_telefono, self.var_diagnostico))


    