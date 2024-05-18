import { getOaiAnswer, getTask, submitTask } from "../../SHARED/taskUtil";

const COUNTRY_URL = (country: string) => `https://restcountries.com/v3.1/name/${country}`

const CURRENCY_URL = (currency: string) => `http://api.nbp.pl/api/exchangerates/rates/a/${currency}/`

/*
const theUrl = CURRENCY_URL("chf")
console.log('THE URL:', theUrl)
const resp = await fetch(theUrl)
//const respB = await resp.blob()
//console.log(respB)
const respText = await resp.json()
console.log(respText)
process.exit()
*/

const systemPromptStep1 = `You'll be given a question in Polish. Your job is to determine, if you have enough knowledge to answer the question truthfully or not.
Return the answer json format. If you don't know, return N/A.
Example: 
User: Ilu ludzi mieszka w Polsce?
Assistant: { "answer": "N/A" }
Explanation: You don't have up-to-date knowledge on this topic.
User: How big is the earth?
Assistant: { "answer": "<your answer goes here>" }
`

const systemPromptStep2 = `You will be given a question in Polish. The question can either be about the current exchange rate against Polish zloty or the population of a country.
If it's about the exchange rate, return the currency code in lower case. If it's about a country, return the country name in English, all lowercase.
Also return the flag indicating the response tyle, 0 for currency, 1 for country.
Example:
User: Jaki jest dziś kurs franka?
Assistant: { "answer": "chf", flag: "0" }
`

const systemPromptCountry = (info: string) => {
    return `Here is information about a country:
${info}
You will be given a question about this country in Polish. Answer the question truthfully and ultra-consisely.`
}

const { theTask, taskToken } = await getTask("knowledge")
console.log('Task:', theTask)
const theAnswer = await getAnswer(theTask)
console.log('Answer:', theAnswer)
//const resp = await submitTask(theAnswer, taskToken)
//console.log('Response:', resp)

async function getAnswer(theQuestion: string) {
    const verdictRaw = await getOaiAnswer(theTask, systemPromptStep1)
    //console.log('Verdict:', verdictRaw)
    let theAnswer = JSON.parse(verdictRaw).answer
    if (theAnswer === "N/A") {
        const codeRaw = await getOaiAnswer(theQuestion, systemPromptStep2)
        //console.log('Code raw:', codeRaw)
        const code = JSON.parse(codeRaw)
        if (code.flag === '0') {
            const currency = code.answer
            //console.log('Currency:', currency)
            //get the currrency at the currency url
            const resp = await fetch(CURRENCY_URL(currency))
            const respText = await resp.json()
            //@ts-ignore
            theAnswer = respText.rates[0].mid
            //console.log(theQuestion, theAnswer)
        } else {
            const country = code.answer
            const resp = await fetch(COUNTRY_URL(country))
            const respJson = await resp.json()
            //@ts-ignore
            const systemPrompt = systemPromptCountry(respJson)
            theAnswer = await getOaiAnswer(theQuestion, systemPrompt)
        }
    }
    return theAnswer
}

