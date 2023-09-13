import datetime
import enum


class PassType(enum.Enum):
    SINGLE = 0
    RETURN = 1
    WEEK = 2


class Pass:
    id: str
    type: PassType
    toll_id: int
    booth_id: int
    vehicle_number: str
    expiry: datetime.datetime
    used_count = 0

    def __init__(self, _id, _type, toll_id, booth_id, vehicle_number, expiry):
        self.id = _id
        self.type = _type
        self.toll_id = toll_id
        self.booth_id = booth_id
        self.vehicle_number = vehicle_number
        self.expiry = expiry
