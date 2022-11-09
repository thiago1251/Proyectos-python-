huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'}
#Se declaran los valores


print (huespedes) #Imprime los valores
print (huespedes.items()) #Imprime los valores separados con la persona y su habitación

print (huespedes.keys()) #Imprime los números
for key in huespedes:
    print (key) #Imprime cada una de las habitaciones en lineas distintas

print (huespedes.values()) #Imprime el nombre del huesped
for key in huespedes:
    print (huespedes[key]) #Imprime cada uno de los nombres
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion]) #Imprime habitación : huesped en lineas separadas
print()
for habitacion,huesped in huespedes.items():
    print (habitacion,':',huespedes[key]) #Imprime la habitación y el último huesped
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key]) #Imprime las habitaciones ennumeradas y el huesped
print()

print (huespedes[105]) #Imprime el nombre del huesped en la habitación especificada
print (huespedes.get(105)) #Escoge el valor de la habitación

print ('====================================')

huespedes[102]='Fanny Lu'
huespedes[107]='Don Omar'
huespedes.setdefault('109','Luis Miguel') #Declara la habitación y el huesped cómo un solo valor

for huesped in huespedes.items():
    print (habitacion,':',huesped) #Imprime los nuevos huespedes y habitaciones
print()

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'}
huespedes.update(registroshoy) #Incluye los nuevos valores en el diccionario
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped) #Imprime la lista de habitaciones y huespedes entera
print()

print ('====================================')

huespedes[107]='Ricky Martin'
print (huespedes) #Imprime las habitaciones y los huespedes

print ('====================================')


del huespedes[102] #Borra el huesped de la habitacion 102
huespedes.pop(202) #Elimina del diccionario el huesped de la habitacion 202
print(huespedes) #Imprime la lista actualizada

print ('====================================')

copia1=huespedes.copy()
print ('copia1: ',copia1) #Copia los valores del diccionario
copia2={}
copia2.update(huespedes) #Inserta los valores del diccionario en el String
print ("copia2: ",copia2)

print ('====================================')

lista=[2,5,7,1]
diccio=dict.fromkeys(lista,"xxx") #Agrega "xxx" a cada uno de los valores
print(diccio)

print ('====================================')
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Moneda","Boletas"],'mecato':'Detodito','dias':1}
print (inventario) #Se crea un diccionario y se imprime
inventario["cartera"].sort()
print(inventario) #Mueve el valor "cartera" a el primer lugar
inventario["cartera"].remove("Moneda")
print(inventario) #Del diccionario "cartera" se remueve el valor "Moneda"
print(inventario.get("plata")[0]) #Se imprime el primer valor del diccionario "plata"