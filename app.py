from flask import Flask, request, jsonify
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

app = Flask(__name__)

# Initialize LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(10, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    temperature = data.get('temperature')
    motion = data.get('motion')
    return jsonify({'status': 'success', 'temperature': temperature, 'motion': motion})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


