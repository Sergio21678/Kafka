from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'hola-mundo'

for i in range(5):
    mensaje = f"Mensaje {i}".encode('utf-8')
    producer.send(topic, mensaje)
    print(f"Enviado: {mensaje}")

producer.flush()
