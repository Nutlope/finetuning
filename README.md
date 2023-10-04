# GPT-3.5 Fine tuning script

This repo contains script to clean up data and These are two files you can run to do finetuning.

## Steps

1. Get your data into a CSV, ideally two columns. One will contain the prompt and one will contain the expected response.
2. Specify your system prompt in the `SYSTEM_PROMPT` variable in `preparing-data.py`.
3. Run `preparing-data.py` to transform data into JSONL format with a system prompt of your choice.
4. Make sure you've exported the env variable `OPENAI_API_KEY` with your API key.
5. Specify the name of the model then run `finetuning-data.csv` to actually trigger a fine-tuning job through OpenAI.

## To add

- Validation script and step
