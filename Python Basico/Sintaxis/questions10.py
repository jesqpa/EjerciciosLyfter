time_seconds = int(input("Indica tiempo en segundos: "))
time_minutes = time_seconds/60

if(time_minutes<10):
    print(f"Segundos para llegar a 10 minutos: {600-time_seconds}")
elif(time_minutes==10) :
    print("Igual")
else :
    print("Mayor")


