from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('mi-topico', b'Hola mundo')
producer.flush()
print("Mensaje enviado.")
