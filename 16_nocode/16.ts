import { ChatOpenAI } from "langchain/chat_models/openai";
import {HumanMessage, SystemMessage} from "langchain/schema";
import {managerSchema} from "./schema";
import {parseFunctionCall} from "./helper.ts";

const MAKE_WEBHOOK = "https://hook.us1.make.com/vgd5gmv7w6gsg083lpqogg5iz39gc6sm"
const model = new ChatOpenAI({
    modelName: "gpt-4-0613",
}).bind({functions: [managerSchema], function_call: { name: "task_manager" }});
const todoist = async (manager: { args: any }) => {
    return await fetch(MAKE_WEBHOOK, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(manager.args),
    });
};
const act = async (command: string) => {
    console.log('User: ' + command);
    const add = await model.invoke([
        new SystemMessage("Fact: Today is 04/10/2024 01:47."),
        new HumanMessage(command)
    ]);
    const action = parseFunctionCall(add);
    console.log('Action:', action)
    if (action) {
        const response = await todoist(action);
        console.log('Make returned:', response)
        const { data } = await response.json();
        console.log('AI: ' + data);
        return data;
    }
    return 'No action found';
}
await act('List my tasks');
await act('Buy milk, eggs, and bread this evening, and make a note about the new Alice feature for tmrw mrng');
await act('I bought groceries and finished the newsletter about the new features.');




