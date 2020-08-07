#!/usr/bin/python3

from flask import Flask
from flaskwebgui import FlaskUI
from flask import render_template
from flask import request

from utils import pyvol as pyvol

WIN_MEMDIR = "mem_dumps/windows/"
LIN_MEMDIR = "mem_dumps/linux/"
MAC_MEMDIR = "mem_dumps/mac/"

# Singular instance of Pyvol
vol = pyvol.Pyvol()

# App and UI
app = Flask(__name__)
ui = FlaskUI(app, height=1000, width=1300)

# Routes
@app.route("/", methods=['GET'])
def index():
    return render_template('home.html')

@app.route("/analyze", methods=['GET'])
def analyze():
    return render_template('analyze.html')

@app.route("/execute", methods=['GET'])
def execute():
    # assert request.path == "/analyze"
    assert request.method == 'GET'

    memfile = request.args['memfile'].split("\\")[-1]
    options = request.args['options']
    command = request.args['command']

    if memfile != None:
        vol.add_file(WIN_MEMDIR + str(memfile))

    if options != None:
        vol.add_option(str(options))

    if command != None:
        vol.add_command(str(command))

    # if outfile != None:
    #     vol.add_outputfile(str(outfile))
    # else:
    vol.add_outputfile("out")

    vol.debug()

    vol.execute()

    file = open("tmp/outputs/" + str(command) + "_output", 'r')
    ret = file.read()
    file.close()

    return render_template("output.html", data = ret, tab = str(command))

# Start
ui.run()
