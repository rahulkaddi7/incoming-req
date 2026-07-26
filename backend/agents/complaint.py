from langgraph.types import Command 

from pydantic_classes import RequestState
from configs import complaint_config, llm

def complaint(state:RequestState):
    system_prompt = """
    You are a customer support agent.

    Generate a professional acknowledgement text response.

    Rules:
    - Do NOT write an email.
    - write a body, and regards

    Mention that:
        - complaint received
        - apology
        - escalated to senior support
        - someone will contact them shortly
        Don't invent any information.
    """

    messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":state["request"]} 
    ]

    response = llm.invoke(messages)

    return Command(
        update={
            "response": response.content[0]["text"],
            "assigned_team": complaint_config["assigned_team"],
            "status": complaint_config["status"],
            "follow_up": complaint_config["follow_up"],
            "actions_taken": complaint_config["actions_taken"],
            "highPriority":True
        },
        goto = "logger"
    )