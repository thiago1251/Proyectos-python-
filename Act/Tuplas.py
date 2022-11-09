t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')
print (t) #imprime el arreglo
print (len(t)) #Cuenta la cantidad de objetos que hay en la tupla


print ('=====================================')
print (t[0]) #Imprime el primer valor de la tupla
print (t[3]) #Imprime el cuarto valor de la tupla
print (t[1:3]) #Imprime el segundo y cuarto valor de la tupla
print (t[3][1]) #Imprime el segundo valor que hay dentro del cuarto objeto de la tupla


print ('====================================')
print (t[3]) #Imprime el tercer objeto de la tupla
t[3].append('lorito') #agrega un valor al tercer objeto de la tupla, en este caso 'lorito'
print (t) #Imprime la tupla modificada

print ('====================================')
for elemento in t:
    print (elemento) #Imprime cada uno de los valores de la tupla en lineas separadas

print ('====================================')
for index in range(0,len(t)):
    print (t[index])  #Imprime los valores hasta el valor específicado

print ('====================================')
if 'a' in t:
    print ("El elemento 'a' esta en la tupla") #Si hay un valor 'a' en el arreglo, se imprime la línea

print ('====================================')
lista=list(t) #transforma la tupla en una lista
lista[1]='A'  #reemplaza segundo valor de la lista por una A
print (lista) #se imprime la lista

tupla=tuple(lista) #cambia la lista a una tupla
print (tupla) #Imprime la tupla

print ('====================================')
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]
for x, y in l:
    print (x, ':', y) #Para cada tupla, asigna los dos valores dentro de cada parentesis como x y y
    #, y agrega un ':' en medio de los valores