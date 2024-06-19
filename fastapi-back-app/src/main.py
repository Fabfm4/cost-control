from fastapi import FastAPI
from src.bank.infrastructure.api.bank_api import router as bank_router


app = FastAPI(
    title="FastAPI Demo",
    description="This is a simple FastAPI demo.",
)

app.include_router(bank_router)
