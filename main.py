from flask import Flask, render_template, request

#from flask_cors import CORS

#from main import #something

app = Flask(__name__)
#CORS(app)

@app.route('/diagnoses')
def get_diagnoses():
    return 

@app.route("/")
def hello_world():
    return "fl"

@app.route("/dothis")
def dothis():
    return "hello"