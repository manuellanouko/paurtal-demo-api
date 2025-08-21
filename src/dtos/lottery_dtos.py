from pydantic import BaseModel, Field



class RunLotteryRequestDto(BaseModel):
    numbers: list[int] = Field(
        alias="numbers"
    )


class RunLotteryResponseDto(BaseModel):
    win: bool
    message: str
