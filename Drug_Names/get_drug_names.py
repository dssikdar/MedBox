import json
from pathlib import Path
import urllib.parse
import urllib.request

BASE_FDA_URL = 'https://api.fda.gov/drug/ndc.json?search=dea_schedule:CIV&'

def build_search_url(max_results: int) -> str:
    query_parameters = [('limit', max_results)]

    return f'{BASE_FDA_URL}{urllib.parse.urlencode(query_parameters)}'

def get_result(url: str, num_of_entries) -> dict:
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
    
def run() -> list:
    max_entries = 10
    return get_result(build_search_url(max_entries), max_entries)

if __name__ == '__main__':
    print(run())