echo $GROQ_API_KEY
curl https://api.groq.com/openai/v1/chat/completions   -H "Content-Type: application/json"   -H "Authorization: Bearer $GROQ_API_KEY"   -d '{
    "model": "mixtral-8x7b-32768",
    "messages": [
      {
        "role": "system",
        "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
        "role": "user",
        "content": "Compose a poem that explains the concept of recursion in programming."
      }
    ]
  }'