#EJERCICIO 1
p_int=float(input("Ingrese el porcentaje de intereses: "))
cap=int(input("Ingrese la capital invertida: "))
intereses=cap*p_int
if intereses>7000:
    capf=cap+intereses
    print(f"Usted tiene en su cuenta ${capf} pesos.")
else:
    print("Los intereses son menores a 7.000")
#EJERCICIO 2
cal1=int(input("Ingrese su calificación 1: "))
cal2=int(input("Ingrese su calificación 2: "))
cal3=int(input("Ingrese su calificación 3: "))
prom=(cal1+cal2+cal3)/3
if prom>=70:
    print("El alumno aprobó el curso")
else:
    print("El alumno reprobó el curso")
#EJERCICIO 3
compra=int(input("Ingrese el valor de su compra: "))
if compra>1000:
    desc=compra*0.20
else: 
    desc=0
tot_pag=compra-desc
print(f"El total a pagar por su compra es de ${tot_pag} pesos")
#EJERCICIO 4
horas_t=int(input("Ingrese las horas trabajadas: "))
if horas_t>40:
    horas_e=horas_t-40
    sal_sem=(((horas_e*20)+40)*16)
else:
    sal_sem=horas_t*16
print(f"Su salario semanal es de ${sal_sem} pesos")
#EJERCICIO 6
num1=int(input("Ingrese el número 1: "))
num2=int(input("Ingrese el número 2: "))
if num1>num2:
    print(f"\n El {num1} es mayor que el {num2}")
elif num1<num2:
    print(f"\n El {num2} es mayor que el {num1}")