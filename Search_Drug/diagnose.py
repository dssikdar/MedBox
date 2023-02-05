from ApiMedicClass import DiagnosisClient
from pathlib import Path
from search_med import search_med_via_diag

def return_sym_ids(user_symptoms: list, all_symptoms: list) -> list:
    sym_ids = []
    for symptom in user_symptoms:
        for i in all_symptoms:
            if i["Name"].lower() == symptom.lower():
                sym_ids.append(i["ID"])
    return sym_ids

def filter_keywords(output: dict) -> list:
    treatment_description = output.get('TreatmentDescription')
    list_of_words = treatment_description.split()
    return [word for word in list_of_words if word[0].isupper()]

def get_most_probable_diagnoses(output: dict) -> list:
    return output['Message'].split(', ')[0:3]

def get_diagnosis_id(diag_client, user_issue):
    all_issues = diag_client.loadIssues()
    for issue in all_issues:
        if user_issue.lower() == issue["Name"].lower():
            return int(issue["ID"])

def run(user_symptoms: list, gender: str, yob: int, username: str, password: str) -> dict:   
    d = DiagnosisClient(username=username,language="en-gb",healthServiceUrl="https://healthservice.priaid.ch",authServiceUrl="https://authservice.priaid.ch/login",password=password)
      
    all_symptoms = d.loadSymptoms()

    relevant_sym_ids = return_sym_ids(user_symptoms, all_symptoms)
                
    do = d.loadDiagnosis(gender=gender, year_of_birth=yob, selectedSymptoms=relevant_sym_ids)

    diagnosis = {'Message':''}
    if do:
        for i in range(len(do)):
            diagnosis['Message'] = diagnosis['Message'] + do[i]['Issue']['Name'] + ', '
    else:
        diagnosis = {'Message': 'I could not diagnose by entered symptoms.'} 

    diagnosis_1_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[0])
    diagnosis_2_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[1])
    diagnosis_3_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[2])

    list_of_treatments = []
    list_of_treatments.append(d.loadIssueInfo(diagnosis_1_id)['TreatmentDescription'])
    list_of_treatments.append(d.loadIssueInfo(diagnosis_2_id)['TreatmentDescription'])
    list_of_treatments.append(d.loadIssueInfo(diagnosis_3_id)['TreatmentDescription'])

    return get_most_probable_diagnoses(diagnosis), list_of_treatments 


def search_med_using_diagnosis(diagnoses: list) -> list:
    medications = []
    for diagnosis in diagnoses:
        med = search_med_via_diag(diagnosis.lower())
        if med != None:
            medications.append(med)
    return medications
    
    
if __name__ == '__main__':
    #symptoms = ["allergies","soreness","body ache","anxiety","pain"]
    #symptoms = ["allergy","soreness","anxiety"]
    symptoms = ['cough', 'fever', 'headache']
    gender = 'Male'
    yob = 1999

    api_username = 'insert username here'
    api_password = 'insert password here'

    diagnoses, treatment = run(symptoms, gender, yob, api_username, api_password)
    print('Diagnoses:', diagnoses, '\n')
    print('Treatments:', search_med_using_diagnosis(diagnoses))

