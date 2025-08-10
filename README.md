mi primer proyecto de python soy aprendiz eh visto muchos videos y 
\n leido informacion para tratar de entender y captar la informacion necesaria buscando 
\n significados de cada comando usado
# El indice de masa corporal IMC se puede calcular con el peso en kg de una persona entre la estatura en metros al cuadrado (IMC = peso (kg) / altura (m²))
# Bajo peso: IMC inferior a 18.5
# Peso normal (saludable): IMC entre 18.5 y 24.9
# Sobrepeso: IMC entre 25 y 29.9
# Obesidad: IMC de 30 o más 


# calculadoraIMC  valida la entrada de los datos para evitar errores
calculadora IMC para control de peso
lenguaje --python 3.13--

# Modelo para calcular el Indice de Masa Corporal (IMC)

# Definimos el numero de personas a evaluar el numero debe ser mayor a 0 
def obtener_datos_persona():    
    
# Solicita los datos de una persona y los devuelve.
# Maneja errores si el usuario ingresa texto en lugar de numeros.

    nombre = input("Ingresa tu nombre, por favor:  ")
    apellido = input("Ingresa tu apellido, por favor:  ")
    
# Creamos el bucle infinito para el numero de personas seleccionadas
    while True:
        try:
            edad = int(input("Ingresa tu edad:  "))
            if edad >= 18: 
                print("¡Usted es mayor de edad!")
            else:
                print("Usted es menor de edad.")
  # Como la altura es en metros y no centimetros es necesario el punto por eso es un flotante Float()
            estatura_m = float(input("Ingresa tu estatura en metros:  "))
            masa_kg = float(input("Ingresa tu peso en kilogramos:  "))
            break # Salir del bucle si los datos son correctos
        except ValueError:
            print("Error: Por favor, ingresa solo numeros para la edad, estatura y peso:")

    return nombre, apellido, edad, estatura_m, masa_kg
def calcular_y_mostrar_imc(nombre, edad, estatura, masa):
    """
    Calcula el IMC, determina la categoria y muestra el resultado.
    """
    # Formula para calcular el IMC
    imc = masa / (estatura ** 2)
    
# Se hacen las diferentes categorias
    # Logica para determinar el rango de IMC
    if imc < 15.99: 
        categoria = " Delgado severamente"
        recomendacion = " Debes alimentarte mejor, ¡por tu salud!"
    elif 16.00 <= imc <= 16.99:
        categoria = " Delgado moderadamente"
        recomendacion = "Aimentate sanamente, !acude a tu medico¡"
    elif 17.00 <= imc <= 18.49:
        categoria = " Peso bajo"
        recomendacion = "¡Casi el IMC adecuado, mejor alimentacion!"
    elif 18.50 <= imc <= 24.99:
        categoria = " Peso normal"
        recomendacion = "¡Felicidades, sigue asi!"
    elif 25.00 <= imc <= 29.99:
        categoria = " Sobre peso"
        recomendacion = "Considera visitar aun nutriologo para control."
    elif 30.00 <= imc <= 34.99:
        categoria = " Obesidad grado I"
        recomendacion= "Visita aun medico o nutriologo por tu salud"
    elif 35.00 <= imc <= 39.99:
        categoria = " Obesidad grado II"
        recomendacion = "Visita a un medico para precausiones"
    else: # imc >= 40.0
        categoria = "Obesidad de grado III (morbida)"
        recomendacion = "¡Por favor, visita a un medico para tratamiento"

    # Mostrar los resultados
    print(f"\n--- Resultados del IMC para {nombre} ---")
    print(f"Edad: {edad}")
    print(f"Tu IMC es: {imc:.2f}") # Formato para mostrar solo 2 decimales
    print(f"Categoria de IMC: {categoria}")
    print(f"Recomendacion: {recomendacion}")
# Agrego un mensaje diciendo que la informacion es basada en una fuente real
    print("\n-------------------------------------------------------------------------------------")
    print("NOTA: La informacion de los rangos de IMC esta basada, \n       en los datos proporcionados por el ISSSTE.")
    print("---------------------------------------------------------------------------------------")
# Ingreso informacion sobre las categorias de cada rango de IMC segun ISSSTE
def main():
    
    # Funcion principal para ejecutar el programa.

    print("¡Bienvenido a la calculadora de IMC!")
    print("Evalua el peso y la altura de una persona,\nayudando a determinar si su peso es saludable.")
    print("! Comenzemos !")

    while True:
        try:
            num_personas = int(input("¿Para cuantas personas deseas calcular el IMC? "))
            if num_personas > 0:
                break
            else:
                print("por favor, ingresa un numero mayor a cero.")
        except ValueError:
            print("Error; Ingresa un numero valido.")

    for _ in range(num_personas):
        print("\n--- Ingresa los datos de la persona ---")
        nombre, apellido, edad, estatura, masa = obtener_datos_persona()
        calcular_y_mostrar_imc(f"{nombre} {apellido}", edad, estatura, masa)

if __name__ == "__main__":
    main()
    
 # Estos son mis comados que utilize en lenguaje --python 3.13-- la verdad me costo mucho trabajo ya que al comienzo no me daba me marcaba error ya que no podia cerrar el bucle para la configuracion de num de personas
# Las contribuciones y opinones son bienvenidas para mejorar o reportar alguna falla o error no duden en hacermelo saber

# Autora
*** Cinthya Vanessa Castillo Mendez ***
