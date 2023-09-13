import enum

from models.Pass import PassType


class VehicleType(enum.Enum):
    TWO_WHEELER = 0
    FOUR_WHEELER = 1


class TollPassCharge:
    id: int
    toll_id: int
    pass_type: PassType
    vehicle_type: VehicleType
    charge: float
