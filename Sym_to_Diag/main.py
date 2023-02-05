from flask import Flask, render_template, request
import database
import diagnose
import json

from flask_cors import CORS

#from main import #something

app = Flask(__name__)
CORS(app)

@app.route('/diagnoses', methods = ['POST', 'GET'])
def get_diagnoses_drugs():
    if request.method == 'POST':
      symptoms = json.loads(request.data).get('symptoms')
      print(symptoms)
      #return {"diagnoses":"sickness", "treatment": "apple"}

      #hard coded string for testing
      '''return {'drugs':['Vicks DayQuil and Nyquil SEVERE Cold',
                              'Flu and Congestion Medicine and Congestion Medicine LiquiCaps Convenience Pack - Relieves Cough, Sore Throat, Congestion, Fever and Runny Nose, Daytime & Nighttime, 48 CT', 
                              'Vicks Vapo Steam Cough Suppressant', 
                              'Tylenol Child & Adult Oral Suspension, Pain & Fever, Cherry, 8 fl. Oz', 
                              'Navage Nasal Care Saline Nasal Irrigation Kit', 
                              'Sinex Severe Vicks Nasal Decongestant Spray, Twin Pack, 1 oz', 
                              'Ricola Nautral Herb Cough Drops', 
                              'Betadine Antiseptic Sore Throat Garagle, 8 OZ']}'''
      diagnoses, treatment = diagnose.run(symptoms, "Male", 2000, 'i7FGf_UCI_EDU_AUT', 'z4E5Ddt7W8FySq39J')
      drugs = diagnose.search_med_using_diagnosis(diagnoses)
      print(diagnoses)
      print(drugs[0])
      return {'drugs':drugs[0]}

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

def unravel_symptoms(form):
  '''Takes in request.form, unravels it to get a list of simple symptoms'''
  
