from datetime import datetime

intentos = {}

with open("eventos.log", "r", encoding="utf-8") as archivo:

    for linea in archivo:

        fecha, tipo, usuario = linea.strip().split(",")

        if tipo == "LOGIN_FALLIDO":

            if usuario not in intentos:
                intentos[usuario] = []

            intentos[usuario].append(fecha)

for usuario, registros in intentos.items():

    if len(registros) >= 3:

        print("ALERTA DE SEGURIDAD")
        print("Usuario:", usuario)
        print("Intentos fallidos:", len(registros))
        print("Primer intento:", registros[0])
        print("Detección:", registros[2])

        inicio = datetime.strptime(registros[0], "%Y-%m-%d %H:%M:%S")
        deteccion = datetime.strptime(registros[2], "%Y-%m-%d %H:%M:%S")

        mttd = (deteccion - inicio).total_seconds()
        
        print("MTTD:", mttd, "segundos")