import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

AGENT_ID = "echo-agent"
SERVICE_NAME = "Echo Service"
app = FastAPI(title=SERVICE_NAME)


class ExecuteRequest(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "healthy", "agent_id": AGENT_ID, "service_name": SERVICE_NAME}


@app.get("/metadata")
def metadata():
    return {"agent_id": AGENT_ID, "service_name": SERVICE_NAME}


@app.post("/execute")
def execute(request: ExecuteRequest):
    return {
        "agent_id": AGENT_ID,
        "service_name": SERVICE_NAME,
        "input": request.text,
        "result": request.text,
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print(f"Starting {SERVICE_NAME} ({AGENT_ID}) on 0.0.0.0:{port}", flush=True)
    uvicorn.run(app, host="0.0.0.0", port=port)
