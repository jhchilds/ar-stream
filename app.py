from flask import Flask, request
from flask import render_template
from flask_socketio import SocketIO
import csv, datetime

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

socketio = SocketIO(app, cors_allowed_origins='*')


# Create new CSV when server is started
data_filename = 'data/pose_data_' + str(datetime.datetime.now()) +'.csv'
with open(data_filename, mode='w') as data_file:
    csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['pose_x', 'pose_y', 'pose_z'])



@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/live-position', methods=['GET','POST'])
def live_position():
    return render_template('live-pos.html')

@app.route('/stream', methods=['POST'])
def stream():
    socketio.emit('data', request.form) #This is for live updating to client with websocket
    # Below is server side data collection
    pose_x = request.form["x"]
    pose_y = request.form["y"]
    pose_z = request.form["z"]
    with open(data_filename, mode='a') as data_file:
        csv_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([pose_x, pose_y, pose_z])


    return 'ok'






socketio.run(app, host="0.0.0.0", port=1142, log_output=True)




