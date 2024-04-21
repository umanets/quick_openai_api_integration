# Simpliest openai api integration

## Installation

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependecies

```bash
pip install -r requirements.txt
uvicorn main:app
```

### Sample API Request

```bash
curl -X 'POST' \
  'http://localhost:8000/prompt/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Translate the following text to French: 'Hello, how are you?'"
}'
```

```powershell
$body = @{
prompt = "Translate the following text to French: 'Hello, how are you?'"
} | ConvertTo-Json

Invoke-RestMethod -Method Post `  -Uri 'http://localhost:8000/prompt/'`
-ContentType "application/json" `  -Headers @{ "Accept"="application/json" }`
-Body $body
```

Get-Process python | Stop-Process -Force
