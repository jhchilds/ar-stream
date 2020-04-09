from flask import Flask, request, render_template
from flask_socketio import SocketIO
from Database import Database
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

db = Database(0, 0, 0, 0, 0)
data_filename = db.create_database()

socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/map', methods=['GET','POST'])
def map():
    return render_template('map.html')

@app.route('/live-position', methods=['GET','POST'])
def live_position():
    return render_template('live-pos.html')

@app.route('/stream', methods=['POST'])
def stream():
    pose_x = request.form["x"]
    pose_y = request.form["y"]
    pose_z = request.form["z"]
    latitude = request.form["lat"]
    longitude = request.form["lon"]

    db.set_pose(pose_x, pose_y, pose_z)
    db.set_lat_long(latitude, longitude)
    db.write_data(data_filename)

    socketio.emit('data', request.form) #This is for live updating to client with websocket
    # Below is server side data collection


    return 'ok'



socketio.run(app, host="0.0.0.0", port=1142, log_output=True)