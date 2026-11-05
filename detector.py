from datetime import datetime

def registrar_respuesta(usuario):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("respuestas.log", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha},USUARIO_BLOQUEADO,{usuario}\n")

    return fecha    

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

        fecha_respuesta = registrar_respuesta(usuario)

        inicio = datetime.strptime(
            registros[0], 
            "%Y-%m-%d %H:%M:%S"
        )

        deteccion = datetime.strptime(
            registros[2],
            "%Y-%m-%d %H:%M:%S"
        )

        respuesta = datetime.strptime(
            fecha_respuesta,
            "%Y-%m-%d %H:%M:%S"
        )

        mttr = (respuesta - deteccion).total_seconds()
        print("MTTR:", mttr, "segundos")

        mttd = (deteccion - inicio).total_seconds()
        print("MTTD:", mttd, "segundos")

        print("Acción aplicada: bloqueo de usuario")
        print("Respuesta:", fecha_respuesta)

        inicio = datetime.strptime(registros[0], "%Y-%m-%d %H:%M:%S")
        deteccion = datetime.strptime(registros[2], "%Y-%m-%d %H:%M:%S")

        mttd = (deteccion - inicio).total_seconds()
        
        print("MTTD:", mttd, "segundos")

        #primer caso de prueba: MTTR:3066.0 segundos y MTTD:25.0 segundos para el usuario "usuario_01"
        #segundo caso de prueba: MTTR:12.0 segundos y MTTD:18.0 segundos para el usuario "usuario_02"
        #tercer caso de prueba: MTTR:10.0 segundos y MTTD:26.0 segundos para el usuario "usuario_03"
        #MTTR promedio: (3066.0 + 12.0 + 10.0) / 3 = 1029.33 segundos
        #MTTD promedio: (25.0 + 18.0 + 26.0) / 3 = 23.0 segundos