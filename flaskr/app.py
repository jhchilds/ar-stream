import os
import json
from flask import Flask, request, jsonify
from flask import render_template
from threading import Thread,Event
from time import sleep
from random import random



from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

socketio = SocketIO(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/stream', methods=['POST'])
def stream():
    socketio.emit('data', request.form)
    return 'ok'

socketio.run(app, host="0.0.0.0", port=1142, log_output=True)




