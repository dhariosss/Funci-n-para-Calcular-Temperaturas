# Función para calcular temperaturas promedio por ciudad
def calcular_promedio_temperaturas(datos_temperaturas):
    """
    Calcula el promedio de temperaturas para cada ciudad a partir de un diccionario de datos.
    
    Parámetros:
    datos_temperaturas (dict): Diccionario con ciudades como claves y listas de temperaturas como valores
    
    Retorna:
    dict: Diccionario con ciudades como claves y sus temperaturas promedio como valores
    """
    promedios = {}
    
    # Iterar sobre cada ciudad y sus temperaturas
    for ciudad, temperaturas in datos_temperaturas.items():
        # Calcular promedio sumando temperaturas y dividiendo entre la cantidad
        if len(temperaturas) > 0:  # Verificar que haya datos
            promedio = sum(temperaturas) / len(temperaturas)
            promedios[ciudad] = round(promedio, 2)  # Redondear a 2 decimales
    
    return promedios

# Datos de ejemplo (3 ciudades, 4 semanas)
temperaturas_ciudades = {
    "QUITO": [25.5, 26.0, 24.8, 25.2],
    "CUENCA": [28.0, 27.5, 29.0, 28.2],
    "IBARRA": [22.0, 21.5, 23.0, 22.8]
}

# Prueba de la función
def probar_funcion():
    """
    Función para probar el cálculo de temperaturas promedio
    """
    print("Calculando temperaturas promedio...")
    resultados = calcular_promedio_temperaturas(temperaturas_ciudades)
    
    # Mostrar resultados
    for ciudad, promedio in resultados.items():
        print(f"Temperatura promedio de {ciudad}: {promedio}°C")

# Ejecutar la prueba
if __name__ == "__main__":
    probar_funcion()

    
temperaturas = [
    # Santo Domingo	
    [
        # Semana 1
        [25, 26, 27, 28, 29, 30, 31],  # Lunes a Domingo
        # Semana 2
        [24, 25, 26, 27, 28, 29, 30],
        # Semana 3
        [23, 24, 25, 26, 27, 28, 29],
        # Semana 4
        [22, 23, 24, 25, 26, 27, 28]
    ],
    # Cuenca 
    [
        # Semana 1
        [20, 21, 22, 23, 24, 25, 26],
        # Semana 2
        [19, 20, 21, 22, 23, 24, 25],
        # Semana 3
        [18, 19, 20, 21, 22, 23, 24],
        # Semana 4
        [17, 18, 19, 20, 21, 22, 23]
    ],
    # Quito 
    [
        # Semana 1
        [30, 31, 32, 33, 34, 35, 36],
        # Semana 2
        [29, 30, 31, 32, 33, 34, 35],
        # Semana 3
        [28, 29, 30, 31, 32, 33, 34],
        # Semana 4
        [27, 28, 29, 30, 31, 32, 33]
    ]
]

# Nombres de las ciudades
ciudades = ["Santo Domingo", "Cuenca", "Quito"]

for i in range(len(ciudades)):  # Iterar sobre ciudades
    print(f"Promedios de temperatura para {ciudades[i]}:")
    for j in range(len(temperaturas[i])):  # Iterar sobre semanas
        semana = temperaturas[i][j]
        promedio = sum(semana) / len(semana)
        print(f"  Semana {j + 1}: {promedio:.2f}°C")
    print() 