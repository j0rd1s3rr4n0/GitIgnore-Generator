import argparse
import requests
import webbrowser

def generate_gitignore(frameworks, output_path):
    frameworks_str = ','.join(frameworks)
    
    url = f"https://www.toptal.com/developers/gitignore/api/{frameworks_str}"
    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        file_name = ".gitignore"
        if output_path:
            file_path = f"{output_path}/{file_name}"
        else:
            file_path = file_name

        with open(file_path, "w") as file:
            file.write(content)
            print(f"Archivo .gitignore generado y guardado en '{file_path}'.")
    else:
        print("Se ha producido un inconveniente durante la generación del archivo .gitignore.\nPor favor, verifique su conexión a Internet para continuar.")

def show_credits():
    webbrowser.open("https://github.com/j0rd1s3rr4n0")

def main():
    parser = argparse.ArgumentParser(description="Generador de .gitignore")
    parser.add_argument("-l", "--list", action="store_true", help="Mostrar lista de frameworks disponibles")
    parser.add_argument("-f", "--frameworks", nargs='+', help="Frameworks para generar el .gitignore")
    parser.add_argument("-r", "--ruta", help="Ruta donde guardar el archivo .gitignore")
    parser.add_argument("-c", "--credits", action="store_true", help="Abrir URL de los créditos")

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    if args.list:
        print("Frameworks disponibles:")
        response = requests.get("https://www.toptal.com/developers/gitignore/api/list?format=lines")
        frameworks_list = response.text.split('\n')
        for framework in frameworks_list:
            print('[+]',framework)

    if args.frameworks:
        generate_gitignore(args.frameworks, args.ruta)

    if args.credits:
        show_credits()

if __name__ == "__main__":
    main()
