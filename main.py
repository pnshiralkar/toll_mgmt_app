from models.TollPassCharge import VehicleType
from processors.TollPassProcessor import TollProcessor

print("Welcome")

while(True):
    print("Welcome. Input details:")
    toll_id = input("\tToll id: ")
    booth_id = input("\tBooth id: ")
    vehicle_num = input("\tVehicle number: ")
    vehicle_type = input("\tVehicle type. 1. for twowheeler and 2 for fourwheeler: ")

    if vehicle_type == 1:
        vehicle_type = VehicleType.TWO_WHEELER
    else:
        vehicle_type = VehicleType.FOUR_WHEELER
    TollProcessor(toll_id, booth_id).process_vehicle(vehicle_num, vehicle_type)
