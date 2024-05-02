import { getOaiAnswer, getTask, submitTask } from "../../SHARED/taskUtil";
import * as fs from "fs";

const data = fs.readFileSync('./C3/L5/people.json', 'utf-8')
const people: any[] = JSON.parse(data)
console.log(people[0])
people.forEach(p => {
    p.imie = p.imie + ' ' + p.nazwisko
    delete p.nazwisko
})
//console.log(people.map(p=>p.name))

const systemPromptGetName = `Dostaniesz tekst zawierający imię i nazwisko. Twoim zadaniem jest znaleźć imię i nazwisko osobo, a następnie zwrócić je w pierwszym przypadku, bez zdrobienia, w formacie JSON
Pzykład:
User: jaki kolor się podoba Piotrkowi Kaczorowi?
Assistant: { name: "Piotr Kaczor" }
Jeśli nie znajdziesz imienia lub nazwiska, zwróć pusty JSON
`
const { theTask, taskToken } = await getTask("people")
console.log('Task:', theTask)
const nameRecord = JSON.parse(await getOaiAnswer(theTask, systemPromptGetName))
console.log('Name:', nameRecord.name)

const person = people.find(p => p.imie === nameRecord.name)
if (person) {
    console.log('Found person:', person)
    const systemPrompt = 'Oto informacje o pewnej osobie. Dostaniesz pytanie na jej temat i odpowiesz prawdziwie, krótko i zwięźle tylko na podstaie podanych informacji.\n' +
        JSON.stringify(person)
    console.log("System prompt:", systemPrompt)
    const theAnswer = await getOaiAnswer(theTask, systemPrompt)
    console.log('ANSWER:', theAnswer)
    submitTask(theAnswer, taskToken)
} else {
    console.error("Could not find person:", nameRecord)
}

