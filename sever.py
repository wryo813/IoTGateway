#! /usr/bin/python3
# -*- coding: utf-8 -*-

import  sys
from flask import Flask, request
import re


app = Flask(__name__)

host = '192.168.0.20'
port = 1883

@app.route("/")
def hello():
    file = open('str.txt', 'r')
    str = file.read()

    a = 't:'
    b = 'm:'
    x = ','

    topicData = re.search(r'%s(.*?)%s'%(a,x), str)
    bodyData = re.search(r'%s(.*?)%s'%(b,x), str)
    topic = topicData.group(1)
    body = bodyData.group(1)
    print(str)
    print('OutTopic={0}'.format(topic))
    print('OutBody={0}'.format(body))
    
    return str


if __name__ == "__main__":
    app.run(debug=False, host=host, port=80)