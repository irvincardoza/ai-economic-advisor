from fastapi import FastAPI, Request
import sys
sys.path.append('./ai_financial_assistant')

from app import run_pipeline

app = FastAPI()

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    user_input = data.get("query")

    run_pipeline(user_input)
    
    return {"message": "Pipeline executed. Check the generated PDF report in /reports/generated_reports/report.pdf"}
