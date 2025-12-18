import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
raiz= tk.Tk()
raiz.title("Registro de Usuarios Contador Pallet")
raiz.geometry("400x500")
#raiz.iconbitmap ("imagen1.ico")


# Lista para almacenar los usuarios. Se añade un campo 'Resultado' para guardar el cálculo.
usuarios = []
# Las variables globales filas, Columnas, Filas_profundidad, y resultado
# ya no son necesarias porque se manejarán dentro del diccionario de cada usuario.
# filas = int()
# Columnas = int()
# Filas_profundidad = int()
# resultado= int()

# Función para actualizar la lista de usuarios mostrada en la interfaz
def actualizar_lista():
    listbox_usuarios.delete(0, tk.END)
    for usuario in usuarios:
        # Se accede directamente al resultado que se guardó en el diccionario del usuario
        listbox_usuarios.insert(tk.END, f"Nombre: {usuario['Nombre']} - Correo: {usuario['Correo']} - Unidades: {usuario['Resultado']} und - peso: {usuario['resultado2']}")
        # El antiguo código era:
        # listbox_usuarios.insert(tk.END, f"Nombre: {usuario['Nombre']} - Correo: {usuario['Correo']} - Unidades:", resultado)

# Función para abrir una ventana secundaria para registrar usuarios
def abrir_ventana_registro():
    ventana_registro = tk.Toplevel(raiz)
    ventana_registro.title("Registrar Nuevo Pallet")
    ventana_registro.geometry("400x400")
   # ventana_registro.iconbitmap("Imagen1.ico")

    # Etiqueta y entrada para el nombre en la ventana secundaria
    label_nombre = tk.Label(ventana_registro, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack(pady=5)

    label_correo = tk.Label(ventana_registro, text="Correo:")
    label_correo.pack(pady=5)
    entry_correo = tk.Entry(ventana_registro)
    entry_correo.pack(pady=5)

    label_Filas = tk.Label(ventana_registro, text="Filas:")
    label_Filas.pack(pady=5)
    entry_Filas = tk.Entry(ventana_registro)
    entry_Filas.pack(pady=5)

    label_columnas = tk.Label(ventana_registro, text="Columnas:")
    label_columnas.pack(pady=5)
    entry_columnas = tk.Entry(ventana_registro)
    entry_columnas.pack(pady=5)

    label_Filas_profundidad = tk.Label(ventana_registro, text="Filas a fondo:")
    label_Filas_profundidad.pack(pady=5)
    entry_Filas_profundidad = tk.Entry(ventana_registro)
    entry_Filas_profundidad.pack(pady=5)
    
    label_peso = tk.Label(ventana_registro, text="peso x und")
    label_peso.pack(pady=5)
    entry_peso = tk.Entry(ventana_registro)
    entry_peso.pack(pady=5)
    

    # Función para agregar el nuevo usuario desde la ventana secundaria
    def agregar_usuario():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        
        # Inicializamos variables para evitar errores si la conversión falla
        filas = Columnas = Filas_profundidad = resultado = None
        
        try: 
            filas = int(entry_Filas.get())
            Columnas = int(entry_columnas.get())
            Filas_profundidad = int(entry_Filas_profundidad.get())
            # Cálculo de resultado
            resultado = filas * Columnas * Filas_profundidad
            resultado2 = resultado * peso
        except ValueError:
            messagebox.showwarning("Advertencia", "Por favor, ingrese valores numéricos válidos en Filas, Columnas y Filas a fondo.")
            return # Detiene la función si hay un error en los números

        # Verificación de que todos los campos de texto y los valores numéricos son válidos
        if nombre and correo and filas is not None and Columnas is not None and Filas_profundidad is not None:
            # Se agrega el campo 'Resultado' al diccionario del usuario
            usuarios.append({
                "Nombre": nombre, 
                "Correo": correo, 
                "Filas": filas, 
                "Columnas": Columnas, 
                "Filas a fondo": Filas_profundidad,
                "Resultado": resultado,
                "resultado2" : resultado2 # <--- Se guarda el resultado aquí
            })
            
            actualizar_lista()
            ventana_registro.destroy()
            messagebox.showinfo("Éxito", "Pallet registrado exitosamente")
            
            # Se corrige la forma de mostrar el resultado en el messagebox. 
            # Se usa el resultado calculado (resultado) y se une con el texto.
            messagebox.showinfo("Resultado del Cálculo", f"El número de elementos en tu pallet es de: {resultado} und y su peso es de {resultado2}")
            
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

    # Botón para registrar el usuario en la ventana secundaria
    boton_agregar = tk.Button(ventana_registro, text="Registrar y Calcular", command= agregar_usuario)
    boton_agregar.pack(pady=10)

# Etiqueta para la lista de usuarios
label_lista = tk.Label(raiz, text="Lista de Pallets Registrados:")
label_lista.pack(pady=10)

# Listbox para mostrar los usuarios registrados 
listbox_usuarios = tk.Listbox(raiz, width=60, height=20)
listbox_usuarios.pack(pady=5)

# Botón para abrir la ventana de registro
boton_abrir = tk.Button(raiz, text="Abrir Registro de Pallet", command=abrir_ventana_registro)
boton_abrir.pack(pady=20)

# Iniciar el bucle principal de la ventana
raiz.mainloop()
