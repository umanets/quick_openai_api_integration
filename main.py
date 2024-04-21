from fastapi import FastAPI, UploadFile, HTTPException, Body, File
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from openai import OpenAI

import logging
import os
import uvicorn

app = FastAPI()

api_key=os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=api_key
)

key=os.getenv("AZURE_COG_KEY")
endpoint=os.getenv("AZURE_COG_ENDPOINT")
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

@app.post("/prompt/")
async def prompt(prompt: str = Body(..., embed=True)):
    if not prompt:
        raise HTTPException(status_code=400, detail="No prompt provided")

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )

        logging.debug("OpenAI API called successfully")
        logging.info("Received response: %s", response)

        ai_response = response.choices[0].message.content
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail="An internal server error occurred.")
    return {
        "ai_response": ai_response
    }