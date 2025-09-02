print("Hello World")
s10_A01805234
#ejercicio 1
donas =int (input("¿Cuántas donas tienes? "))
docenas=int(donas)//12
print(f"Con {donas} donas puedes hacer {docenas} docenas!")
#ejercicio 2
num1=int(input("pon un numero" ))
num2=int(input("pon otro numero"))
residuo=num1%num2
print (f"el residuo de {num1} y {num2} es {residuo}")
#ejercicio 3
segundos = int(input("Escribe una cantidad de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_final} segundos")
