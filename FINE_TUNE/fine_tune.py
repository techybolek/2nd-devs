from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-TzglsSCioGhh1BV6G6OXkd28",
  model="gpt-3.5-turbo"
)