import paho.mqtt.client as paho
import time
import json


env = "local" # [local, remote]


# Load MQTT server configuration
with open('mqtt-config.json') as f:
    conf = json.load(f)
    #print(f"Configuration: {conf[env]}")

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

    client.subscribe(MQTT_TOPIC)
    

def on_message(client, userdata, message):
    print('\n')
    payload = json.loads(message.payload.decode("utf-8"))
    print(f"Topic: {message.topic}\nPayload: {payload}")


def main():
    client = paho.Client(paho.CallbackAPIVersion.VERSION2, client_id=MQTT_CLIENT_ID)
    client.username_pw_set(username=MQTT_USER, password=MQTT_PASS) if MQTT_REQUIRE_LOGIN else None
    
    # register callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    client.tls_set() if MQTT_TLS else ""
    print(f"Connecting to the MQTT broker {MQTT_SERVER} on port {MQTT_PORT}")
    client.connect(MQTT_SERVER, MQTT_PORT) 
    client.loop_start()

    try:
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == '__main__':
    main()