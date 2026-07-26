# from db.crud import save_request

# save_request(
    
#     request="Refund my money",
#     classification="Complaint",
#     urgency="High",
#     assigned_team="Billing",
#     generated_response="Acknowledged",
#     follow_up="2 Hours",
#     status="Escalated",
#     reasoning="Customer requested refund",
#     confidence=0.96,
# )

# print("Inserted!")

from db.database import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)