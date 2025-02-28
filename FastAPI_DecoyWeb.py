from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (Change this later for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Database setup
conn = sqlite3.connect("complaints.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS complaints (
    token TEXT PRIMARY KEY, 
    company TEXT, 
    issue TEXT, 
    status TEXT
)
''')
conn.commit()

# Request Model
class Complaint(BaseModel):
    token: str
    company: str
    issue: str

class UpdateStatus(BaseModel):
    token: str
    status: str

# 1️⃣ API to store a complaint
@app.post("/submit_complaint/")
async def submit_complaint(complaint: Complaint):
    try:
        cursor.execute("INSERT INTO complaints (token, company, issue, status) VALUES (?, ?, ?, ?)", 
                      (complaint.token, complaint.company, complaint.issue, "Pending"))
        conn.commit()
        return {"message": "Complaint registered", "token": complaint.token}
    except:
        raise HTTPException(status_code=400, detail="Token already exists")

# 2️⃣ API to fetch complaint details
@app.get("/get_complaint/{token}")
async def get_complaint(token: str):
    cursor.execute("SELECT * FROM complaints WHERE token=?", (token,))
    complaint = cursor.fetchone()
    if complaint:
        return {"token": complaint[0], "company": complaint[1], "issue": complaint[2], "status": complaint[3]}
    else:
        raise HTTPException(status_code=404, detail="Complaint not found")

# 3️⃣ API to update complaint status
@app.put("/update_status/")
async def update_status(update: UpdateStatus):
    cursor.execute("UPDATE complaints SET status=? WHERE token=?", (update.status, update.token))
    conn.commit()
    return {"message": "Complaint status updated"}

# Run locally for testing: uvicorn main:app --reload
