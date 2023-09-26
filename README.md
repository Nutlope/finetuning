# GPT-3.5 Fine tuning script

This repo contains script to clean up data and These are two files you can run to do finetuning.

## Steps

1. Get your data into a CSV, ideally two columns. One will contain the prompt and one will contain the expected response.
2. Run `preparing-data.py` to transform data into JSONL format with a system prompt of your choice.
3. Run `finetuning-data.csv` to actually trigger a fine-tuning job through OpenAI.

## To add

- Validation script and step
- Better docs and more variables
