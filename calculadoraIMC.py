# Defino el numero de personas que quiero procesar
num_personas_a_calcular= int(input( "Num_personas:  "))
# Verifico numero de personas que sea mayor a 0
print()
# pido ingresen sus datos personales
palabra = ("hola bienvenido a tu consulta de IMC") # Una bienvenida para estimular la alegria
print("Hola bienvenido a tu consulta de IMC")
print() # Realizo print sin palabra para dejar un espacio
palabra = ("Es importate conocerlo para tener un peso adecuado por salud") # Una informacion importante
print("Es importante conocerlo para tener un peso adecuado por salud")
print() # ingreso prin sin palabras para tener un espacio y no se vea saturado
palabra = ("Comenzemos") # Un comentario de entrada
print("¡Comenzemos!")
# se me hizo comodo poner 2 print sin palabra para tener un espacio por que se me parecia muy saturado
print()
print()
# Aqui pido ingresar los datos por favor para evitar estar repitiendo lo mismo cada renglon
print("Ingrese los siguientes datos por favor...")
# Se pide ingresar nombre capturado con input para su correcta captura
nombre = input("Nombre o nombres:  ")
# se pide ingrese apellido para hacer mas completo el formulario con input para su captura
apellido = input("Apellidos:  ")
# Aqui se ingresa edad como es numero entero se pone int()
edad = int(input("Edad:  "))
# aqui se ingresa float por ser con numeros decimales
estatura = float(input("Altura: "))
# aqui tambien ingrese float por si ponen numero decimal en sus kilos
masa = float(input("Peso en Kilogramos: "))
print() # Dejo espacio para evitar saturar la vista
IMC = masa / estatura ** 2 # Formula para calcular IMC masa entre altura al cuadrado
# Al capturar la edad se realizara la especificaion si es menor o mayor de edad
if edad >= 18 :
    print("¡Usted es mayor de edad!")

else:
    print("¡Usted es menor de edad!")
print() # dejo espacio para no saturar la vista
# Despues de confirmar eda se proporciona el indice de masa corporal para que vea su realidad
print("IMC: " + str(IMC) )
# Se proporciona los distintos rango de IMC segun las fuentes del ISSTE
if IMC >= 0 and IMC <= 15.99 :
    print("Delgado severamente")

elif IMC >= 16.00 and IMC <= 16.99 :
    print("Delgado moderado")

elif IMC >= 17.00 and IMC <= 18.49 :
    print("Delgado levemente")

elif IMC >= 18.50 and IMC <= 24.99 :
    print("Normal ¡FELICIDADES! sigue asi")

elif IMC >= 25.00 and IMC <= 29.99 :
    print("Usted tiene ¡Sobrepeso!, consulte un Nutriologo para control")

elif IMC >= 30.00 and IMC <= 34.99 :
    print("Tienes nivel ¡Leve de obesidad!, visite un Nutriologo por ¡Salud!")

elif IMC >= 35.00 and IMC <= 39.00 :
    print("Tiene Obesidad media, visite a su Medico por precaucion")

elif IMC >= 40.00 :
    print("¡Tiene Obesidad morvida!, ¡Por Favor! visita a tu Medico para tratamiento")
print() # espacio para evitar saturar de informacion
print("Los rangos de IMC son proporcionados por el ISSTE") # comentario para que se corrobore informacion
print("Siempre pensando en su salud acuda a un medico de confianza") # comentario extra
