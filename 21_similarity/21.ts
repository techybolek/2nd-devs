import {HumanMessage, SystemMessage} from "langchain/schema";
import {ChatOpenAI} from "langchain/chat_models/openai";
import {getVectorStore} from "./helpers.ts";

const query = "Do you know the name of Adam's dog?";
console.log('Getting vector store...')
const vectorStore = await getVectorStore(false);
console.log('Performing similarity search...')
const context = await vectorStore.similaritySearchWithScore(query, 3);
console.log('Vector store returned:', context)
console.log('Creating new chat...')
const chat = new ChatOpenAI();
console.log('Executing API call...')
const { content } = await chat.call([
    new SystemMessage(`
        Answer questions as truthfully using the context below and nothing more. If you don't know the answer, say "don't know".
        context###${context?.[0]?.[0].pageContent}###
    `),
    new HumanMessage(query),
]);

console.log('Received:',content);