import csv
import json

SYSTEM_PROMPT = "Marv is an educational researcher who is investigating inclusive teacher's agency in implementing socially inclusive practices. He will read in a paragraph from an interview and determine if it is significant from a research perspective and if it includes important themes for the PANTIC agency framework and the sociopolitical development theory. Marv will return a 0 is the paragraph is not significant and a 1 if it is significant."

with open('finetuning-data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('output.jsonl', mode='w', encoding='utf-8') as jsonl_file:
        for row in csv_reader:
            # Prepare the data
            messages = [
                {
                    "role": "system",
                    "content": (SYSTEM_PROMPT)
                },
                {"role": "user", "content": row['Copy']},
                {"role": "assistant", "content": row['Codes']}
            ]
            # Write to the JSONL file
            jsonl_file.write(json.dumps({"messages": messages}) + '\n')
