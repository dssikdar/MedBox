#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from ApiMedicClass import DiagnosisClient

def run(args: dict) -> dict:       
    d = DiagnosisClient(username="s2NEp_GMAIL_COM_AUT",language="en-gb",healthServiceUrl="https://healthservice.priaid.ch",authServiceUrl="https://authservice.priaid.ch/login",password="f9H6Brm5Z3NyFk8p7")
        
    option = args.get("option")
    issue = args.get("issue")
    symptom_1 = args.get("symptom_1")
    symptom_2 = args.get("symptom_2")
    symptom_3 = args.get("symptom_3")
    if int(option) == 1:
        issues_1 = d.loadIssues()
        for ism in issues_1:
            if issue.lower() == ism["Name"].lower():
                issues = d.loadIssueInfo(int(ism["ID"]))
    if int(option) == 2:
        symptoms = d.loadSymptoms()
        sym_id = []
        gender = args.get("gender","")
        yob = args.get("yob","")
        if symptom_1:
            for i in symptoms:
                if i["Name"].lower() == symptom_1.lower():
                    sym_id.append(i["ID"])
        if symptom_2:
            for i in symptoms:
                if i["Name"].lower() == symptom_2.lower():
                    sym_id.append(i["ID"])
        if symptom_3:
            for i in symptoms:
                if i["Name"].lower() == symptom_3.lower():
                    sym_id.append(i["ID"])
                  
        do = d.loadDiagnosis(gender=gender,yearOfBirth=int(yob),selectedSymptoms=sym_id)
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

def filter_keywords(output: dict) -> list:
    treatment_description = output.get('TreatmentDescription')
    list_of_words= treatment_description.split()
    return [word for word in list_of_words if word[0].isupper()]
    
if __name__ == '__main__':
    # option: 1 or 2
    # issue: choose one among csv

    symptoms = {'option': 1,
                'issue': 'cold',
                'symptom_1': 'Fever',
                'symptom_2': 'Face pain',
                'gender': 'Female',
                'yob': 1993}
    
    diagnosis = run(symptoms)
    print(filter_keywords(diagnosis))
