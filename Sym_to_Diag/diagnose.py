from ApiMedicClass import DiagnosisClient


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
    list_of_diagnoses = output['Message']

    temp1 = []
    for string in list_of_diagnoses.split(':'):
        temp1.append(string.split('(')[0])
    
    temp2 = []
    for string in temp1:
        temp2 += string.split(')')
    
    diagnoses = [temp2[0].rstrip()]
    for i in range(1,3):
        diagnoses.append(temp2[2*i][4:].rstrip())

    return diagnoses


def get_diagnosis_id(diag_client, user_issue):
    all_issues = diag_client.loadIssues()
    for issue in all_issues:
        if user_issue.lower() == issue["Name"].lower():
            return int(issue["ID"])


def run(user_symptoms: list, gender: str, yob: str) -> dict:       
    d = DiagnosisClient(username="s2NEp_GMAIL_COM_AUT",language="en-gb",healthServiceUrl="https://healthservice.priaid.ch",authServiceUrl="https://authservice.priaid.ch/login",password="f9H6Brm5Z3NyFk8p7")
      
    all_symptoms = d.loadSymptoms()

    relevant_sym_ids = return_sym_ids(user_symptoms, all_symptoms)
                
    do = d.loadDiagnosis(gender=gender, yearOfBirth=int(yob), selectedSymptoms=relevant_sym_ids)

    diagnosis = {'Message':''}
    if do:
        for i in range(len(do)):
            if len(do)-1 == i:
                diagnosis["Message"] = diagnosis["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "
            elif len(do)-2 == i:
                diagnosis["Message"] = diagnosis["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "+" and "
            else:
                diagnosis["Message"] = diagnosis["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "+" , "
    else:
        diagnosis = {"Message":"I could not diagnose by entered symptoms."} 

    diagnosis_1_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[0])
    diagnosis_2_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[1])
    diagnosis_3_id = get_diagnosis_id(d, get_most_probable_diagnoses(diagnosis)[2])

    list_of_treatments = []
    list_of_treatments.append(d.loadIssueInfo(diagnosis_1_id)['TreatmentDescription'])
    list_of_treatments.append(d.loadIssueInfo(diagnosis_2_id)['TreatmentDescription'])
    list_of_treatments.append(d.loadIssueInfo(diagnosis_3_id)['TreatmentDescription'])

    return get_most_probable_diagnoses(diagnosis), list_of_treatments
    
    
if __name__ == '__main__':
    symptoms = ['cough', 'fever', 'headache']
    gender = 'Male'
    yob = 1999

    diagnoses, treatment = run(symptoms, gender, yob)
    print('Diagnoses:', diagnoses, '\n')
    print('Treatment:', treatment)

