# def main():
#     open("/path/to/mars.jpg")

# if __name__ == '__main__':
#     main()

def main():
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("Hubo un problema abriendo el archivo:", err)

if __name__ == '__main__':
    main()