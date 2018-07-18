#! /usr/bin/python3
# -*- coding: utf-8 -*-


import paho.mqtt.client as mqtt

topic = 'outTopic'

def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

    topic = msg.topic
    msg = str(msg.payload)
    string = 't:' + topic + ',' + ' ' + 'm:' + msg + ','

    file = open('str.txt', 'w') 
    file.write(string)
    return ''

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.20", 1883, 60)
client.loop_forever()