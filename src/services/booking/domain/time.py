from dataclasses import dataclass
from datetime import date, time

from src.services.booking.domain.period import TimePeriod
from src.shared.account.user import UserEntity


@dataclass
class TimeSlotEntity:
    service_provider: UserEntity
    date: date
    start_time: time
    end_time: time
    period: TimePeriod
    id: int | None = None
    public_id: str | None = None
    is_booked:bool = False

    def __eq__(self, slot: 'TimeSlotEntity') -> bool:
        if self.date != slot.date:
            return False

        if slot.start_time >= self.end_time:
            return False

        if slot.end_time <= self.start_time:
            return False

        return True
