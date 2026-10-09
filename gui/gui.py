import tkinter as tk 

ventana=tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("400x400")
lbl_mensaje=tk.Label(ventana, text="Hola Mundo", font=("Arial",24,"bold"))
lbl_mensaje.pack(pady=10)
ventana.mainloop()