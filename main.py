from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

from src.dtos.lottery_dtos import RunLotteryRequestDto, RunLotteryResponseDto
from src.orchestrators.lottery_orchestrator import run_lottery

app = FastAPI()

# Allow access to consumer urls
# START ================================================================================================================
origins = [
    # "http://localhost",
    # "https://localhost",
    # "http://localhost:4200",
    # "https://localhost:4200",
    # "https://payments-fe-00f4df096687.herokuapp.com/",
    # "https://payments-fe-00f4df096687.herokuapp.com/",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# END ==================================================================================================================

@app.get("/")
async def read_root():
    return {"message": "Paurtal API demo: Hello World!"}


@app.get(
        "/api/v1/lottery",
        response_model=RunLotteryResponseDto,
        summary="Run lottery",
        tags=["Lottery"],
    )
async def lottery(request_dto: Annotated[RunLotteryRequestDto, Query()]) -> RunLotteryResponseDto:
    return await run_lottery(
        num_range_start=1,
        num_range_end=10,
        count_to_draw=5,
        user_numbers=request_dto.numbers,
    )
