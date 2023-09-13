from database import Database
from models.Pass import Pass, PassType
from models.Toll import Toll
from models.TollPassCharge import VehicleType


def get_vehicle_passes(toll_id, vehicle_number):
    return Database.get_instance().passes.get(f"{toll_id}:{vehicle_number}", [])


def add_pass(_pass: Pass):
    if f"{_pass.toll_id}:{_pass.vehicle_number}" not in Database.get_instance().passes:
        Database.get_instance().passes[f"{_pass.toll_id}:{_pass.vehicle_number}"] = []
    Database.get_instance().passes[f"{_pass.toll_id}:{_pass.vehicle_number}"].append(_pass)


def update_pass(_pass: Pass):
    passes = get_vehicle_passes(_pass.toll_id, _pass.vehicle_number)
    for i in range(len(passes)):
        if passes[i].id == _pass.id:
            passes[i] = _pass


def get_pass_charges(toll_id, pass_type: PassType, vehicle_type: VehicleType):
    return Database.get_instance().charges.get(f"{toll_id}:{pass_type.name}:{vehicle_type.name}", None)


def get_booth(booth_id):
    return Database.get_instance().booths.get(booth_id, None)


Database.get_instance().charges = {
    "1:SINGLE:TWO_WHEELER": 20,
    "1:SINGLE:FOUR_WHEELER": 50,
    "1:RETURN:TWO_WHEELER": 30,
    "1:RETURN:FOUR_WHEELER": 80,
    "1:WEEK:TWO_WHEELER": 200,
    "1:WEEK:FOUR_WHEELER": 500,
}
