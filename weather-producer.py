import json
import time
import requests
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

API_KEY = ""
CITY = "Chennai"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=yes"

def create_producer():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=["kafka:9092"],
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                retries=5
            )
            print("Producer connected to Kafka")
            return producer
        except NoBrokersAvailable:
            print("Kafka not ready, retrying in 5 seconds...")
            time.sleep(5)

producer = create_producer()

while True:
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Guard against API errors
        if "current" not in data:
            print("Weather API error response:", data)
            time.sleep(10)
            continue

        producer.send("weather", value=data)
        producer.flush()

        temp = data["current"]["temp_c"]
        print(f"Sent weather data: {CITY}, {temp}°C")

        time.sleep(10)

    except requests.exceptions.RequestException as e:
        print("Weather API request failed:", e)
        time.sleep(10)

    except Exception as e:
        print("Producer runtime error:", e)
        time.sleep(5)
