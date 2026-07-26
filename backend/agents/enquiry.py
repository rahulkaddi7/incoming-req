from langgraph.types import Command 

from pydantic_classes import RequestState
from configs import enquiry_config, knowledge_base, llm

def enquiry(state:RequestState):
    system_prompt = f"""
    You are a customer support assistant.

    The user has submitted a general enquiry.
    Use ONLY the following knowledge base to answer the customer's enquiry.

    Knowledge Base: {knowledge_base}

    Your task is to:
    1. Identify the enquiry topic.
    2. Answer the user's question accurately.
    3. If the answer is unknown, politely state that the information is unavailable instead of inventing it.

    Rules:
    - If the answer exists in the knowledge base, answer using only that information.
    - If the answer is not present, respond:
    "I'm sorry, I couldn't find information related to your question. A support representative will assist you shortly."
    - Do not invent information.
    """

    messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":state["request"]}
    ]

    response = llm.invoke(messages)

    return Command(
        update={
            "response": response.content[0]["text"],
            "assigned_team": enquiry_config["assigned_team"],
            "status": enquiry_config["status"],
            "follow_up": enquiry_config["follow_up"],
            "actions_taken": enquiry_config["actions_taken"],
            "highPriority":False
        },
        goto = "logger"
    )