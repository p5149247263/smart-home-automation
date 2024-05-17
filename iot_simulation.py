import random
import time
import requests

def get_temperature():
    return 20 + random.random() * 5

def get_motion():
    return random.choice([True, False])

def send_data(temp, motion):
    payload = {'temperature': temp, 'motion': motion}
    response = requests.post('http://localhost:5000/process_data', json=payload)
    return response.json()

while True:
    temp = get_temperature()
    motion = get_motion()
    result = send_data(temp, motion)
    print(f"Processed Data: {result}")
    time.sleep(5)
