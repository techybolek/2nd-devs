import * as fs from "fs";
import {TextLoader} from "langchain/document_loaders/fs/text";
import {IFile, split} from "./helpers.ts";
import {HumanMessage, SystemMessage} from "langchain/schema";
import {ChatOpenAI} from "langchain/chat_models/openai";
import {getSystemPrompt} from "./prompts.ts";

const file: IFile = {title: "Lekcja kursu AI_Devs, S03L03 — Wyszukiwanie i bazy wektorowe", name: 'draft.md', author: 'Adam', excerpt: '', content: '', tags: [],}
let summary: Pick<IFile, "content"> = {content: ''};

const OUTPUT_FILE = '26_summarize/summarized_tr.md'

const loader = new TextLoader(`26_summarize/${file.name}`);
const [doc] = await loader.load();
const documents = split(doc.pageContent, 2000);
console.log('Documents len:', documents.length)

const model = new ChatOpenAI({ modelName: "gpt-4", maxConcurrency: 5 })

let scount = 0
export const summarize = async (chunk: string, file: IFile) => {
    scount++
    const system = getSystemPrompt(file);
    console.log('\n\n##########Summarizing chunk: ', scount, '###################\n', chunk, '\n------------------------------------------------------------------------', scount)

    return model.invoke([
        new SystemMessage(system),
        new HumanMessage(`###${chunk}###`)
    ]);
}

const intro = `# Summary of the document ${file.title}\n\n`;
fs.writeFileSync(OUTPUT_FILE, intro);

for (let i = 0; i < documents.length; i++) {
    const result = await summarize(documents[i].pageContent, {...file, ...summary});
    console.log('OAI returned:', result.content)
    fs.appendFileSync(OUTPUT_FILE, result.content + "\n\n");
}