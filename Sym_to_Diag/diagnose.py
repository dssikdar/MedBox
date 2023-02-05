from ApiMedicClass import DiagnosisClient


def return_sym_ids(user_symptoms, all_symptoms) -> list:
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


def get_most_probable_diagnosis(output: dict) -> str:
    diagnosis = output['Message'].split()[0]
    confidence_level = output['Message'].split()[2]

    return f"I am {confidence_level} confident that you have {diagnosis}."


def run(user_symptoms: list, gender: str, yob: str) -> dict:       
    d = DiagnosisClient(username="s2NEp_GMAIL_COM_AUT",language="en-gb",healthServiceUrl="https://healthservice.priaid.ch",authServiceUrl="https://authservice.priaid.ch/login",password="f9H6Brm5Z3NyFk8p7")
      
    all_symptoms = d.loadSymptoms()

    relevant_sym_ids = return_sym_ids(user_symptoms, all_symptoms)
                
    do = d.loadDiagnosis(gender=gender, yearOfBirth=int(yob), selectedSymptoms=relevant_sym_ids)

    issues = {}
    if do:
        issues = {"Message":""}
        for i in range(len(do)):
            if len(do)-1 == i:
                issues["Message"] = issues["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "
            elif len(do)-2==  i:
                issues["Message"] = issues["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "+" and "
            else:
                issues["Message"] = issues["Message"]+ do[i]["Issue"]["Name"] + " (Accuracy: " + str(do[i]["Issue"]["Accuracy"])[:4] +"% ) "+" , "
    else:
        issues = {"Message":"I could not diagnose by entered symptoms."} 
        
    return issues

    
if __name__ == '__main__':
    symptoms = ['cough', 'fever', 'headache']
    gender = 'Male'
    yob = 1999

    diagnosis = run(symptoms, gender, yob)
    print(get_most_probable_diagnosis(diagnosis))
