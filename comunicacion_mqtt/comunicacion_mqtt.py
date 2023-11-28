import paho.mqtt.client as mqtt

class comunicacion_mqtt():
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        try:
            self.client.connect(self.broker, self.port, 60)
        except Exception as e:
            print(f"Error al conectar al broker MQTT: {str(e)}")
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conexión exitosa al broker MQTT")
            client.subscribe("datos-salida")
            client.loop_start()
        else:
            print(f"Fallo en la conexión al broker. Código de retorno={rc}")

    def on_message(client, userdata, msg):
        print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")
    
    def publicar(self, topic, payload):
        self.client.publish(topic, payload)
        print(f"Mensaje publicado en el tema {topic}: {payload}")