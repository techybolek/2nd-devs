import { BufferWindowMemory } from "langchain/memory";
import { ConversationChain } from "langchain/chains";
import { OpenAI } from "@langchain/openai";


const chat = new OpenAI();
const memory = new BufferWindowMemory({ k: 2 });
const chain = new ConversationChain({ llm: chat, memory: memory });
const {response: response1} = await chain.call({ input: "Hey there! I'm Adam" });
console.log(`AI:`, response1); // Hi Adam!
const {response: response2} = await chain.call({ input: "Hold on." });
console.log(`AI:`, response2); // Likewise, how can I help you?

// Tutaj model "zapomina" imię, ponieważ "k" jest ustawione na 1. Wcześniejsza wiadomość została ucięta.
const {response: response3} = await chain.call({ input: "Do you know my name?" });
console.log(`AI: `, response3); // Nope.
const {response: response4} = await chain.call({ input: "How big is the earth." });
console.log(`AI:`, response4); // Likewise, how can I help you?
const {response: response5} = await chain.call({ input: "How big is the mars." });
console.log(`AI:`, response5); // Likewise, how can I help you?
const {response: response6} = await chain.call({ input: "Do you know my name?" });
console.log(`AI:`, response6); // Likewise, how can I help you?