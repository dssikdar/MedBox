from pathlib import Path
from meds import all_medications

def search_medication(drug_query: str, file_path: Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as drugs_file:
        for line in drugs_file:
            if drug_query in line:
                return line
        return 'No matches found'
            
def search_med_via_diag(diag_query: str) -> list:
    for diag in all_medications.keys():
        if diag_query in diag:
            return all_medications[diag]
            
if __name__ == '__main__':
    my_query = 'Tylenol'
    file_path = Path('meds.txt')
    print(search_medication(my_query, file_path))