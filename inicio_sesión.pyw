import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  
from Menu import Menu

class Sesion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.usuario = ""
        self.contraseña = ""
        self.geometry("500x300")  
        self.resizable(False, False)
        self.configure(bg="#40E0D0")  
        self.title("Inicio de Sesión")

        ruta_imagen = 'C:/Users/lauta/TesisPeluqueria/TesisPeluqueria/Interfaces de la peluqueria/imagen3.png'
        self.imagen = PhotoImage(file=ruta_imagen)
        
        self.label_imagen = tk.Label(self, image=self.imagen,bg=self.cget('bg'))
        self.label_imagen.grid(row=2, column=1, rowspan=3, padx=20, pady=40)
        
        self.etiqueta1 = tk.Label(self, text="Usuario", font=("Calibri", 20), bg=self.cget('bg'), fg="black")
        self.etiqueta1.grid(row=0, column=0, padx=20, pady=20)
        self.etiqueta2 = tk.Label(self, text="Contraseña", font=("Calibri", 20), bg=self.cget('bg'), fg="black")
        self.etiqueta2.grid(row=1, column=0, padx=20, pady=20)

        self.mostrador_usuario = tk.Entry(self, state="normal", font=("Calibri", 15))
        self.mostrador_usuario.grid(row=0, column=1, padx=20, pady=20)
        self.mostrador_contraseña = tk.Entry(self, show="*", state="normal", font=("Calibri", 15))
        self.mostrador_contraseña.grid(row=1, column=1, padx=20, pady=20)

        self.boton = tk.Button(self, text="Ingresar", command=self.verificar_sesion, font=("Calibri", 12))
        self.boton.grid(row=2, column=1, padx=10, pady=1)

        self.boton_registro = tk.Button(self, text="Registrarse", command=self.abrir_registro, font=("Calibri", 12))
        self.boton_registro.grid(row=3, column=1, padx=10, pady=1)

    def abrir_registro(self):
        self.registro = Registro(self)
        self.registro.mainloop()

    def verificar_sesion(self):
        usuario_ingresado = self.mostrador_usuario.get()
        contraseña_ingresada = self.mostrador_contraseña.get()

        if usuario_ingresado == self.usuario and contraseña_ingresada == self.contraseña:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")  
            self.abrir_menu_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")  

    def abrir_menu_principal(self):
        self.destroy()  # Cierra la ventana de inicio de sesión
        menu = Menu()  # Abre el menú principal desde el otro archivo
        menu.mainloop()

class Registro(tk.Tk):
    def __init__(self, master):
        super().__init__()

        self.master = master
        self.geometry("300x200")  
        self.resizable(False, False)
        self.configure(bg="#40E0D0")  
        self.title("Registro de Usuarios")

        self.etiqueta1 = tk.Label(self, text="Usuario", font=("Calibri", 15), bg=self.cget('bg'), fg="black")
        self.etiqueta1.grid(row=0, column=0, padx=20, pady=20)
        self.etiqueta2 = tk.Label(self, text="Contraseña", font=("Calibri", 15), bg=self.cget('bg'), fg="black")
        self.etiqueta2.grid(row=1, column=0, padx=20, pady=20)

        self.mostrador_usuario = tk.Entry(self, state="normal", font=("Calibri", 12))
        self.mostrador_usuario.grid(row=0, column=1, padx=20, pady=20)
        self.mostrador_contraseña = tk.Entry(self, show="*", state="normal", font=("Calibri", 12))
        self.mostrador_contraseña.grid(row=1, column=1, padx=20, pady=20)

        self.boton_registro = tk.Button(self, text="Registrarse", command=self.registrar_usuario, font=("Calibri", 10))
        self.boton_registro.grid(row=2, column=1, padx=10, pady=1)

    def registrar_usuario(self):
        username = self.mostrador_usuario.get()
        password = self.mostrador_contraseña.get()

        # Check if the username and password are not empty
        if username and password:
            # You can add additional validation or encryption here
            print(f"User {username} registered successfully!")
            # Store the new user credentials (e.g., in a database or file)
            # For simplicity, I'm storing them as instance variables
            self.master.usuario = username
            self.master.contraseña = password
            messagebox.showinfo("Éxito", "Registro exitoso")
            self.destroy()  # Close the registration window
        else:
            messagebox.showerror("Error", "Please enter a valid username and password.")

ventana = Sesion()
ventana.mainloop()