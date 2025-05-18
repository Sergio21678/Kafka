from kafka import KafkaConsumer

consumer = KafkaConsumer('mi-topico', bootstrap_servers='localhost:9092')
print("Esperando mensajes...")
for message in consumer:
    print(f"Mensaje recibido: {message.value.decode()}")
