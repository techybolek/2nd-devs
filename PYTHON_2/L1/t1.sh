curl -X POST https://api.openai.com/v1/chat/completions \
-H 'Content-Type: application/json' \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{"model": "gpt-4", "messages": [{"role": "user", "content": "How big is the Earth?"}]}'