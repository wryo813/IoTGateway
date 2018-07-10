#! /usr/bin/python
# -*- coding: utf-8 -*-

import  sys
from time import sleep
import paho.mqtt.client as mqtt
from flask import Flask, request
import re


app = Flask(__name__)

host = '192.168.0.20'
port = 1883

@app.route("/")
def hello():
    return "Now Running"

@app.route("/", methods=['POST'])
def webhook():

    str = request.data

    a = 't:'
    b = 'b:'
    x = ','

    topicData = re.search(r'%s(.*?)%s'%(a,x), str)
    bodyData = re.search(r'%s(.*?)%s'%(b,x), str)
    
    topic = topicData.group(1)
    body = bodyData.group(1)

    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.connect(host, port=port, keepalive=60)

    client.publish(topic, body)

    print('Topic={0}'.format(topic))
    print('Body={0}'.format(body))

    return 'OK'

if __name__ == "__main__":
    app.run(debug=False, host=host, port=80)