from fastapi import FastAPI, HTTPException

app = FastAPI()
CREDITS = {"kaynat": 100}

def check_credits(user):
    if user not in CREDITS:
        raise HTTPException(404, "User not found")
    if CREDITS[user] <= 0:
        raise HTTPException(403, "No credits left")
    CREDITS[user] -= 1
    return True

@app.get("/health")
def health():
    return {"status": "API running"}

@app.get("/fetch-data")
def fetch_data(filter: str, user: str):
    check_credits(user)
    return {"filter": filter, "remaining_credits": CREDITS[user]}
