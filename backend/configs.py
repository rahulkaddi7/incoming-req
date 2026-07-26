from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

complaint_config = {
    "assigned_team": "Senior Complaint Team",
    "status": "Escalated",
    "follow_up": "2 Hours",
    "actions_taken": [
                    "Acknowledgement Generated",
                    "Escalated to Senior Complaint Team",
                    "Priority Flag Added",
                    "Follow-up Reminder Created"
                ]
}

enquiry_config = {
    "assigned_team": "AI Knowledge Base",
    "status": "Resolved",
    "follow_up": "Not Required",
    "actions_taken": [
        "Enquiry Topic Identified",
        "Knowledge Base Searched",
        "AI Response Generated",
        "Request Marked as Resolved"
    ]
}

service_request_config = {
    "assigned_team": "Service Operations",
    "status": "Assigned",
    "follow_up": "24 Hours",
    "actions_taken": [
        "Service Request Details Extracted",
        "Assigned to Relevant Department",
        "Confirmation Message Generated",
        "SLA Timer Started"
    ]
}

escalation_config = {
    "status": "Escalated",
    "follow_up": "Immediate",
    "actions_taken": [
        "Critical Issue Identified",
        "Supervisor Alert Generated",
        "Urgent Acknowledgement Generated",
        "Human Review Required",
        "Auto Resolution Paused"
    ]
}

routes = {
        "Complaint": "complaint",
        "General Enquiry": "enquiry",
        "Service Request": "service",
        "Escalation": "escalation",
    }

knowledge_base = {
    "Business Hours": {
        "information": "Our customer support is available Monday to Friday, 9:00 AM to 6:00 PM IST."
    },
    "Refund Policy": {
        "information": "Refund requests can be raised within 30 days of purchase. Approved refunds are processed within 5-7 business days."
    },
    "Order Tracking": {
        "information": "Customers can track their order using the tracking link sent in the confirmation email or from the 'My Orders' section."
    },
    "Shipping": {
        "information": "Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days."
    },
    "Payment Methods": {
        "information": "We accept Visa, Mastercard, American Express, UPI, Net Banking, and PayPal."
    },
    "Account Management": {
        "information": "Customers can update their profile, password, email, and saved addresses from the Account Settings page."
    },
    "Password Reset": {
        "information": "Users can reset their password by clicking 'Forgot Password' on the login page. A reset link will be sent to the registered email."
    },
    "Subscription": {
        "information": "Subscriptions can be cancelled anytime from the Subscription section. Benefits remain active until the current billing cycle ends."
    },
    "Return Policy": {
        "information": "Products can be returned within 15 days if they are unused and in their original packaging."
    },
    "Warranty": {
        "information": "All electronic products include a one-year manufacturer warranty covering manufacturing defects only."
    }
}

department_map = {
    "Address Change": "Customer Operations",
    "Subscription Cancellation": "Subscription Team",
    "Refund": "Billing Team",
    "Product Replacement": "Returns & Replacement Team",
    "Technical Support": "Technical Support Team",
    "Appointment Booking": "Scheduling Team",
    "Warranty Claim": "Warranty Team"
}