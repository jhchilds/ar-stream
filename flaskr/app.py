import os
from flask import Flask
from flask import render_template



app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

@app.route('/')
def index():
    return render_template('index.html')

