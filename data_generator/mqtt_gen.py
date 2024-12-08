from faker import Faker
from datetime import datetime

def generate_sensor_data(num): 
    fake = Faker()
    sensors = [{
        'event_id': fake.uuid4(), 
        'event_time': datetime.now().isoformat(),
        'temperature': fake.random_int(-20, 40),
        'humidity': fake.random_int(0, 100)
    } for x in range(num)]
    return sensors