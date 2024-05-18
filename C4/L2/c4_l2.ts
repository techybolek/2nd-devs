import { getOaiAnswer, getTask, submitTask } from "../../SHARED/taskUtil";

const { theTask, taskToken } = await getTask("tools")
console.log('Task:', theTask)
const parsedTask: any = await determineTask(theTask)
console.log('parsed task:', parsedTask)
const theAnswer = parsedTask.arguments
theAnswer.tool = parsedTask.tool
console.log('The answer:', theAnswer)
const resp = await submitTask(theAnswer, taskToken)
console.log('Submit Response:', resp)

async function determineTask(thePrompt: string): Promise<'TODO' | 'CALENDAR'> {

    /*const thePrompt = "You will be given a task description. Your job is to figure out if the task contains date information. If it does,\
return 'CALENDAR'. If it doesn't, return 'TODO'."*/
    const systemPrompt = "Fact: today is 05/17/2024. You are a helpful assistant with the expanded capacity to manage todo lists.\
    You will be given a user prompt in Polish. If the prompt describes a task that needs to be done,\
    add the task either to the TODO list or the CALENDAR list, if it contains date information.\
    If it contains an appointment then also add it to the CALENDAR list. The date should be returned in the format 'DD/MM/YYYY'."

    const functions = [
        {
            "name": "ToDo",
            "description": "Add task to the todo list",
            "parameters": {
                "type": "object",
                "properties": {
                    "desc": {
                        "type": "string",
                        "description": "The task to be added to the todo list",
                    },
                },
                "required": ["desc"],
            },
        },
        {
            "name": "Calendar",
            "description": "Add task to the calendar list",
            "parameters": {
                "type": "object",
                "properties": {
                    "desc": {
                        "type": "string",
                        "description": "The task r appointment to be added to the calendar list",
                    },
                    "date": {
                        "type": "string",
                        "description": "The date when the task or appointment is due",
                    },
                },
                "required": ["desc", "date"],
            },
        }
    ]

    const theTask = await getOaiAnswer(thePrompt, systemPrompt, functions)
    return theTask
}

