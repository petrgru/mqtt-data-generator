import paho.mqtt.client as paho
import json
import time

from data_generator.mqtt_gen import generate_sensor_data
    
env = "local"
# local, remote


with open('mqtt-config.json') as f:
    conf = json.load(f)
    print(f"Configuration: {conf[env]}")

    MQTT_SERVER = conf[env]['mqtt.server']
    MQTT_PORT = conf[env]['mqtt.port']
    MQTT_CLIENT_ID = conf[env]['mqtt.client.id']
    MQTT_TOPIC = conf[env]['mqtt.topic']
    MQTT_REQUIRE_LOGIN = conf[env]['mqtt.require.login']
    MQTT_USER = conf[env]['mqtt.user']
    MQTT_PASS = conf[env]['mqtt.pass']
    MQTT_TLS = conf[env]['mqtt.tls']


def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"Connected with reason code: {reason_code}")
 

def main():
    sensors = generate_sensor_data(100)

    #print(tags)

    client = paho.Client(paho.CallbackAPIVersion.VERSION2, client_id='generator-client-1')
    if MQTT_REQUIRE_LOGIN: client.username_pw_set(username=MQTT_USER, password=MQTT_PASS)

    # register callbacks
    client.on_connect = on_connect

    if MQTT_TLS: client.tls_set()
    print(f"Connecting to the MQTT server {MQTT_SERVER} on port {MQTT_PORT}")
    client.connect(MQTT_SERVER, MQTT_PORT) 
    client.loop_start()

    topic = MQTT_TOPIC

    try:
        for sensor in sensors:
            result = client.publish(topic, json.dumps(sensor).encode('utf-8'))
            print(f"Published with result: {result} \n{sensor}")
            time.sleep(1)  
    except KeyboardInterrupt:
        pass  
    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == '__main__':
    main()