import json
from pathlib import Path
import urllib.parse
import urllib.request

BASE_FDA_URL = 'https://api.fda.gov/drug/ndc.json?search=dea_schedule:C'

def build_search_url(category, max_results: int) -> str:
    query_parameters = [('limit', max_results)]

    return f'{BASE_FDA_URL}{category}&{urllib.parse.urlencode(query_parameters)}'

def read_json(url: str, num_of_entries: int) -> dict:
    response = None
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        json_text = response.read().decode(encoding = 'utf-8')
        json_dict = json.loads(json_text)
        drug_names = set()
        for i in range(num_of_entries):
            drug_names.add(json_dict['results'][i]['generic_name'])
        return drug_names
    finally:
        if response != None:
            response.close()

def make_output_file(list_of_drugs: set) -> None:
    with open("list_of_drugs.txt", 'a') as file:
        for drug_name in list_of_drugs:
            file.write(drug_name.lower()+'\n')
    
def get_drugs(max_entries) -> list:
    return read_json(build_search_url('V', max_entries), max_entries)

if __name__ == '__main__':
    make_output_file(get_drugs(600))