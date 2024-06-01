# Clone the repository


# Create a virtual environment
```
python -m venv venv
```

# Activate the virtual environment
```
.\venv\Scripts\activate
```

# Install the dependencies
```
pip install -r requirements.txt
```

# Initialize the MQTT broker with docker
```
docker-compose up -d
```

# Run the subscriber in a terminal
```
python paho_subscribe.py
```

# Run the generator in a separate terminal
```
python paho_generator.py
```