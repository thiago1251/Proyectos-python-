masa = input(" ¡HI! Let's calculate your Body Mass Index (BMI)  Please, write your weight in Kg ")
altura = input("let's continue with your height in m ")
elevado = pow(float(altura), 2)
imc = int(masa)/elevado
print("Your Body Mass Index (BMI) is: " + str(imc))