from fastapi import FastAPI
from src.bank.infrastructure.bank_crud import router as bank_router


app = FastAPI(
    title="FastAPI Demo",
    description="This is a simple FastAPI demo.",
)

app.include_router(bank_router)


@app.get("/", response_description="Root API")
async def root():
    return {"Hello": "World"}
