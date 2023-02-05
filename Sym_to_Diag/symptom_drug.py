import requests
import json
# File that gets a symptom list and returns the best drugs for the purpose

url = "https://api.fda.gov/drug/label.json"

def retrieve_drugs(search_str):
    symptoms = search_str.split()
    return [best_drug(purpose) for purpose in symptoms]

def best_drug(purpose):
    params = 'search=purpose:{purpose}+AND+_exists_:openfda.brand_name&limit=2'.format(purpose='"'+purpose+'"')
    response = requests.get(url, params = params)
    results = response.json()['results']

    brand_names = [result['openfda']['brand_name'] for result in results]

    return brand_names

#print('{}'.format(json.dumps(best_drug('scaly'), indent=4)))
print(best_drug('scaly'))
