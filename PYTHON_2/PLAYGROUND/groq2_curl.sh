echo $GROQ_API_KEY
curl https://api.groq.com/openai/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $GROQ_API_KEY"   -d '{
    "model": "mixtral-8x7b-32768",
    "messages": [
      {
        "role": "system",
        "content": "Get everything user will say and write back in JSON format {\"query\": \"contents of the message\" }. Only return the JSON without any additional text."
      },
      {
        "role": "user",
        "content": "Helloooo!"
      }
    ]
  }'