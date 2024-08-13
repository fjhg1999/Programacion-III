#while
"""""
i=0
while i<99999999999:
    print(f"vamor por el {i}")
    i+=99999999

valor= int(input("ingrese un numero "))
i=1
while (i<=valor):
    print(i)
    i+=1

while True:
    contador = 1
    numero=int(input("ingrese un numero: "))
    while contador <= 10:
        resultado = numero * contador
        print(f"{numero}x {contador} = {resultado}")
        contador += 1
        opt=int(input("seleciona una opcion  1-ingresar otro numero 2-salir"))
        
        if(opt==1):
                continue
        elif(opt==2):
                break
    """""


while True:
    usuario="Masca"
    contra="hola123"
    user=input("ingrese su usuario: ")
    if usuario==user:
        print("bienvenido:  ")
        print("ingrese su contrasena")
        
    
        
    else: (print("usuario incorrecto: "))




