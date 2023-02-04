import requests

url = "https://api.fda.gov/drug/drugsfda.json"

def drug_exists(generic_name):
    params = 'search=generic_name:{name}+openfda.generic_name:{name}+product.active_ingredients.name:{name}'.format(name='"'+generic_name+'"')
    response = requests.get(url, params = params)
    #req = requests.Request('GET',url, params = params)
    #print(req.prepare().url)
    #print(response.text)
    return response.ok

#print(drug_exists("CLOBETASOL PROPIONATe"))
#print(drug_exists("sfklsfd"))
#print(drug_exists("Adderall"))
#print(drug_exists("migraine"))
#print(drug_exists("Ibuprofen"))