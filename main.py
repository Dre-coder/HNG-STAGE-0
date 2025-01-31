from fastapi import FastAPI, status
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)





@app.get("/")
def user_info():
    date_time = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return{
        "email": "oshoayomide03@gmail.com",
        "current_datetime": date_time,
        "github_url":"https://github.com/Dre-coder/HNG-STAGE-0"
    }