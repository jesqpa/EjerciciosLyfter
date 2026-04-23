notes = int(input("Defina cantidad de notas: "))
approveds=0
disapproveds=0
total_sum = 0
approveds_sum = 0
disapproveds_sum = 0

for cant in range(notes):
    value = int(input(f"Indica la nota {cant+1}: "))
    total_sum = total_sum + value
    if(value>=70):
        approveds = approveds + 1
        approveds_sum = approveds_sum + value
    else :
        disapproveds = disapproveds + 1
        disapproveds_sum = disapproveds_sum + value

print(f"Tiene {approveds} notas aprobadas")
print(f"Tiene {disapproveds} notas desaprobadas")
print(f"El promedio de todas es {total_sum/notes} ")

if(approveds>0):
    print(f"El promedio de aprobadas es {approveds_sum/approveds} ")
else : 
    print("No hay notas aprobadas")

if(disapproveds>0):
    print(f"El promedio de desaprobadas es {disapproveds_sum/disapproveds} ")
else :
    print("No hay notas desaprobadas")




