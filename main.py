from flask import Flask, render_template, request
import paho.mqtt.publish as publish
import random
import time

broker = '41.193.5.155'
port = 23000
client_id = f'python-mqtt-{random.randint(0, 1000)}'

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def form_data():
    ph = request.form['ph']
    water_level = request.form['water_level']
    lux = request.form['lux']
    temperature = request.form['temperature']
    humidity = request.form['humidity']

    ph_topic = 'Topic/pH'
    wl_topic = 'Topic/WaterLevel'
    lux_topic = 'Topic/PhotoResistor'
    temp_topic = 'Topic/Temperature'
    humid_topic = 'Topic/Humidity'

    msgs = [{
        'topic': ph_topic,
        'payload': ph,
        "qos": 2
    }, {
        'topic': wl_topic,
        'payload': water_level,
        "qos": 2
    }, {
        'topic': lux_topic,
        'payload': lux,
        "qos": 2
    }, {
        'topic': temp_topic,
        'payload': temperature,
        "qos": 2
    }, {
        'topic': humid_topic,
        'payload': humidity,
        "qos": 2
    }]

    publish.multiple(msgs, hostname=broker, port=port)
    time.sleep(1)
    return (render_template('index.html'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
