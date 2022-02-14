# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("¡No se encontro el archivo de configuración!")


# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("¡No se encontro el archivo de configuración!")

# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         open('config.txt')
#     except FileNotFoundError:
#         print("¡No se encontro el archivo de configuración!")
#     except IsADirectoryError:
#         print("Se encontro el archivo config.txt, pero no se puede leer")

## En este ejercicio anterior no se logro abrir el archivo config.txt, imagino que IsADirectoryError busca una carpeta y no un archivo.

# if __name__ == '__main__':
#     main()

# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("¡No se encontro el archivo de configuración!")
#     except IsADirectoryError:
#         print("Se encontro el archivo config.txt, pero no se puede leer")
#     except (BlockingIOError, TimeoutError):
#         print("El sistema de navegación esta sobrecargado, no se puede terminar de leer el archivo de configuración")

# if __name__ == '__main__':
#     main()

def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("No se encontro el archivo config.txt")
        elif err.errno == 13:
            print("Se encontro el archivo config.txt, pero no se pudo abrir")

if __name__ == '__main__':
    main()