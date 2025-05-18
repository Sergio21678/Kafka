from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'hola-mundo',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='test-group'
)

print("Esperando mensajes...")
for mensaje in consumer:
    print(f"Recibido: {mensaje.value.decode('utf-8')}")
