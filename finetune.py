import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

MODELNAME = 'mom-interviews'

training_file_name = "output.jsonl"
training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine-tune"
)
training_file_id = training_response["id"]

print("Training file ID:", training_file_id)

response = openai.FineTuningJob.create(
    training_file=training_file_id,
    model="gpt-3.5-turbo",
    suffix=MODELNAME,
)

job_id = response["id"]

print("Job ID:", response["id"])
print("Status:", response["status"])
