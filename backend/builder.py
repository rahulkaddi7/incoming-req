
from langgraph.graph import START, StateGraph

from pydantic_classes import RequestState
from agents.classifier import classifier
from agents.complaint import complaint
from agents.enquiry import enquiry
from agents.service import service
from agents.escalation import escalation
from agents.logger import logger

builder = StateGraph(RequestState)

builder.add_node("classifier", classifier)
builder.add_node("complaint", complaint)
builder.add_node("enquiry", enquiry)
builder.add_node("service", service)
builder.add_node("escalation", escalation)
builder.add_node("logger", logger)

builder.add_edge(START, "classifier")