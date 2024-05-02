const AIDEVS_BASE_URL = "https://tasks.aidevs.pl/"

const _getTask = (taskName: string) => {

    console.log(taskName)
    return {
        theTask: "Co różni pseudonimizację od anonimizowania danych?",
        taskToken: ''
    }
}
export const getTask = async (taskName: string) => {
  const apiKey = process.env.AIDEVS_API_KEY;
  const headers = {
    'Content-Type': 'application/json',
    // add other headers if needed
  };

  let url = `${AIDEVS_BASE_URL}token/${taskName}`;
  let data = { apikey: apiKey };

  let response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  let parsedResponse = await response.json();
  const token = parsedResponse.token;
  console.log('Token:', token)

  url = `${AIDEVS_BASE_URL}task/${token}`;
  response = await fetch(url, { method: 'POST' });
  parsedResponse = await response.json();

  return { theTask: parsedResponse.question, taskToken: token };
};

export const submitTask = async (answer: string, token: string) => {
  const url = `${AIDEVS_BASE_URL}answer/${token}`;
  const data = { answer: answer };
  const headers = {
    'Content-Type': 'application/json',
    // add other headers if needed
  };

  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  console.log("submit result:", response);
  const parsedResponse = await response.json();
  console.log('submit response:', parsedResponse);

  return parsedResponse;
};

export async function getOaiAnswer(userPrompt:string, systemPrompt?: string ) {
  const BASE_URL = "https://api.openai.com/v1/chat/completions";
  const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
  const url = BASE_URL;
  const headers = { 'Authorization': `Bearer ${OPENAI_API_KEY}`, 'Content-Type': 'application/json' };

  let messages: any[] = [];
  if (systemPrompt !== null) {
    messages = [{ role: "system", content: systemPrompt }];
  }
  messages.push({ role: "user", content: userPrompt });

  const data = { model: "gpt-4", messages: messages };

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: headers,
      body: JSON.stringify(data)
    });
    const responseData = await response.json();
    const resp = responseData.choices[0].message.content;
    return resp;
  } catch (error) {
    console.error(error);
  }
}