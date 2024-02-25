import tkinter as tk
from PIL import Image, ImageTk

# funciones
def buscar():
    pass

def hola():
    pass

# Inicio de la vista
root = tk.Tk()

# Establezco las dimensiones de la ventana
root.geometry("600x400")

# seteo el titulo de la app
root.title("Maestro de materiales")

# inserto el titulo
tk.Label(root, text="Maestro de Materiales", font=('Arial',15), fg="white", bg="black").pack(fill=tk.X)


# inserto el menu
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=False)

submenu = tk.Menu(filemenu, tearoff=True)

filemenu.add_cascade(label="Registro", menu=submenu)  # Cambiado el label a "Archivo" en lugar de "Registro"
submenu.add_command(label="Modificar", command=hola)
submenu.add_command(label="Eliminar", command=hola)
submenu.add_command(label="Nuevo registro", command=hola)
submenu.add_command(label="Nueva Consulta", command=hola)

filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)  # Cambiado el label a "Archivo" en lugar de "Registro"

helpmenu = tk.Menu(menubar, tearoff=False)
helpmenu.add_command(label="Guia", command=lambda: print("Guia"))
menubar.add_cascade(label="Ayuda", menu=helpmenu)






# agrega la barra de menus a la ventana principal
root.config(menu=menubar)

# Agrego un frame para los botones y otro para mostrar imagenes
frameBotones = tk.Frame(root)
frameImagen = tk.Frame(root)

# posiciono los frames en la ventana
frameBotones.pack(side=tk.LEFT)
frameImagen.pack(side=tk.RIGHT)


# Maquetacion de los widget
material = tk.Label(root, text="Material: ", fg='blue', font=('Helvetica', 14))
material.pack(side=tk.LEFT, padx=50, pady=25, anchor=tk.NW)

material_entrada = tk.Entry(root, width=30)
material_entrada.pack(side=tk.LEFT, padx=0, pady=30, anchor=tk.NW)

boton = tk.Button(root, text="Buscar", command=buscar)
boton.pack(side=tk.LEFT, padx=60, pady=25, anchor=tk.NW)

# Cargar la imagen y redimensionarla
imagen_pil = Image.open("./1.jpg")
imagen_pil = imagen_pil.resize((400, 200))  # Redimensionar la imagen a 200x200 píxeles
imagen = ImageTk.PhotoImage(imagen_pil)

# Mostrar la imagen en un Label
label_imagen = tk.Label(root, image=imagen)
label_imagen.image = imagen
label_imagen.place(x=100, y=120)  # Ajusta las coordenadas según sea necesario

# fin de la vista
root.mainloop()

