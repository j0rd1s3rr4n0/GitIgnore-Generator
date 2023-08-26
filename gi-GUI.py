import tkinter as tk
import requests
from tkinter import filedialog
from tkinter import ttk
import webbrowser

def generate_gitignore():
    selected_frameworks = listbox.curselection()
    selected_frameworks_names = [frameworks_list[index] for index in selected_frameworks]
    frameworks_str = ','.join(selected_frameworks_names)
    
    url = f"https://www.toptal.com/developers/gitignore/api/{frameworks_str}"
    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        save_path = filedialog.asksaveasfilename(initialfile=".gitignore",defaultextension=".gitignore", filetypes=[("Gitignore files", "*.gitignore")])
        if save_path:
            with open(save_path, "w") as file:
                file.write(content)
                show_message("Éxito", "Archivo .gitignore generado y guardado.")
        else:
            show_message("Advertencia", "No se seleccionó una ubicación de guardado.")
    else:
        show_message("Error", "Hubo un problema al generar el archivo .gitignore.")

def open_google():
    webbrowser.open("https://github.com/j0rd1s3rr4n0")

def show_message(title, message):
    message_window = tk.Toplevel(window)
    message_window.title(title)
    
    label = tk.Label(message_window, text=message, padx=20, pady=10)
    label.pack()
    
    ok_button = tk.Button(message_window, text="OK", command=message_window.destroy)
    ok_button.pack(pady=5)

# Obtener la lista de frameworks desde la URL
response = requests.get("https://www.toptal.com/developers/gitignore/api/list?format=lines")
frameworks_list = response.text.split('\n')

# Configuración de la ventana
window = tk.Tk()
window.title("Generador de .gitignore")

# Agregar el icono (reemplaza 'icon.ico' con la ruta de tu archivo de icono)
window.iconbitmap('icon.ico')

# Crear un label y un combobox para seleccionar frameworks
framework_label = tk.Label(window, text="Seleccione Sistemas Operativos,IDEs, o Lenguajes de Programación:")
framework_label.pack(padx=20, pady=10)

# Crear un Listbox con scrollbar
listbox_frame = tk.Frame(window)
listbox_frame.pack(padx=20, pady=5)

listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, height=5)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for framework in frameworks_list:
    listbox.insert(tk.END, framework)

# Botón para generar .gitignore
generate_button = tk.Button(window, text="Generar .gitignore", command=generate_gitignore)
generate_button.pack(padx=20, pady=10)


google_link = tk.Label(window, text="Desarrollado por @j0rd1s3rr4n0", fg="blue", cursor="hand2")
google_link.pack(pady=5)
google_link.bind("<Button-1>", lambda e: open_google())

# Etiqueta de resultado
result_label = tk.Label(window, text="")
result_label.pack(padx=10, pady=10)

# Iniciar la interfaz
window.mainloop()
