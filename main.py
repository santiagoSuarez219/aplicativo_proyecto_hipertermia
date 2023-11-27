from ComunicacionSerial import ComunicacionSerial

vid_sensor = 0x1A86
pid_sensor = 0x7523
baud_rate_sensor = 115200

comunicacion_serial = ComunicacionSerial(vid_sensor, pid_sensor, baud_rate_sensor)
conexion = comunicacion_serial.conectar()

dato_a_enviar = "o"

# Convertir el string a bytes antes de enviarlo
dato_a_enviar_bytes = dato_a_enviar.encode('utf-8')

# Enviar el dato
conexion.write(dato_a_enviar_bytes)

# Leer la respuesta
respuesta = conexion.readline().decode('utf-8')
print(respuesta)

