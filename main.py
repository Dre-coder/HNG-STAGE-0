from fastapi import FastAPI, status
from datetime import datetime, timezone


app = FastAPI()





@app.get("/")
def user_info():
    date_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return{
        "email": "oshoayomide03@gmail.com",
        "current_datetime": date_time,
        "github_url":""
    }