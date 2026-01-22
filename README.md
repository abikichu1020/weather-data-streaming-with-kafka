# Weather Data Streaming using Kafka and Weather API

## Project Title
Real-Time Weather Data Streaming using Apache Kafka

## Project Folder
weather-data-streaming-with-kafka

## Objective
The objective of this project is to demonstrate real-time data streaming using Apache Kafka by fetching live weather data from a Weather API and streaming it between a producer and consumer application. This project showcases how Kafka can be used for event-driven architectures and real-time data pipelines.

## Description
This project implements a real-time data streaming pipeline where weather data is continuously fetched from an external Weather API and published to a Kafka topic by a producer. A Kafka consumer subscribes to the same topic and processes the incoming weather data.

Docker and Docker Compose are used to containerize Kafka, Zookeeper, and the Python applications, ensuring easy setup and portability.

The project simulates a real-world streaming use case such as live monitoring, analytics, or ingestion into downstream systems.

## Project Structure
- docker-compose.yml : Defines Kafka and Zookeeper services
- Dockerfile : Builds the Python application container
- requirements.txt : Python dependencies
- weather-producer.py : Kafka producer that fetches and publishes weather data
- weather-consumer.py : Kafka consumer that reads and displays weather data

## Technologies Used
- Apache Kafka
- Zookeeper
- Python
- Docker
- Docker Compose
- Weather API (REST API)

## Data Flow
1. Weather API provides live weather data
2. Producer fetches weather data at regular intervals
3. Producer publishes data to a Kafka topic
4. Kafka broker handles message streaming
5. Consumer subscribes to the topic
6. Consumer processes and displays weather data

## Kafka Components
- Kafka Broker
- Zookeeper
- Topic-based messaging
- Producer and Consumer model

## Libraries Used
- kafka-python
- requests
- json
- time

## Docker Services
- Zookeeper
- Kafka Broker
- Python application container

## Features
- Real-time data ingestion
- Producer-consumer architecture
- Containerized deployment
- Scalable streaming pipeline
- Fault-tolerant messaging system

## Use Cases
- Real-time weather monitoring
- Streaming analytics
- IoT data pipelines
- Event-driven systems
- Data engineering practice projects

## How to Run
1. Install Docker and Docker Compose
2. Navigate to the project directory
3. Update the Weather API key in weather-producer.py
4. Run the following command:
   docker-compose up --build
5. Kafka producer starts fetching and sending weather data
6. Kafka consumer starts receiving and displaying data

## Output
- Continuous streaming of weather data in JSON format
- Logs showing producer publishing messages
- Logs showing consumer receiving messages

## Advantages
- Real-time processing
- Scalable architecture
- Decoupled producer and consumer
- Easy deployment using Docker

## Limitations
- Depends on external Weather API availability
- Basic error handling
- No persistent storage implemented

## Conclusion
This project demonstrates a complete real-time data streaming pipeline using Apache Kafka and a Weather API. It provides hands-on experience with Kafka producers, consumers, Docker-based deployment, and real-world streaming data concepts essential for data engineering and distributed systems.

## Author
Developed as part of a data streaming and big data practical implementation.
