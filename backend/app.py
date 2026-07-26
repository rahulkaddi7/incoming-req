from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

from db.database import Base, engine
from builder import builder
from schema import ApiRequestBody, ApiResponseBody
from dashboard.escalation import escalation_dashboard
from dashboard.service import service_dashboard
from dashboard.enquiry import enquiry_dashboard
from dashboard.complaint import complaint_dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = builder.compile()

@app.post("/requests/process",response_model=ApiResponseBody)
def process_request(body: ApiRequestBody):
    result = graph.invoke(
        {
            "request": body.request
        }
    )

    return ApiResponseBody(
        classification=result["classification"].classification,
        urgency=result["urgency"],
        response=result["response"],

        assigned_team=result["assigned_team"],
        status=result["status"],
        follow_up=result["follow_up"],

        highPriority=result["highPriority"],
    )

@router.get("/dashboard/complaint")
def get_complaint_dashboard():
    return complaint_dashboard()


@router.get("/dashboard/enquiry")
def get_enquiry_dashboard():
    return enquiry_dashboard()


@router.get("/dashboard/service")
def get_service_dashboard():
    return service_dashboard()


@router.get("/dashboard/escalation")
def get_escalation_dashboard():
    return escalation_dashboard()

app.include_router(router)
