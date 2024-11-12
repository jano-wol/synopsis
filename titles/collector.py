import os
import json

# Define directories and file name patterns
languages = ["de", "en", "hu", "la"]
categories = ["part_titles", "section_titles", "sub_part_titles"]

# Initialize the structure for JSON data
data = {lang: {category: {} for category in categories} for lang in languages}

# Read files and populate the data dictionary
for lang in languages:
    for category in categories:
        # Construct the filename based on language and category
        filename = f"{lang}_{category}"
        if os.path.isfile(filename):
            # Open and read the file, expecting it to be UTF-8 encoded
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    # Split each line into key and value based on tab character
                    key_value = line.strip().split('\t', 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        # Populate the data dictionary
                        data[lang][category][key] = value

# Write the structured data to a JSON file
output_filename = "collected_titles.json"
with open(output_filename, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Data has been collected into {output_filename}")

