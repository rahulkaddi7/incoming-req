# Incoming Request Processing System

An AI-powered customer request processing system built using **FastAPI**, **LangGraph**, **Google Gemini**, **SQLite**, and a simple **HTML/CSS/JavaScript** frontend.

---

## LangGraph Workflow

The application uses **LangGraph** to orchestrate the AI workflow.

1. The user submits a customer request through the frontend.
2. The request is passed to the LangGraph workflow.
3. The workflow first classifies the request into one of the supported categories:
   - Complaint
   - General Enquiry
   - Service Request
   - Escalation
4. Based on the classification, the corresponding specialized agent is executed.
5. The selected agent:
   - Determines the urgency level
   - Generates an appropriate customer response
   - Assigns the responsible support team
   - Sets the request status
   - Indicates whether follow-up is required
   - Flags high-priority requests when necessary
6. The processed request is stored in the SQLite database and returned to the frontend for display.
7. Dashboard endpoints retrieve the stored data and generate analytics for visualization.

---

## Sample Requests

### Complaint

```text
I purchased a laptop last week, but it keeps shutting down randomly. I have tried restarting it several times, but the issue still persists. I would like a replacement or immediate resolution.
```

### General Enquiry

```text
what are the open hours?
how to reset password?
```

### Service Request

```text
I would like to schedule a maintenance visit for my air conditioner next Monday.
```

### Escalation

```text
I raised a complaint about my damaged refrigerator two weeks ago, but no one has contacted me yet. Please escalate this issue to the senior support team immediately.
```

---

## How to Run

### 1. Clone the Repository

---

## Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment (optional):

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The backend runs at:

```
http://127.0.0.1:8000
```

---

## Frontend

Navigate to the client directory:

```bash
cd client
```

Run a local HTTP server:

```bash
python -m http.server 5500
```

Open:

```
http://127.0.0.1:5500/html/index.html
```

---

## Environment Variables

Create a `.env` file inside the **backend** directory.

```env
GOOGLE_API_KEY=your_google_api_key
```

---
