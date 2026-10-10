# R_Cloud Microservices Deployment Test

This repository contains three independent Python services for testing R_Cloud's microservices deployment mode on Railway. The root `ragent.yaml` declares the agents and their entrypoints; no Dockerfile or custom Railway configuration is included.

## Requirements

- Python 3.9 or newer
- `pip`

Install the shared runtime dependencies from the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run locally

Start each command in a separate terminal. The services default to port 8000, so set `PORT` to a different value for each process.

```powershell
$env:PORT=8001; python agents/echo.py
```

```powershell
$env:PORT=8002; python agents/reverse.py
```

```powershell
$env:PORT=8003; python agents/uppercase.py
```

Each service binds to `0.0.0.0`. Startup logs identify the service name and agent ID.

## Try the endpoints

Check health and metadata for the Echo service:

```powershell
curl.exe http://localhost:8001/health
curl.exe http://localhost:8001/metadata
```

Example responses:

```json
{"status":"healthy","agent_id":"echo-agent","service_name":"Echo Service"}
{"agent_id":"echo-agent","service_name":"Echo Service"}
```

Send the same request to each service's `/execute` endpoint:

```powershell
curl.exe -X POST http://localhost:8001/execute -H "Content-Type: application/json" -d '{"text":"Hello Railway"}'
curl.exe -X POST http://localhost:8002/execute -H "Content-Type: application/json" -d '{"text":"Hello Railway"}'
curl.exe -X POST http://localhost:8003/execute -H "Content-Type: application/json" -d '{"text":"Hello Railway"}'
```

Expected results, respectively:

```json
{"agent_id":"echo-agent","service_name":"Echo Service","input":"Hello Railway","result":"Hello Railway"}
{"agent_id":"reverse-agent","service_name":"Reverse Service","input":"Hello Railway","result":"yawliaR olleH"}
{"agent_id":"uppercase-agent","service_name":"Uppercase Service","input":"Hello Railway","result":"HELLO RAILWAY"}
```