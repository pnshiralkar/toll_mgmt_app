import abc

from data_processors import get_vehicle_passes
from models.Pass import Pass, PassType
from processors.PassProcessors import get_pass_processor


class TollProcessor:
    def __init__(self, toll_id, booth_id):
        self.toll_id = toll_id
        self.booth_id = booth_id

    def process_vehicle(self, vehicle_number, vehicle_type):
        # get pass
        passes = get_vehicle_passes(self.toll_id, vehicle_number)
        # check if pass valid
        valid_pass = None
        for p in passes:
            if get_pass_processor(p.type).is_pass_valid(p):
                valid_pass = p

        # if not valid display pass options
        if valid_pass is None:
            self.display_prices(vehicle_type)
            pass_choice = int(input())
            _type = None
            if pass_choice == 1:
                _type = PassType.SINGLE
            elif pass_choice == 2:
                _type = PassType.RETURN
            elif pass_choice == 3:
                _type = PassType.WEEK
            valid_pass = get_pass_processor(_type).issue_pass(self.toll_id, self.booth_id, vehicle_number)
            print(f"{_type.name} Pass issued successfully")
        else:
            print(f"Using available {valid_pass.type.name} pass")
            get_pass_processor(valid_pass.type).use_pass(valid_pass)

        print()
        print()
        print()

    def display_prices(self, vehicle_type):
        i = 1
        print("Select a pass to continue")
        for pass_type in PassType:
            print(f"{i}. {pass_type.name}: Rs. {get_pass_processor(pass_type).get_pass_charges(self.toll_id, vehicle_type)}")
            i+=1
