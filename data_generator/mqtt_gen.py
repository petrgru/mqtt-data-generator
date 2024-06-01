from faker import Faker


def generate_sensor_data(num): 
    fake = Faker()
    sensors = [{
        'event_id': fake.uuid4(), 
        'event_time': fake.iso8601(),
        'sensor_id': fake.mac_address(),
        'sensor_name': 'test' + str(fake.pyint(100, 999)),
        'sensor_type': 'gps',
        'latitude': str(fake.latitude()),
        'longitude': str(fake.longitude())
    } for x in range(num)]
    return sensors