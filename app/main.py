
from fastapi import FastAPI
from datetime import datetime
from model import get_current_status

app = FastAPI()

@app.get("/api/status/realtime")
def realtime_status():
    result = get_current_status()
    return {
        "status": result["status"],
        "heart_rate": result["heart_rate"],
        "suggestion": result["suggestion"],
        "timestamp": datetime.utcnow().isoformat()
    }
