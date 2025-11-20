import os
os.system("cls")

usuarios={}
sexos={}
contraseñas={}


def ingresar_usuario():
    nombre=input("Ingrese el nombre del usuario: ")
    if nombre not in usuarios:
        usuarios.append(nombre)
    else:
        print("Usuario repetido")

    sexo=input("Ingrese sexo: ").upper()
    if sexo =="F" or sexo=="M":
        sexos.append(sexo)
    else:
        print("Ingrese F o M")

    contraseña=input("Ingrese contraseña: ")
    if contraseña is not len(8):
        print("La contraseña debe tener 8 carácteres")
    elif " " in contraseña:
        print("La contraseña no debe tener espacios en blanco")
    elif not (contraseña).isdigit:
        print("Debe tener un valor numérico") 
    else:
        contraseñas.append(contraseña)
        return

def buscar_usuario():
    usuario=input("Ingrese usuario a buscar: ")
    if " " in usuario:
            print("El usuario no puede tener espacios en blanco")
    elif usuario in usuarios:
        print(f"Usuario: {usuario}")
        print(f"sexo: {sexos}")
        print(f"contraseña: {contraseñas}")

def eliminar_usuario():
    usuario=input("Ingrese el usuario a eliminar: ")
    for usuario in usuarios:
        if usuario in usuarios:
            usuarios.remove(usuario)
            print("Usuario eliminado!")
        if usuario not in usuarios:
            print("No se pudo eliminar el usuario!")

def salir():
    print("Programa terminado...")


def mostrar_menu():
    if opcion==1:
        ingresar_usuario()
    elif opcion==2:
        buscar_usuario()
    elif opcion==3:
        eliminar_usuario()
    elif opcion==4:
        salir()
try:
    opcion=int(input("Ingrese una opción: "))
except ValueError:
    print("Debe ingresar una opción válida!!")

