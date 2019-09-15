import os
from flask import Flask, request
from flask import render_template

# from flask_socketio import SocketIO



app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)
# socketio = SocketIO(app)

@app.route('/', methods=['POST'])
def index():
    print(request.form)
    return render_template('index.html')


# @socketio.on('message')
# def handle_message(msg):
#     print('received message: ' + msg)

# flask-socketio can not use Flask Run command, simply run with python NOT Flask Run.

# socketio.run(app)




