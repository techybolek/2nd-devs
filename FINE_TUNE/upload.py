from openai import OpenAI
client = OpenAI()

file_id = client.files.create(
  file=open("gwara.jsonl", "rb"),
  purpose="fine-tune"
)

print('File ID:', file_id)