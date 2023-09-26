import csv
import json

with open('finetuning-data.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('output.jsonl', mode='w', encoding='utf-8') as jsonl_file:
        for row in csv_reader:
            # Prepare the data
            messages = [
                {
                    "role": "system",
                    # Add your system prompt here, if any
                    "content": ("Marv is an educational researcher who is "
                                "investigating inclusive teachers agency in "
                                "implementing socially just inclusive practices. "
                                "Marv uses PANTIC agency framework and the "
                                "sociopolitical development theory.")
                },
                {"role": "user", "content": row['Copy']},
                {"role": "assistant", "content": row['Codes']}
            ]
            # Write to the JSONL file
            jsonl_file.write(json.dumps({"messages": messages}) + '\n')
