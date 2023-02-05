from flask import Flask, render_template, request
import database

#from flask_cors import CORS

#from main import #something

app = Flask(__name__)
#CORS(app)

@app.route('/diagnoses', methods = ['POST', 'GET'])
def get_diagnoses_drugs():
    if request.method == 'POST':
      symptoms = request.form.get('symptoms')
      return diagnose(symptoms)

@app.route("/withdraw", methods = ['POST', 'GET'])
def decrement_inventory():
   if request.method == 'POST':
      name = request.form.get('name')
      a_drug = get_drug("Salt")
      if a_drug['inventory'] > 0:
        database.update_stock(a_drug['name'], a_drug['inventory']-1)
        
        return True

@app.route("/dothis", )
def get_drug():
    return get_drug(request.args.get('drug_name'))