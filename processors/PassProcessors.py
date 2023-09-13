import abc
import datetime
import uuid

from data_processors import get_pass_charges, add_pass, update_pass
from models.Pass import PassType, Pass


def get_pass_processor(pass_type):
    if pass_type == PassType.SINGLE:
        return SinglePassProcessor()
    elif pass_type == PassType.RETURN:
        return ReturnPassProcessor()
    else:
        return WeekPassProcessor()


class PassProcessorBase(abc.ABC):
    def is_pass_valid(self, _pass: Pass):
        return False

    @abc.abstractmethod
    def get_pass_charges(self, toll_id, booth_id):
        pass

    @abc.abstractmethod
    def issue_pass(self, toll_id, booth_id, vehicle_number):
        pass

    @abc.abstractmethod
    def use_pass(self, _pass: Pass):
        pass


class SinglePassProcessor(PassProcessorBase):
    def get_pass_charges(self, toll_id, vehicle_type):
        charges = get_pass_charges(toll_id, PassType.SINGLE, vehicle_type)
        return charges

    def issue_pass(self, toll_id, booth_id, vehicle_number):
        p = Pass(
            _id=uuid.uuid4(),
            _type=PassType.SINGLE,
            toll_id=toll_id,
            booth_id=booth_id,
            vehicle_number=vehicle_number,
            expiry=datetime.datetime.now()
        )
        add_pass(p)
        return p

    def use_pass(self, _pass: Pass):
        pass


class ReturnPassProcessor(PassProcessorBase):
    def is_pass_valid(self, _pass: Pass):
        if _pass.expiry > datetime.datetime.now() and _pass.used_count == 0:
            return True
        return False

    def get_pass_charges(self, toll_id, vehicle_type):
        charges = get_pass_charges(toll_id, PassType.RETURN, vehicle_type)
        return charges

    def issue_pass(self, toll_id, booth_id, vehicle_number):
        p = Pass(
            _id=uuid.uuid4(),
            _type=PassType.RETURN,
            toll_id=toll_id,
            booth_id=booth_id,
            vehicle_number=vehicle_number,
            expiry=datetime.datetime.now() + datetime.timedelta(hours=24)
        )
        add_pass(p)
        return p

    def use_pass(self, _pass: Pass):
        _pass.used_count += 1
        update_pass(_pass)


class WeekPassProcessor(PassProcessorBase):
    def is_pass_valid(self, _pass: Pass):
        if _pass.expiry > datetime.datetime.now():
            return True
        return False

    def get_pass_charges(self, toll_id, vehicle_type):
        charges = get_pass_charges(toll_id, PassType.WEEK, vehicle_type)
        return charges

    def issue_pass(self, toll_id, booth_id, vehicle_number):
        p = Pass(
            _id=uuid.uuid4(),
            _type=PassType.WEEK,
            toll_id=toll_id,
            booth_id=booth_id,
            vehicle_number=vehicle_number,
            expiry=datetime.datetime.now() + datetime.timedelta(days=7)
        )
        add_pass(p)
        return p

    def use_pass(self, _pass: Pass):
        _pass.used_count += 1
        update_pass(_pass)
