"""""
x=7//3
y = 7%3
print (x,y)


def square(x):
    return x **2
print (square(4))
def func():
    return 5+2 
print(func(3))

x= True+5
print (x)

def greet(name="world"):
    return "hello, "+ name
print(greet("alice"))
def saludaor(nombre):
    return"hola, "+nombre
print(saludaor("mundo"))

a="hello"
b="world"

def func(x):
    return x*x
print (func())


x=10/3

print(x)






Agenda_Fernando = {
    "04:00 pm": "Sumergirme en mi propia miseria",
    "04:30 pm": "Contemplar el abismo",
    "05:00 pm": "Solucionar la hambruna mundial sin decírselo a nadie",
    "05:30 pm": "Danza y ejercicio",
    "06:30 pm": "Cena conmigo. Esa no la cancelaré",
    "07:00 pm": "Luchar con el odio que me tengo"
}
print(Agenda_Fernando)

num=int(input("Ingrese un numero: "))




if((num%2==0)):
    print("el numero es par")

else:
    print("el numero es impar")
"""""


num1=int(input("digita un numero: "))

num2=int(input("digita un numero: "))

num3=int(input("digita un numero: "))

if(num1>num2>num3):
    print(f"el mayor de los numeros es :{num1}")


elif(num1==num2==num3):
    print(f"todos los  numeros son iguales")

else:
    print(f"el mayor de los numeros es :{num2}")

