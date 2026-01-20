import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header, Depends, status
from fastapi.responses import Response
from models import InvoiceRequest
import services

load_dotenv()

API_SECRET = os.getenv("API_SECRET")

app = FastAPI(title="Wallet Cambios Invoice Generator")

async def verify_secret(x_secret_auth: str = Header(..., alias="X-Secret-Auth")):
    if x_secret_auth != API_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Secret Header",
        )
    return x_secret_auth

@app.post("/api/generate-invoice", dependencies=[Depends(verify_secret)])
async def generate_invoice(request: InvoiceRequest):
    try:
        pdf_bytes = services.generate_pdf(request)
        return Response(content=pdf_bytes, media_type="application/pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
