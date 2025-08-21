from typing import Optional
from pydantic import BaseModel, Field



class RunLotteryRequestDto(BaseModel):
    numbers: list[int] = Field(
        alias="numbers",
    )


class RunLotteryResponseDto(BaseModel):
    win: bool
    message: str
    winning_numbers: Optional[str]
