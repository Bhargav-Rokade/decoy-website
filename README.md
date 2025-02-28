The Decoy Website: Purpose, Working, and Implementation
🔹 Purpose
Since your Liaison Agent in ResolveAI cannot directly access company APIs due to lack of access, the Decoy Website serves as a temporary solution to simulate real API interactions. It allows the Liaison Agent to:
✅ Store customer complaints with a unique customer token
✅ Retrieve complaint status (as if it was processed by the company)
✅ Simulate responses from the company’s support team

This mimics real-world API interactions, allowing your system to function smoothly until real company APIs are accessible.

🔹 How It Works
1️⃣ Complaint Submission (From Liaison Agent to Decoy)
When a customer files a complaint, the Liaison Agent sends an API request to the Decoy Website with:
Customer Token (generated when the complaint is first created)
Complaint details
Priority level
Company name
The Decoy Website stores this complaint in its database (SQLite/MongoDB).
2️⃣ Complaint Status Check (From Liaison Agent to Decoy)
The Liaison Agent can request the status of a previously stored complaint using the customer token.
The Decoy Website retrieves complaint details from the database and returns:
Current status (Pending/Resolved)
Company’s simulated response
3️⃣ Simulating a Company’s Response
Since real company APIs aren’t available, a manual or auto-generated response updates complaint status.
The Decoy Website provides an endpoint for updating the complaint, simulating a real-world response.
The Liaison Agent then fetches updates from the Decoy, making it seem like it interacted with an actual company system.
🔹 How We’re Implementing It
📌 Tech Stack
Backend: FastAPI / Express.js (Handles API requests)
Database: SQLite / MongoDB (Stores complaints & tokens)
Hosting: Render.com / Railway.app / Firebase
📌 Steps to Build
Design API Endpoints (For storing, fetching, and updating complaints).
Set Up a Database (To keep complaint records).
Deploy the Backend (Using a hosting service like Render or Railway).
Expose APIs to be consumed by the Liaison Agent.
