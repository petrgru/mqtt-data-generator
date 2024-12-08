# for pernament running

docker compose build

docker compose up

listen on localhost 1883


# MQTT Data Generator
This is a simple self-contained MQTT solution designed to generate randomized sample data and publish it to a MQTT broker. The data is generated using the [Faker](https://pypi.org/project/Faker/) library, and then published to a specified topic in the MQTT broker.


## Features
- Host a Mosquitto MQTT broker with Docker Compose
- Generate randomized sample data using Faker library
- Publish the sample data to a specified topic in the MQTT broker
- Subscribe to the topic and print out the received messages


*Data generation, publishing, and subscribing can be configured to inteface with the contained dockerized MQTT broker or with an external MQTT broker.*


## Requirements
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker Compose](https://docs.docker.com/compose/) if using the dockerized MQTT broker


## Project Setup
### Local w/ Dockerized MQTT Broker
1. Install Python dependencies using `pip install -r requirements.txt`
2. Run the MQTT broker using `docker-compose up -d`


### Setup w/o Dockerized MQTT Broker
1. Install Python dependencies using `pip install -r requirements.txt`
2. Configure the MQTT broker in `mqtt-config.json`


## Testing the MQTT broker
To test the MQTT broker, you can use the `paho_subscribe.py` script. This script will connect to the MQTT broker and subscribe to the topic specified in the `mqtt-config.json` file. It will print out the messages received from the broker.

```
python paho_subscribe.py
```

In a separate terminal, run the `paho_generator.py` script to generate randomized sample data and publish it to the MQTT broker.

```
python paho_generator.py
```


## Other Configuration Options
- `mosquitto/config/mosquitto.conf` - Moquitto MQTT dockerized broker configuration file
- `data_generator/mqtt_gen.py` - Faker data generator script


### Python Dependencies
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)
- [faker](https://pypi.org/project/Faker/)
