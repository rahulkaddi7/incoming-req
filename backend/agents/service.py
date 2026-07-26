from langgraph.types import Command 

from pydantic_classes import RequestState, ServiceRequestResponse
from configs import service_request_config, department_map, llm

def service(state:RequestState):
    system_prompt = f"""
        You are a customer support service request processor.

        Available departments:
        {department_map}

        Tasks:
        1. Identify the requested service.
        2. Extract the important details.
        3. Choose ONLY one department from the department map.
        4. Generate a confirmation message.

        Rules:
        - Do not invent department names.
        - If no department matches exactly, choose the closest one.
        - Do not generate an email.
        - Keep the confirmation message under 50 words.
    """

    messages = [
        {"role":"system", "content":system_prompt},
        {"role":"user", "content":state["request"]}
    ]

    response = llm.with_structured_output(ServiceRequestResponse).invoke(messages)

    return Command(
        update={
            "response": response.confirmation_message,
            "assigned_team": service_request_config["assigned_team"] + "-" + response.assigned_department,
            "status": service_request_config["status"],
            "follow_up": service_request_config["follow_up"],
            "actions_taken": service_request_config["actions_taken"],
            "service_type": response.service_type,
            "service_details": response.extracted_details,
            "highPriority": False,
        },
        goto = "logger"
    )

