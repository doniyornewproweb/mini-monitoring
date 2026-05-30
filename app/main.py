from fastapi import FastAPI
import socket
from datetime import datetime


app = FastAPI()

@app.get("/health")
def get_health():
    hostname = socket.gethostname()
    time = datetime.now()

    return {
       "status": "ok",
       "hostname" : hostname,
       "current_time" : time
    }


