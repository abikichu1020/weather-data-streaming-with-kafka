import json
import time
import psycopg2
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

KAFKA_TOPIC = "weather"
KAFKA_SERVER = "kafka:9092"

DB_CONFIG = {
    "host": "postgres",
    "dbname": "weatherdb",
    "user": "user",
    "password": "password",
    "port": 5432
}

def connect_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPIC,
                bootstrap_servers=[KAFKA_SERVER],
                value_deserializer=lambda v: json.loads(v.decode("utf-8")),
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                group_id="weather-group"
            )
            print("Consumer connected to Kafka")
            return consumer
        except NoBrokersAvailable:
            print("Kafka not ready, retrying in 5 seconds...")
            time.sleep(5)

def connect_postgres():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.autocommit = True
            print("Connected to PostgreSQL")
            return conn
        except Exception as e:
            print("PostgreSQL not ready, retrying in 5 seconds...", e)
            time.sleep(5)

consumer = connect_kafka()
conn = connect_postgres()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature FLOAT,
        condition TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

for message in consumer:
    weather = message.value
    try:
        city = weather["location"]["name"]
        temp = weather["current"]["temp_c"]
        condition = weather["current"]["condition"]["text"]

        cur.execute(
            "INSERT INTO weather_data (city, temperature, condition) VALUES (%s, %s, %s)",
            (city, temp, condition)
        )

        print(f"Inserted weather data: {city}, {temp}°C, {condition}")

    except KeyError:
        print("Invalid weather message format:", weather)

    except Exception as e:
        print("Database insert error:", e)
        time.sleep(2)
