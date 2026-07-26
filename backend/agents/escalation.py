from langgraph.types import Command 

from pydantic_classes import RequestState, EscalationResponse
from configs import escalation_config, llm

def escalation(state:RequestState):
    system_prompt = """
        You are an escalation handling agent.

        The user's request has already been classified as an Escalation.

        Your responsibilities are:

        1. Identify why the request requires escalation.
        2. Determine the most appropriate supervisor team.
        3. Generate a short acknowledgement.

        Rules:
        - Assume human intervention is required.
        - Do not attempt to resolve the issue.
        - Do not generate an email.
        - Do not include greetings or signatures.
        - Keep the acknowledgement under 50 words.
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": state["request"]}
    ]

    response = llm.with_structured_output(EscalationResponse).invoke(messages)

    return Command(
        update={
            "response": response.acknowledgement,
            "assigned_team": response.supervisor_team,
            "status": escalation_config["status"],
            "follow_up": escalation_config["follow_up"],
            "actions_taken": escalation_config["actions_taken"],
            "highPriority": True,
            "escalation_reason": response.escalation_reason,
        },
        goto="logger"
    )
