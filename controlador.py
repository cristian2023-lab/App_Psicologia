from tkinter import Tk
from tkinter import ttk
from tkinter.font import ITALIC
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import W
import vista
import modelo


class VisorDeImagenApp:
    def __init__(self, master):
       self.master = master
       master.title("Visor de Imagen")
       self.Conexion = modelo.Conexion()
       vista.VistaPrincipal(master) 
      
                  
if __name__ == "__main__":
    master_tk = Tk()
    app = VisorDeImagenApp(master_tk)
    master_tk.mainloop()