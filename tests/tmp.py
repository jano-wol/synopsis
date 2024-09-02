import json

def clean_values(data):
    if isinstance(data, dict):
        return {k: clean_values(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_values(item) for item in data]
    else:
        return None

def modify_json_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    
    modified_data = clean_values(data)

    with open("synopsis_empty", 'w') as file:
        json.dump(modified_data, file)
    return modified_data
    
    print(modified_data)

# Replace 'your_file.json' with the path to your JSON file
tmp1 = modify_json_file('../src/assets/synopsis_szit.json')
print(tmp1)
tmp2 = modify_json_file('../src/assets/synopsis_esv.json')
print(tmp1 == tmp2)