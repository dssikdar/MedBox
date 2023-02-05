from pathlib import Path

def search_medication(drug_query: str, file_path: Path) -> str:
    with open(file_path, 'r', encoding='utf-8') as drugs_file:
        for line in drugs_file:
            if drug_query in line:
                return line
            
if __name__ == '__main__':
    my_query = 'Tylenol'
    file_path = Path('meds.txt')
    print(search_medication(my_query, file_path))