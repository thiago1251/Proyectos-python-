precio = input(" ¡HI! Please, write the price of the product")
iva= 0.21
precioA =iva*int(precio)
precioF = int(precio) + precioA
print("The price including IVA is: $" + str(precioF) + "\n" + "Price: $ " + str(precio) + "\n" + "IVA: $ " + str(precioA))