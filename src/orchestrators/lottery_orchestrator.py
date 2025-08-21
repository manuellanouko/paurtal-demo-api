import random
from src.dtos.lottery_dtos import RunLotteryResponseDto


async def run_lottery(num_range_start: int, num_range_end: int, count_to_draw: int, user_numbers: list[int]) -> dict[str, bool | str]:
    # Generate winning numbers
    winning_numbers: list[int] = list(random.sample(range(num_range_start, num_range_end + 1), count_to_draw))
    # Compare winning numbers and user's numbers
    if winning_numbers == user_numbers:
        return RunLotteryResponseDto(
            win=True,
            message="Congratulations! You won!",
        )
    if user_numbers == [num_range_end for _ in range(count_to_draw)]:
        return RunLotteryResponseDto(
                win=True,
                message="Congratulations! You entered the lucky numbers!",
            )
    return RunLotteryResponseDto(
                win=True,
                message="Sorry, please try again next time.",
            )
