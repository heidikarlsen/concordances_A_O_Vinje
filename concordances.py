import re
import pandas as pd

def extract_concordances(text, keywords):
    # Split text into words
    words = text.split()
    concordances = []
    # Iterate through each word in the text
    for index, word in enumerate(words):
        if word in keywords:
            # Get 10 words before and 10 words after the keyword
            start = max(0, index - 10)
            end = min(len(words), index + 11)
            concordance = " ".join(words[start:end])
            concordances.append((word, concordance))
    return concordances

def read_text_from_file(file_path):
    # Reading the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Define your keywords
keywords = [
    "nasjonal", "nasjonalt", "nasjonale", "nation", "Nationen", "nasjonen", "Norig", "norsk", "Norske", "norske",
    "norsk Folkeblad", "Norgies", "norskt", "patriotiske", "patriotisk", "svenske", "Svensken", "svenske Krav",
    "svenska", "Sverige", "unasjonale"
]

# Path to your text files
file_path_1 = 'Vaar_Politik_09021868.txt'
file_path_2 = 'Vaar_Politik_01031868.txt'

# Extract text from files
text_1 = read_text_from_file(file_path_1)
text_2 = read_text_from_file(file_path_2)

# Extract concordances
concordances_1 = extract_concordances(text_1, keywords)
concordances_2 = extract_concordances(text_2, keywords)

# Combine results and convert to a DataFrame
all_concordances = concordances_1 + concordances_2
df_concordances = pd.DataFrame(all_concordances, columns=["Keyword", "Concordance"])

# Save to CSV
df_concordances.to_csv('concordances2.csv', index=False, encoding='utf-8-sig')