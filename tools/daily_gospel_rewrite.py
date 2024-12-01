import re

book_mapping = {
    "Lk": "Luke",
    "Mt": "Matthew",
    "Mk": "Mark",
    "Jn": "John"
}

# Input and output file paths
input_file = "C:\\Repositories\\synopsis\\tools\\data\\000.txt"  # Update with your input file path
output_file = "C:\\Repositories\\synopsis\\tools\\data\\000_rewrite.txt"  # Update with your desired output file path

# Function to rewrite the lines
def rewrite_lines(line):
    # Split the line into date and gospel reference
    date, gospel = line.split(" : ")

    # Replace book abbreviations with full names
    for abbrev, full_name in book_mapping.items():
        if gospel.startswith(abbrev):
            gospel = gospel.replace(abbrev, full_name, 1)

    # Replace commas with colons in verse references
    gospel = re.sub(r"(\d+),(\d+)", r"\1:\2", gospel)

    return f"{date} : {gospel}"

# Read, process, and write the file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Strip the line to avoid trailing newline issues
        line = line.strip()
        if line:  # Skip empty lines
            rewritten_line = rewrite_lines(line)
            outfile.write(rewritten_line + "\n")

print(f"Rewritten file saved to {output_file}")
